from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^events/', include('events.urls')),
    (r'^committees/', include('pspmizzou.committees.urls')),
    (r'^brothers/', include('pspmizzou.brothers.urls')),

#    (r'^admin/', include(admin.site.urls)),
)
