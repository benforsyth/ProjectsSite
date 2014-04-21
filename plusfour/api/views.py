from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from plusfour.projects.models import Project, Technology


class ProjectListView(RetrieveAPIView):
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.values('pk', 'name', 'description', 'ranking', 'icon_path')

        return Response(data=projects, status=status.HTTP_200_OK)



class ProjectRetrieveView(RetrieveAPIView):
    model = Project

    def get(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        detail_dict = model_to_dict(project)
        detail_dict['technology'] = project.technology_set.values('pk', 'framework', 'language')
        return Response(data=detail_dict, status=status.HTTP_200_OK)
