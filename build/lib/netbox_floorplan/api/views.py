from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import FloorplanSerializer


class FloorplanViewSet(NetBoxModelViewSet):
    queryset = models.Floorplan.objects.all()
    serializer_class = FloorplanSerializer
    filterset_class = filtersets.FloorplanFilterSet
