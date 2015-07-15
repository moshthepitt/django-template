from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings

from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^page/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    ]
