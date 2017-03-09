from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.mainpage, name='homepage'),
	 url(r'^message/$', views.message, name='files'),
	url(r'^project/$', views.project, name='project'),

]