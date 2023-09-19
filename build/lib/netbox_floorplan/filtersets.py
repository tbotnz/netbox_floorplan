from netbox.filtersets import NetBoxModelFilterSet
from .models import Floorplan


class FloorplanFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Floorplan
        fields = ['id', 'site', 'location']

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
