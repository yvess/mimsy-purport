from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from grapple import urls as grapple_urls

# from search import views as search_views

urlpatterns = [
    url(r"", include(grapple_urls)),
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    # url(r"^search/$", search_views.search, name="search"),
    url(r"", include(wagtail_urls)),
)
