from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class ReservedContentType(models.Model):
    user = models.ForeignKey(User,
                             related_name="reserved", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total_reservers(self):
        return self.reserved_by.count()

    @property
    def url(self):
        return f"{settings.WHISHLIST_URL}{self.id}"

    @property
    def share_url(self):
        return f"{settings.WHISHLIST_URL}{self.id}/send"

    def __str__(self):
        return self.name  # name to be shown when called


class Item(models.Model):
    wishlist_id = models.ForeignKey(
        Wishlist, related_name="wishes", on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    reserved_by = GenericRelation(ReservedContentType)
    is_done = models.BooleanField(default=False)

    @property
    def author(self):
        return self.wishlist_id.author

    @property
    def total_reservers(self):
        return self.reserved_by.count()

    def __str__(self):
        return self.content  # name to be shown when called
