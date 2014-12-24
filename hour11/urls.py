from django.conf.urls import patterns, url
from hour11 import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$',views.user_login, name='login'),
	url(r'^(?P<username>[\w.,/_\-]+)/$',views.user_page, name='user_page')
)