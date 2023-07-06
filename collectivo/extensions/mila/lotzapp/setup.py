"""Setup function of the mila lotzapp extension."""
import os

from collectivo.core.models import Permission, PermissionGroup
from collectivo.extensions.models import Extension
from collectivo.menus.models import MenuItem

from .models import LotzappSettings


def setup(sender, **kwargs):
    """Initialize extension after database is ready."""

    extension = Extension.objects.register(
        name="mila_lotzapp",
        label="MILA Lotzapp",
        description="Integration with the lotzapp ERP system.",
        version="1.0.0",
    )

    perm_names = [
        "use_lotzapp",
    ]
    superuser = PermissionGroup.objects.get(name="superuser")
    for perm_name in perm_names:
        perm = Permission.objects.register(
            name=perm_name,
            label=perm_name.replace("_", " ").capitalize(),
            description=f"Can {perm_name.replace('_', ' ')}",
            extension=extension,
        )
        superuser.permissions.add(perm)

    MenuItem.objects.register(
        name="lotzapp",
        label="Lotzapp",
        extension=extension,
        route=extension.name + "/admin",
        icon_name="pi-sync",
        requires_perm=("use_lotzapp", "mila_lotzapp"),
        parent="admin",
        order=30,
    )

    settings = LotzappSettings.object()
    settings.lotzapp_url = os.environ.get("LOTZAPP_URL", "")
    settings.lotzapp_user = os.environ.get("LOTZAPP_USER", "")
    settings.lotzapp_pass = os.environ.get("LOTZAPP_PASS", "")
    settings.save()
