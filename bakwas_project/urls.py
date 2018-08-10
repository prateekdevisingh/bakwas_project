"""bakwas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from . import views
# 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^admin/', admin.site.urls),
#     url(r'^firsttemplate/$', views.jsonData),
#     url(r'^api/data/$', views.get_data, name='api-data'),
# #     url(r'^firsttemplate/', views.index),    
# ]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from bakwas_project.views import HomeView, get_data, ChartData


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),
]
