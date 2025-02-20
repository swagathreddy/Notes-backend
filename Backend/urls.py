from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from core.views import CreateUserView, health_check
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # API endpoints
    path('admin/', admin.site.urls),
    path("core/user/register/", CreateUserView.as_view(), name='register'),
    path("core/token/", TokenObtainPairView.as_view(), name='get_token'),
    path("core/token/refresh/", TokenRefreshView.as_view(), name='refresh'),
    path("core-auth/", include("rest_framework.urls")),
    path("core/", include("core.urls")),
    path("health/", health_check, name='health_check'),
    
    # Serve frontend - must be last
    re_path(r'^(?!admin|api|core|health).*', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)