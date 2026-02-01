from django.contrib import admin
from django.urls import path , include
from .views import api_router_view
from debug_toolbar.toolbar import debug_toolbar_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Library management API",
      default_version='v1',
      description="Api Document for Library management service usning DRF ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mdsamiulhaque682@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_router_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'), name='api-root'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + debug_toolbar_urls()
