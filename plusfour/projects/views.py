from django.views.generic import DetailView

from plusfour.projects.models import Project


class ProjectDetailView(DetailView):

    model = Project
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['technology_list'] = self.object.technology_set.all()
        return context