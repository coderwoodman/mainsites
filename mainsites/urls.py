from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import blogs.views
import views
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),             
    url(r'^about$',views.about),
    url(r'^blog/$',blogs.views.current_url),
                       
    url(r'^static/(?P<path>.*)$','django.views.static.serve',),
)
