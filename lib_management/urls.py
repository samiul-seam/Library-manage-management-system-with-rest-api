from django.contrib import admin
from django.urls import path , include
from .views import api_router_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', api_router_view),
    path('api/', include('api.urls'), name='api-root'),
]
