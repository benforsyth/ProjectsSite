from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = \
    patterns('',
             url(r'^$', include('plusfour.projects.urls')),
             url(r'^admin/', include(admin.site.urls)),
             url(r'^api/', include('plusfour.api.urls')),
             url(r'^projects/', include('plusfour.projects.urls')),
             )
