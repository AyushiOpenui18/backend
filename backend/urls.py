from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view=get_schema_view(
    openapi.Info(
        title="Backend APIs Document",
        default_version='1.0.0',
        description="This is a swagger document for our APIs"
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('onlineshop.urls')),
    path('swagger/schema/',schema_view.with_ui('swagger',cache_timeout=0),name="Swagger Schema")
]
