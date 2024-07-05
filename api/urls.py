from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import permissions
from drf_yasg import openapi
from .views import Protected
from rest_framework import routers
from django.conf import settings
router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="API crypto_payments",
      default_version='v1',
      description="API documentation",
   ),
   url=f'http://{settings.DOMAIN}/launcher/api/',
   public=True,
   permission_classes=([permissions.AllowAny]),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('rest_framework.urls')),
    path('TokenRefreshView/', TokenRefreshView.as_view(), name='TokenRefreshView'),
    path('TokenObtainPairView/', TokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('Protected/', Protected.as_view(), name='Protected'),
]
