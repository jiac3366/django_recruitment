from django.conf.urls import url
from django.urls import path
from jobs import views

urlpatterns = [
    # 职位列表
    path("", views.joblist, name="name"),
    # path("joblist/", views.joblist, name="joblist"),
    # 职位详情
    url(r"(?P<job_id>\d+)/$", views.job_detail, name="job_detail"),
    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name="resume-add"),
]
