"""djdigitalhub URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
]

# Errors
handler404 = 'djdigitalhub.views.not_found'
handler500 = 'djdigitalhub.views.server_error'
handler403 = 'djdigitalhub.views.permission_denied'
handler400 = 'djdigitalhub.views.bad_request'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)