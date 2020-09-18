from rest_framework import routers
from .views import WishlistViewSet, MailSenderView, WishViewSet
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'wishlists', WishlistViewSet)
router.register(r'wishes', WishViewSet)


urlpatterns = [
    path(r'auth/', include('rest_framework_social_oauth2.urls')),
    path(r'wishlists/<pk>/send', MailSenderView.as_view({'post': 'create'})),
    path(r'auth2', include('social_django.urls', namespace='social_1')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
