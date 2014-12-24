from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hour11/',include('hour11.urls', namespace = 'hour11')),
    url(r'^polls/',include('polls.urls', namespace = 'polls')),
    url(r'^admin/', include(admin.site.urls))
)
