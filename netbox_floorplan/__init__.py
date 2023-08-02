from extras.plugins import PluginConfig


class LocationMapConfig(PluginConfig):
    name = 'netbox_floorplan'
    verbose_name = 'Netbox Location Map'
    description = ''
    version = '0.1'
    base_url = 'floorplan'
    min_version = '3.4.1'


config = LocationMapConfig
