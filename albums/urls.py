from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'albums.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('albumapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
