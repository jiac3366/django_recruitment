"""meetingroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.utils.translation import gettext as _
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.models import User
from jobs.models import Job
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation. 4行代码就可以定义一个API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jobs', JobViewSet)


def trigger_error(request):
    division_zero = 1 / 0


urlpatterns = [
    # url(r"^", include("jobs.urls"))
    path('', admin.site.urls),
    # path('admin/', admin.site.urls),
    path('job/', include("jobs.urls")),
    path('accounts/', include('registration.backends.simple.urls')),
    # django rest—framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('error-debug/', trigger_error),
    path('dashboard/', include("dashboard.urls")),
]

# 存文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = _('你好鸭公司招聘系统')
