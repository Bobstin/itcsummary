from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next/$', views.nextSession, name='nextSession'),
    url(r'^singleSession/(?P<session_number>.*)/$', views.singleSession, name='singleSession'),
    url(r'^$', views.example, name='example'),
]