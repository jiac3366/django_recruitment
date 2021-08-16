from django.shortcuts import render

from jobs.models import Job, Cities, JobTypes
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from jobs.models import Resume
from django.http import HttpResponseRedirect
from .forms import ResumeForm

import logging

logger = logging.getLogger(__name__)


# Create your views here.


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context = {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    return render(request, 'joblist.html', context)


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'job_detail.html', {'job': job})
    # render可以防止跨站脚本攻击 把JS代码做转移再渲染到页面
    # 危害：使得管理员打开页面 会意外执行用户上传的js代码 从而发生意外


class ResumeCreateView(LoginRequiredMixin, CreateView):  # Mixin可以达到一个类继承多个类的目的
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone", "born_address",
              "email", "apply_position", "gender",
              "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
              "candidate_introduction", "work_experience", "project_experience"]

    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})

    # 从 URL 请求参数带入CreateView视图作为默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        # 验证表单 验证完就保存
        self.object = form.save(commit=False)
        # 把简历与当前的登陆用户作一个关联
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
