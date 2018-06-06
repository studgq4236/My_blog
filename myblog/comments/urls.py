from django.conf.urls import url
from . import views

app_name = 'commnets'
urlpatterns = [
	url('^comment/post(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment')
]