"""Serializers of the profiles extension."""

from rest_framework import serializers

from . import models


class LotzappSettingsSerializer(serializers.ModelSerializer):
    """Serializer for lotzapp settings."""

    class Meta:
        """Serializer settings."""

        model = models.LotzappSettings
        exclude = ["id"]
        extra_kwargs = {
            "lotzapp_pass": {"write_only": True, "required": False}
        }


class LotzappSyncSerializer(serializers.ModelSerializer):
    """Serializer for lotzapp sync actions."""

    class Meta:
        """Serializer settings."""

        model = models.LotzappSync
        fields = "__all__"
        read_only_fields = ("date", "status", "status_message")
