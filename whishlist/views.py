from rest_framework import viewsets
from .models import Wishlist, Item
from .mixins import ReservedMixin
from .serializers import WishlistSerializer, WishesSerializer
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly


class WishlistViewSet(ReservedMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()


class WishlistCRUDViewSet(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()


class WishViewSet(ReservedMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = WishesSerializer
    queryset = Item.objects.all()


class MailSenderView(viewsets.ViewSet):

    def create(self, request, pk):
        from_mail = request.user.email
        mailto = request.data.get('mailto')
        wishlist_url = get_object_or_404(Wishlist, id=pk).url
        send_mail('New Files have been Uploaded',
                  wishlist_url,
                  from_mail,
                  [mailto, ],
                  fail_silently=False)
        return Response()
