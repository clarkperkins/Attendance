from django.conf.urls import patterns, include, url

from Attendance import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^login/$', views.login, name='login'),
)
