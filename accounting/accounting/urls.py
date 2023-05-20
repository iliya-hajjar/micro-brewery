from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.transaction import urls as transaction_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Projectokay API",
      default_version='v1',
      description="This is the API for accounting service",
   ),
    public=True,
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/transaction/', include(transaction_urls)),
]
