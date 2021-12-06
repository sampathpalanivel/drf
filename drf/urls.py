"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include
from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token
apiVersion = "api/v1"

schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="test@gmail.com"),
        license=openapi.License(name="TEST License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
#  permission_classes=[permissions.AllowAny]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path(apiVersion, TestView.as_view(), name="Test"),
    path('api/token', obtain_auth_token, name="Token"),
    # path(r'^swagger(?P<format>\.json|\.yaml)$',
    #      schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),  # new

    # path('redoc/', schema_view.with_ui('redoc',
    #                                    cache_timeout=0), name='schema-redoc'),

]
