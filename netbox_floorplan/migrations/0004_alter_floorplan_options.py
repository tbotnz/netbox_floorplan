# Generated by Django 4.1.9 on 2023-07-08 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_floorplan', '0003_floorplan_canvas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='floorplan',
            options={'ordering': ('site', 'location', 'background_image', 'scale', 'measurement_unit')},
        ),
    ]
