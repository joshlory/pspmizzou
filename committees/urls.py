from django.conf.urls.defaults import url, patterns
from django.conf import settings
from committees.views import view_committees_overview, view_committees_quickview, view_committee

urlpatterns = patterns('',
    url(r'^(?P<committee>(' + '|'.join(settings.COMMITTEES) + '))/$',
        view_committee, name='view_committee'),
    url(r'^quickview/$', view_committees_quickview, name='view_events_quickview'),
    url(r'^$', view_committees_overview, name='view_committees_overview'),
)
