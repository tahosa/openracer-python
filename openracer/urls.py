from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from events.rest import *

router = routers.SimpleRouter()
router.register(r'events', EventsViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openracer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rest/', include(router.urls)),
    url(r'^', include('events.urls')),
)
