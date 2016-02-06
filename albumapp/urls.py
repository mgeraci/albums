from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.album_lists, name='album_lists_url'),
    url(r'^list/(?P<slug>[^/]+)/$', views.album_list, name='album_list_url'),
]
