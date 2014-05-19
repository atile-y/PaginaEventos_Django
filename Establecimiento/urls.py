from django.conf.urls import patterns, url

from Establecimiento import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<est_id>\d+)/$', views.detail, name='detail'),
)

