"""Views of the memberships extension."""
import logging

from collectivo.utils.mixins import HistoryMixin, SchemaMixin
from collectivo.utils.permissions import IsSuperuser
from django.contrib.auth import get_user_model
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from . import serializers
from .models import (
    LotzappAddress,
    LotzappInvoice,
    LotzappSettings,
    LotzappSync,
)

User = get_user_model()
logger = logging.getLogger(__name__)


class LotzappSettingsViewSet(
    SchemaMixin, GenericViewSet, RetrieveModelMixin, UpdateModelMixin
):
    """ViewSet to manage lotzapp settings."""

    queryset = LotzappSettings.objects.all()
    serializer_class = serializers.LotzappSettingsSerializer
    permission_classes = [IsSuperuser]

    def get_object(self):
        """Return single entrys."""
        return self.queryset.get(pk=1)


class LotzappSyncViewSet(
    SchemaMixin,
    HistoryMixin,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """ViewSet to manage lotzapp sync actions."""

    queryset = LotzappSync.objects.all().order_by("-date")
    serializer_class = serializers.LotzappSyncSerializer
    permission_classes = [IsSuperuser]


class LotzappInvoiceViewSet(
    SchemaMixin,
    HistoryMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    """ViewSet to manage lotzapp invoice connections."""

    queryset = LotzappInvoice.objects.all()
    serializer_class = serializers.LotzappInvoiceSerializer
    permission_classes = [IsSuperuser]


class LotzappAddressViewSet(
    SchemaMixin,
    HistoryMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    """ViewSet to manage lotzapp address connections."""

    queryset = LotzappAddress.objects.all()
    serializer_class = serializers.LotzappAddressSerializer
    permission_classes = [IsSuperuser]
