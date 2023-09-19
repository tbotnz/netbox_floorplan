from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from .utils import file_upload

from dcim.models import Rack, Device


class Floorplan(NetBoxModel):
    site = models.ForeignKey(
        to='dcim.Site',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    location = models.ForeignKey(
        to='dcim.Location',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    background_image = models.ImageField(
        upload_to=file_upload,
        blank=True,
        null=True
    )
    width = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    measurement_choices = [
        ('ft', 'Feet'),
        ('m', 'Meters')
    ]
    measurement_unit = models.CharField(
        max_length=2,
        choices=measurement_choices,
        default='m'
    )

    canvas = models.JSONField(default=dict)

    class Meta:
        ordering = ('site', 'location', 'background_image',
                    'width', 'height', 'measurement_unit')

    def __str__(self):
        if self.site:
            return f'{self.site.name} Floorplan'
        else:
            return f'{self.location.name} Floorplan'

    def get_absolute_url(self):
        return reverse('plugins:netbox_floorplan:floorplan_edit', args=[self.pk])

    @property
    def record_type(self):
        if self.site:
            return "site"
        else:
            return "location"

    @property
    def mapped_racks(self):
        drawn_racks = []
        if self.canvas:
            if self.canvas.get("objects"):
                for obj in self.canvas["objects"]:
                    if obj.get("objects"):
                        for subobj in obj["objects"]:
                            if subobj.get("custom_meta"):
                                if subobj["custom_meta"].get("object_type") == "rack":
                                    drawn_racks.append(
                                        int(subobj["custom_meta"]["object_id"]))
        return drawn_racks

    @property
    def mapped_devices(self):
        drawn_devices = []
        if self.canvas:
            if self.canvas.get("objects"):
                for obj in self.canvas["objects"]:
                    if obj.get("objects"):
                        for subobj in obj["objects"]:
                            if subobj.get("custom_meta"):
                                if subobj["custom_meta"].get("object_type") == "device":
                                    drawn_devices.append(
                                        int(subobj["custom_meta"]["object_id"]))
        return drawn_devices

    def resync_canvas(self):
        if self.canvas:
            if self.canvas.get("objects"):
                for index, obj in enumerate(self.canvas["objects"]):
                    if obj.get("custom_meta"):
                        if obj["custom_meta"].get("object_type") == "rack":
                            rack_id = int(obj["custom_meta"]["object_id"])
                            # if rack is not in the database, remove it from the canvas
                            rack_qs = Rack.objects.filter(pk=rack_id)
                            if not rack_qs.exists():
                                self.canvas["objects"].remove(obj)
                            else:
                                rack = rack_qs.first()
                                self.canvas["objects"][index]["custom_meta"]["object_name"] = rack.name
                                if obj.get("objects"):
                                    for subcounter, subobj in enumerate(obj["objects"]):
                                        if subobj.get("type") == "i-text":
                                            if subobj.get("custom_meta", {}).get("text_type") == "name":
                                                self.canvas["objects"][index]["objects"][
                                                    subcounter]["text"] = f"{rack.name}"
                                            if subobj.get("custom_meta", {}).get("text_type") == "status":
                                                self.canvas["objects"][index]["objects"][
                                                    subcounter]["text"] = f"{rack.status}"
                        if obj["custom_meta"].get("object_type") == "device":
                            device_id = int(obj["custom_meta"]["object_id"])
                            # if rack is not in the database, remove it from the canvas
                            device_qs = Device.objects.filter(pk=device_id)
                            if not device_qs.exists():
                                self.canvas["objects"].remove(obj)
                            else:
                                device = device_qs.first()
                                self.canvas["objects"][index]["custom_meta"]["object_name"] = device.name
                                if obj.get("objects"):
                                    for subcounter, subobj in enumerate(obj["objects"]):
                                        if subobj.get("type") == "i-text":
                                            if subobj.get("custom_meta", {}).get("text_type") == "name":
                                                self.canvas["objects"][index]["objects"][
                                                    subcounter]["text"] = f"{device.name}"
                                            if subobj.get("custom_meta", {}).get("text_type") == "status":
                                                self.canvas["objects"][index]["objects"][
                                                    subcounter]["text"] = f"{device.status}"
        self.save()

    def save(self, *args, **kwargs):
        if self.site and self.location:
            raise ValueError(
                "Only one of site or location can be set for a floorplan")
        # ensure that the site or location is set
        if not self.site and not self.location:
            raise ValueError(
                "Either site or location must be set for a floorplan")
        super().save(*args, **kwargs)
