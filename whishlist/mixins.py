from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import FanSerializer


class ReservedMixin:
    @action(detail=True, methods=["POST"])
    def reserve(self, request, pk=None):
        """Reserves `obj`.
        """
        obj = self.get_object()
        services.reserve(obj, request.user)
        return Response()

    @action(detail=True, methods=["GET"])
    def fans(self, request, pk=None):
        """Gets all users who reserved `obj`.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)
