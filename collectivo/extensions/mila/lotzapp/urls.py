"""URL patterns of the extension."""
from collectivo.utils.routers import DirectDetailRouter
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "mila.lotzapp"


router = DefaultRouter()
router.register("sync", views.LotzappSyncViewSet, basename="sync")
router.register("invoices", views.LotzappInvoiceViewSet, basename="invoices")
router.register("addresses", views.LotzappAddressViewSet, basename="addresses")

srouter = DirectDetailRouter()
srouter.register("settings", views.LotzappSettingsViewSet, basename="settings")

urlpatterns = [
    path("api/lotzapp/", include(router.urls)),
    path("api/lotzapp/", include(srouter.urls)),
]
