from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^dashboard/$', 'bigbrother.views.dashboard', name='dashboard'),
    url(r'^hola/$', 'bigbrother.views.hola', name='hola'),
    url(r'^monitoring/([a-z]*)/$', 'bigbrother.views.monitoring', name='monitoring'),
    # Examples:
    # url(r'^$', 'bigbrother.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
