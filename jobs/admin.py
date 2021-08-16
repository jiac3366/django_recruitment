from django.contrib import admin
from jobs.models import Job, Resume
from django.contrib import messages
from interview.models import Candidate
from datetime import datetime


# Register your models here.
# 模型的管理类--在列表页展示哪些字段
class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        # save_model会保存自动定义好的属性
        super().save_model(request, obj, form, change)


#  HR对应聘者到候选人的转换操作
def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + "," + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人: %s 已成功进入面试流程' % (candidate_names))


enter_interview_process.short_description = u"进入面试流程"

from django.utils.html import format_html


class ResumeAdmin(admin.ModelAdmin):
    actions = (enter_interview_process,)

    # 使得简历Admin能显示出应聘者上传的图片
    def image_tag(self, obj):
        if obj.picture:
            return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
        return ""
    image_tag.allow_tags = True
    image_tag.short_description = '个人照片'

    list_display = (
        'username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'image_tag', 'major',
        'created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", "username", "city", "phone", "picture", "attachment",
            "email", "apply_position", "born_address", "gender",
            "bachelor_school", "master_school", "major", "degree", 'created_date', 'modified_date',
            "candidate_introduction", "work_experience", "project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)
