from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from views import view_index, view_login, view_logout

urlpatterns = patterns('',
    
    (r'^events/', include('events.urls')),
    (r'^committees/', include('committees.urls')),
#    (r'^brothers', include('brothers.urls')),
    
    url(r'^$', view_index, name='view_index'),
    url(r'^login/', view_login, name='login'),
    url(r'^logout/', view_logout, name='logout'),
    
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + "/static"}),
    )
    