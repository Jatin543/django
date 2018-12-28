"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from foo import views
from rest_framework.authtoken import views as authviews

urlpatterns = [
    url(r'^api-token-auth/', authviews.obtain_auth_token),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.view ,name='a'),
    url(r'^ping/' ,views.PingApiView.as_view(),name='b'),
    url(r'^adextractor/' ,views.AdExtractorApiView.as_view(),name='h'),
    url(r'api-login/',views.login,name='api-login')
]
