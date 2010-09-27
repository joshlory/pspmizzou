from django.conf.urls.defaults import *
from views import view_index

urlpatterns = patterns('',
    
    (r'^events/', include('events.urls')),
    (r'^committees/', include('committees.urls')),
#    (r'^brothers', include('brothers.urls')),
    url(r'^$', view_index, name='view_index'),

#    (r'^admin', include(admin.site.urls)),
)
