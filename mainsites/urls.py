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
    url(r'^tool$',views.tool),
    url(r'^blog/$',blogs.views.bloglist),
    url(r'^blogadd/$',blogs.views.blog_add),
                       
    url(r'^static/(?P<path>.*)$','django.views.static.serve',),
)
