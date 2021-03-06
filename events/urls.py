from django.conf.urls.defaults import url, patterns
from django.conf import settings
from events.views import view_event, view_events_quickview, view_events_overview, view_committee_events

urlpatterns = patterns('',
    url(r'^id/(?P<event_id>\w+)/$', view_event, name='view_event'),
    #url(r'^add/$', add_event, name='add_event'),
    url(r'^(?P<committee>(' + '|'.join(settings.COMMITTEES) + '))/$',
        view_committee_events, name='view_committee_events'),
    url(r'^quickview/$', view_events_quickview, name='view_events_quickview'),
    url(r'^$', view_events_overview, name='view_events_overview'),
)
