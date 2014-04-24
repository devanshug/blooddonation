from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#Valid URLs
urlpatterns = patterns('',
    url(r'^$', 'appviews.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bloodgroupsystem/', 'appviews.views.bloodgroupsystem'),
    url(r'^calculate/', 'appviews.views.calculate'),
    url(r'^data/(?P<state>[a-zA-Z /(/)]+)/$', 'appviews.views.getData'),
    url(r'^details', 'appviews.views.details'),
    url(r'^exists/(?P<username>[a-zA-Z ]+)/$', 'appviews.views.exists'),
    url(r'^facts/', 'appviews.views.facts'),
    url(r'^famousquotes/', 'appviews.views.famousquotes'),
    url(r'^login/', 'appviews.views.login'),
    url(r'^logout/', 'appviews.views.logout'),
    url(r'^qualification/', 'appviews.views.qualified'),
    url(r'^register/', 'appviews.views.register'),
    url(r'^urgent/', 'appviews.views.urgent_blood'),
    url(r'^verify/(?P<code>[a-z0-9]+)/$', 'appviews.views.verify'),
    url(r'^wall/', 'appviews.views.wall'),
)
