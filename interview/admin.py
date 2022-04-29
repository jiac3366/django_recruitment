from django.contrib import admin
from interview.models import Candidate
from django.contrib import messages
from .dingtalk import send
from .tasks import send_dingtalk_message
from django.http import HttpResponse
import csv
from datetime import datetime
import logging
from interview import candidate_field as cf
from django.db.models import Q

logger = logging.getLogger(__name__)

exportable_fields = (
    'username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
    'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


# Register your models here.
# 导出CSV
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        # 单行 的记录（各个字段的值），根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)
    logger.error(" %s has exported %s candidate records" % (request.user.username, len(queryset)))
    return response


export_model_as_csv.short_description = u'导出为csv文件'

from .tasks import send_dingtalk_message
# 通知一面面试官面试(异步)
def notify_interviewer1(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.first_interviewer_user.username + ";" + interviewers
    # 这里的消息发送到钉钉， 或者通过 Celery 异步发送到钉钉
    # send("候选人%s进入面试环节，请以下各位面试官准备好第一轮面试:%s，谢谢！" % (candidates, interviewers))
    send_dingtalk_message.delay("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers))
    messages.add_message(request, messages.INFO, '已经成功发送通知')


# DJANGO_SETTINGS_MODULE=settings.local celery --app meetingroom worker -l info

notify_interviewer1.short_description = u'通知一面面试官'
notify_interviewer1.allowed_permissions = ('notify1',)


# 通知二面面试官面试(同步)
def notify_interviewer2(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.second_interviewer_user.username + ";" + interviewers
    # 这里的消息发送到钉钉， 或者通过 Celery 异步发送到钉钉
    send("候选人%s进入面试环节，请以下各位面试官准备好第二轮面试:%s，谢谢！" % (candidates, interviewers))
    # send_dingtalk_message.delay("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers))
    messages.add_message(request, messages.INFO, '已经成功发送通知')


notify_interviewer2.short_description = u'通知二面面试官'
# 只有notify2权限的用户才能用这个菜单功能 notify2对应的权限记录在model.py中的permissions定义
notify_interviewer2.allowed_permissions = ('notify2',)


class CandidateAdmin(admin.ModelAdmin):
    actions = (notify_interviewer1, notify_interviewer2, export_model_as_csv,)

    # 当前用户是否有权限：
    def has_notify1_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, "notify1"))

    def has_notify2_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, "notify2"))

    exclude = ('creator', 'created_date', 'modified_date')

    # 右侧筛选条件
    list_filter = (
        'city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user',
        'hr_interviewer_user')

    # 查询字段
    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    # 列表页排序字段
    ordering = ('hr_result', 'second_result', 'first_result',)

    # HR分组展示字段 分2块
    # fieldsets = (
    #     ('第一轮面试', {'fields': (('字段1', '字段2', '字段3'), '字段4', '字段5',)}),
    #     ('第二轮面试', {'fields': ('字段6', '字段7', ('字段8', '字段9', '字段10'))})
    # )

    # form字段权限 根据系统身份设置数据字段权限 一面 二面面试官只能看到对应的部分 但HR和超级管理员可以见到所有
    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if 'Interviewer' in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        if 'Interviewer' in group_names and obj.first_interviewer_user == request.user:
            return cf.default_fieldsets_first
        if request.user.is_superuser or 'HR' in group_names:
            return cf.default_fieldsets
        return ()

    # 记录权限
    def get_queryset(self, request):  # show data only owned by the user
        qs = super(CandidateAdmin, self).get_queryset(request)

        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'HR' in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user)
        )

    # 使相应字段对于所有用户都是只读的 但是并不是我想要的结果 我要面试官只读 HR可修改
    # readonly_fields = ('first_interviewer_user', 'second_interviewer_user',)

    # 使相应字段对于所有用户在列表页可以修改  但是并不是我想要的结果 我要面试官只读 HR可修改
    # list_editable = ('first_interviewer_user', 'second_interviewer_user')

    # 让HR可以在列表上修改面试官是谁 而不用一个一个点进去修改
    def get_list_editable(self, request):
        """
        1.23.2021 18:35
        实现系统的get_list_editable方法
        """
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or 'HR' in group_names:
            return ('first_interviewer_user', 'second_interviewer_user',)
        return ()

    # django没有对list_editable给出方法支持它的设置 所以我们覆盖一下ModelAdmin的get_changelist
    # 在这个方法可以覆盖父类list_editable的属性 让list_editable的值从我们自定义的get_list_editable获取
    def get_changelist_instance(self, request):
        """
        辅助get_list_editable
        override admin method and list_editable property value
        with values returned by our custom method implementation.
        """
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)

    def get_group_names(self, user):
        """
        1.23.2021 18:29
        找出用户所属的群组
        :param user:
        :return: list,用户所属群组的名称
        """
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_readonly_fields(self, request, obj):
        """
        1.23.2021 18:20
        实现系统的get_readonly_fields方法
        """
        group_names = self.get_group_names(request.user)

        if 'Interviewer' in group_names:
            # logger.info("interviewer is in user's group for %s" % request.user.username)
            return ('first_interviewer_user', 'second_interviewer_user')  # 如果该用户是面试官，则返回这2个只读字段
        return ()

    # 列表字段
    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer_user',
        'second_score', 'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',
    )


admin.site.register(Candidate, CandidateAdmin)
