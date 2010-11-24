from django.conf.urls.defaults import url, patterns
from rush.views import view_rush_overview

urlpatterns = patterns('',
    url(r'^$', view_rush_overview, name='view_rush_overview'),
)
