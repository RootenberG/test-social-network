from rest_framework.serializers import ModelSerializer
from .models import Wishlist, Item
from django.contrib.auth.models import User


class FanSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
        )


class WishesSerializer(ModelSerializer):
    # author = FanSerializer()
    class Meta:
        model = Item
        fields = (
            "id",
            "wishlist_id",
            "content",
            "total_reservers",
            # 'author'
        )


class WishlistSerializer(ModelSerializer):
    wishes = WishesSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = (
            "id",
            "name",
            "author_id",
            "wishes",
            "share_url"
        )
