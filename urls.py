from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^events/', include('events.urls')),
#    (r'^committees/', include('committees.urls')),
#    (r'^brothers/', include('brothers.urls')),

#    (r'^admin/', include(admin.site.urls)),
)
