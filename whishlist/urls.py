from rest_framework import routers
from .views import WishlistViewSet, MailSenderView, WishViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'wishlists', WishlistViewSet)
router.register(r'wishes', WishViewSet)


urlpatterns = [
    path(r'auth/', include('rest_framework_social_oauth2.urls')),
    path(r'wishlists/<pk>/send', MailSenderView.as_view({'post': 'create'})),
    path(r'auth2', include('social_django.urls', namespace='social_1'))
]

urlpatterns += router.urls
