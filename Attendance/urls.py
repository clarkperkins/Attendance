from django.conf.urls import patterns, include, url

from Attendance import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^login/$', views.web_login, name='login'),
    url(r'^logout/$', views.web_logout, name='logout'),
    url(r'^api/$', views.mcc_api, name='api'),
)
