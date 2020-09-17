from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import ReservedContentType

User = get_user_model()


def reserve(obj, user):
    """Reserves `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    reserve, is_created = ReservedContentType.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    return reserve


def is_fan(obj, user) -> bool:
    """Checks if  user is reserver.
    """
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    reservers = ReservedContentType.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return reservers.exists()


def get_fans(obj):
    """Gets all users who reserved `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(reserved__content_type=obj_type,
                               reserved__object_id=obj.id)
