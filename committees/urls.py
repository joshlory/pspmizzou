from django.conf.urls.defaults import url, patterns
from django.conf import settings
from committees.views import view_committees_overview, view_committee

urlpatterns = patterns('',
    url(r'^(?P<committee>(' + '|'.join(settings.COMMITTEES) + '))/?$',
        view_committee, name='view_committee'),
    url(r'^$', view_committees_overview, name='view_committees_overview'),
)
