from netbox.forms import NetBoxModelForm
from .models import Floorplan
from dcim.models import Rack, Device


class FloorplanForm(NetBoxModelForm):
    class Meta:
        model = Floorplan
        fields = ['site', 'location', 'background_image', 'width', 'height']


class FloorplanRackFilterForm(NetBoxModelForm):
    class Meta:
        model = Rack
        fields = ['name']


class FloorplanDeviceFilterForm(NetBoxModelForm):
    class Meta:
        model = Device
        fields = ['name']
