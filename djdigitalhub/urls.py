"""djdigitalhub URL Configuration
"""
# Django Module
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# App view
from django.contrib.auth import views as auth_views
from accounts import views as user_views
from courses import views as course_views
from djdigitalhub.views import HomeView

# Template view
from django.views.generic import TemplateView

# Language
from django.conf.urls.i18n import i18n_patterns

# Sitemap
from django.contrib.sitemaps.views import sitemap
from djdigitalhub.sitemap import (
    StaticViewSitemap, 
    CourseSitemap,
    InstructorSitemap
)

# Error Handler
from django.conf.urls import handler400, handler403, handler404, handler500

sitemaps = {
    'static': StaticViewSitemap,
    'courses': CourseSitemap,
    'instructors': InstructorSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # robots.txt
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    
    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    # Language
    path('i18n/', include('django.conf.urls.i18n')),

    # Home Page
    path('', HomeView, name='home'),

    # Login, Logout, Signup, Password
    path('register/', user_views.UserRegistrationView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # Account
    path('profile/', user_views.ProfileView, name='profile'),
    path('dashboard/', include('memberships.urls', namespace='memberships')),

    # Subscription
    path('subscribe/', include('subscriptions.urls', namespace='subscriptions')),

    # Notification
    path('notifications/', include('notifications.urls', namespace='notifications')),

    # Pages
    path('faqs/', include('pages.urls', namespace='pages')),
    path('search/', include('search.urls', namespace='search')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('instructors/', include('instructors.urls', namespace='instructors')),

    # CK EDITOR
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Errors
handler404 = 'djdigitalhub.views.not_found'
handler500 = 'djdigitalhub.views.server_error'
handler403 = 'djdigitalhub.views.permission_denied'
handler400 = 'djdigitalhub.views.bad_request'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)