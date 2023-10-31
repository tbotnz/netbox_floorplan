from setuptools import find_packages, setup

setup(
    name="netbox-floorplan-plugin",
    version="0.1.1",
    author="Tony Nealon",
    author_email="tony@worksystems.co.nz",
    description="Netbox Plugin to support graphical floorplans",
    url="https://github.com/netboxlabs/netbox-floorplan-plugin.git",
    license="LGPLv3+",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
