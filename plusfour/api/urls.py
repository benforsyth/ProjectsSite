from django.conf.urls import patterns, url

from views import ProjectListView, ProjectRetrieveView

urlpatterns = \
    patterns('',
             url(r'^v1/projects/$', ProjectListView.as_view(), name='project-list'),
             url(r'^v1/projects/(?P<pk>\d+)/$', ProjectRetrieveView.as_view(), name='project-detail')
             )
