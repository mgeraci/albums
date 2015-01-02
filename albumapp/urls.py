from django.conf.urls import patterns, url

urlpatterns = patterns(
    'albumapp.views',
    url(r'^$', 'album_lists', name='album_lists_url'),
    url(r'^list/(?P<slug>[^/]+)$', 'album_list', name='album_list_url'),
)
