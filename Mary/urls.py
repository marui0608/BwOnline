"""Mary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import xadmin
from django.contrib import admin
from django.views.static import serve
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from apps.users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from apps.organization.views import OrgView
from Mary.settings import MEDIA_ROOT

urlpatterns = [
    path('captcha/',include('captcha.urls')),
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)',serve, {'document_root':MEDIA_ROOT}),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path("org/", include('organization.urls', namespace="org")),
    path("course/",include('course.urls',namespace='course')),
]
