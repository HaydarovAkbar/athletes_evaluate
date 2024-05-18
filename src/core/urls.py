from django.contrib import admin
from django.urls import path, include
from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('app/', include('app.urls')),
    path('press_service/', include('press_service.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]