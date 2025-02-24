from django.conf.urls.static import static

from gsmpsite import settings
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from gsmp import views
from gsmp.views import index

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path("__debug__/", include("debug_toolbar.urls")),


]

urlpatterns += i18n_patterns(
    path('', include('gsmp.urls', namespace="gsmp")),
    path('members/', include('members.urls', namespace="members")),
    path('mp_news/', include('mp_news.urls', namespace="mp_news")),
    path('online_encyclopedia/', include('online_encyclopedia.urls', namespace="online_encyclopedia")),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)