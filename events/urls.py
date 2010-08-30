from django.conf.urls.defaults import *
from events.views import view_event, view_events_overview, view_committee_events

urlpatterns = patterns('',
    url(r'^id/(?P<event_id>\w+)/?$', view_event, name='view_event'),
    url(r'^(?P<committee>(' + '|'.join(['service', 'das', 'etc']) + '))/?$',
        view_committee_events, name='view_committee_events'),
    url(r'^$', view_events_overview, name='view_events_overview'),
)
