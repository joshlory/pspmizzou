from django.conf.urls.defaults import *
from events.views import view_event, view_events_overview

urlpatterns = patterns('',
    url(r'^(id/?P<event_id>\w+)/$', view_event, name='view_event'),
    url(r'^/?$', view_events_overview, name='view_events_overview'),
)
