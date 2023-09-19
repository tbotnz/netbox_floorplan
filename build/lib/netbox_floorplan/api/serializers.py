from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import Floorplan


class FloorplanSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_floorplan-api:floorplan-detail')

    class Meta:
        model = Floorplan
        fields = ['id', 'url', 'site', 'location', 'background_image',
                  'width', 'height', 'tags', 'custom_fields', 'created',
                  'last_updated', 'canvas', 'measurement_unit']
