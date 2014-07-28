from django.conf.urls import patterns, include, url
from __APPNAME__.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', index, name='index'),
    #url(r'^admin/', include(admin.site.urls)),
)

