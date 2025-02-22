from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from core.views import CreateUserView, CustomTokenObtainPairView, health_check
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # ✅ Admin Panel
    path('admin/', admin.site.urls),

    # ✅ Authentication Endpoints
    path("core/user/register/", CreateUserView.as_view(), name='register'),
    path("core/token/", CustomTokenObtainPairView.as_view(), name='get_token'),  # Use Custom Token View
    path("core/token/refresh/", TokenRefreshView.as_view(), name='refresh'),

    # ✅ API Routes
    path("core-auth/", include("rest_framework.urls")),
    path("core/", include("core.urls")),
    path("health/", health_check, name='health_check'),

    # ✅ Serve React Frontend (Must be last)
    re_path(r'^(?!admin|core|health|static|media).*$', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
