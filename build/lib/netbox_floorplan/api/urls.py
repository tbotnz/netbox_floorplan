from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_floorplan'

router = NetBoxRouter()
router.register('floorplans', views.FloorplanViewSet)

urlpatterns = router.urls
