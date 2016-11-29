"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from apps.account import views as account_views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    # account
    url(r'api/auth$', account_views.AuthenticateViewSet.as_view()),
    url(r'api/auth/social$', account_views.SocialSignUpViewSet.as_view()),
    url(r'api/me$', account_views.MeViewSet.as_view()),
    url(r'api/users$', account_views.UserViewSet.as_view()),

    # Sample
    url(r'api/sample_tasks', account_views.SampleTasksViewSet.as_view()),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
]
