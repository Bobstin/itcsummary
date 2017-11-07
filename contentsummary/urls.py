from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next/$', views.nextSession, name='nextSession'),
    url(r'^all/$', views.allSessions, name='allSessions'),
    url(r'^singleSession/(?P<session_number>[1-9]+)/$', views.singleSession, name='singleSession'),
    url(r'^$', views.example, name='example'),
]