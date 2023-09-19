from django.contrib import admin
from .models import Floorplan


@admin.register(Floorplan)
class FloorplanAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
    )
