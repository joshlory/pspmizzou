from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^events/', include('pspmizzou.events.urls')),
    (r'^committees/', include('pspmizzou.committees.urls')),
    (r'^brothers/', include('pspmizzou.brothers.urls')),

    (r'^admin/', include(admin.site.urls)),
)