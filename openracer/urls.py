from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openracer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^events/', include('events.urls')),
)
