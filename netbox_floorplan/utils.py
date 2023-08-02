def file_upload(instance, filename):
    """
    Return a path for uploading image attchments.
    Adapted from netbox/extras/utils.py
    """
    path = 'netbox-floorplan/'

    if hasattr(instance, 'site'):
        path_prepend = instance.site.id

    return f'{path}{path_prepend}_{filename}'
