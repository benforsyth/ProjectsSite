from django.contrib import admin
from plusfour.projects.models import Project, Technology, Owner

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Owner)