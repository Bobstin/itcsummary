from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next/(?P<priornumber>[0-9]+)/$', views.nextSession, name='nextSession'),
    url(r'^all/$', views.allSessions, name='allSessions'),
    url(r'^allpt1/$', views.allSessionspt1, name='allSessionspt1'),
    url(r'^allpt2/$', views.allSessionspt2, name='allSessionspt2'),
    url(r'^singleSession/(?P<session_number>[0-9]+)/$', views.singleSession, name='singleSession'),
    url(r'^$', views.example, name='example'),
]