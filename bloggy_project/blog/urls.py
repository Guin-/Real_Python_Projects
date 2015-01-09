from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(
	'blog.views',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
	)

