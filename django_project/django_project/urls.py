from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/', include('hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)