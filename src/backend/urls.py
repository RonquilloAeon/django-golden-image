from apps.account import views as account_views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    # account
    url(r'api/auth$', account_views.AuthenticateView.as_view()),
    url(r'api/me$', account_views.MeView.as_view()),
    url(r'api/users$', account_views.UsersView.as_view()),

    url(r'^admin/', admin.site.urls),
]

# Enable local images and debug toolbar in dev
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
