# netbox floorplan

<img src="https://github.com/tbotnz/netbox_floorplan/workflows/tests/badge.svg" alt="Tests"/>

#### summary
A netbox plugin providing floorplan mapping capability for locations and sites

- provides graphical ability to draw racks & unracked devices on a floorplan
- Support for metadata such as labels, areas, walls, coloring
- floorplan object mapped to sites or locations and click through rack/devices
- keyboard controls supported

#### installing
Install the package, apply migrations then add the plugin to ```PLUGINS = ["netbox_floorplan"]``` in ```/opt/netbox/netbox/netbox/configuration.py:```

#### demo
![demo](/media/demo.gif)