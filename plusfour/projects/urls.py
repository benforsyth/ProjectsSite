from django.conf.urls import patterns, url
from django.views.generic import ListView

from models import Project
from views import ProjectDetailView

urlpatterns = \
    patterns('',
             url(r'^$', ListView.as_view(queryset=Project.objects.order_by('ranking')[:3],
                                         context_object_name='project_list',
                                         template_name='index.html')),
             url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view()),
             )
