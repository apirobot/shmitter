from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


# Register API
apipatterns = [
    url(r'^', include('shmitter.authentication.urls')),
    url(r'^', include('shmitter.tweets.urls')),
    url(r'^', include('shmitter.users.urls')),
]

urlpatterns = [

    url(r'^api/v1/', include((apipatterns, 'api'), namespace='api')),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
