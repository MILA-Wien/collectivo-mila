"""Setup function of the mila lotzapp extension."""
import os

from collectivo.extensions.models import Extension
from collectivo.menus.models import MenuItem

from .models import LotzappSettings


def setup(sender, **kwargs):
    """Initialize extension after database is ready."""

    extension = Extension.register(
        name="mila_lotzapp",
        label="MILA Lotzapp",
        description="Integration with the lotzapp ERP system.",
        version="1.0.0",
    )

    MenuItem.register(
        name="lotzapp",
        label="Lotzapp",
        extension=extension,
        route=extension.name + "/admin",
        icon_name="pi-sync",
        requires_perm=("admin", "core"),
        parent="admin",
        order=30,
    )

    settings = LotzappSettings.object()
    settings.lotzapp_url = os.environ.get("LOTZAPP_URL", "")
    settings.lotzapp_user = os.environ.get("LOTZAPP_USER", "")
    settings.lotzapp_pass = os.environ.get("LOTZAPP_PASS", "")
    settings.save()
