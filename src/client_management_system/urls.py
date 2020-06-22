from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns


# urlpatterns = i18n_patterns(

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agent_portal.urls')),
    path('accounts/', include('allauth.urls')),
]

#     # if no prefixis given, use default language
#     prefix_default_language=False
# )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
