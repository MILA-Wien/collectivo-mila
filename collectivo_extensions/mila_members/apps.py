"""Configuration file for the members extension."""
from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from collectivo.version import __version__


def post_migrate_callback(sender, **kwargs):
    """Initialize extension after database is ready."""
    from collectivo.extensions.utils import register_extension
    from collectivo.menus.utils import register_menuitem
    from collectivo.dashboard.utils import register_tile
    from .utils import (
        register_tag, register_group, register_skill, register_status)

    name = 'mila_members'
    # TODO Language change
    # TODO Error handling
    # TODO Path handling
    # TODO Test put and patch
    # TODO Role filtering menu

    register_extension(
        name=name,
        version=__version__,
        description='An extension to manage member data and registration.'
    )

    register_menuitem(
        item_id='members_user_menu_item',
        menu_id='main_menu',
        label='Membership',
        extension=name,
        action='component',
        component_name='profile',
        required_role='members_user'
    )

    register_menuitem(
        item_id='members_admin_menu_item',
        menu_id='main_menu',
        label='Members',
        extension=name,
        menu='admin_menu',
        action='component',
        component_name='members',
        required_role='members_admin'
    )

    register_tile(
        tile_id='members_registration_tile',
        label='Register as a member',
        extension=name,
        component_name='members_registration_tile',
        blocked_role='members_user'
    )

    tags = [
        'Statutes approved', 'Public use approved', 'Data use approved',
        'Founding event'
    ]
    for label in tags:
        register_tag(label=label)

    status_fields = [
        'Antrag ausstehend', 'Zahlung ausstehend', 'Bestätigung ausstehend',
        'Zahlung fehlgeschlagen', 'Mitglied', 'Gesperrt', 'Beendet'
    ]
    for label in status_fields:
        register_status(label=label)

    if settings.DEVELOPMENT:
        groups = [
            'Infogespräche', 'Sortiment',
            'Öffentlichkeitsarbeit', 'Finanzen',
            'Genossenschaft', 'IT und Digitales',
            'Events', 'Standort', 'Minimarkt'
        ]
        for label in groups:
            register_group(label=label)
        skills = [
            "Immobilien/Architektur/Planung",
            "Einzelhandel",
            "Handwerk (Elektrik, Tischlerei, …)",
            "Genossenschaft/ Partizipation/Organisationsentwicklung",
            "Kommunikation (Medien, Grafik, Text,…)",
            "IT/ Digitales",
            "Finanzen (BWL, Buchhaltung,…)",
        ]
        for label in skills:
            register_skill(label=label)


class MembersConfig(AppConfig):
    """Configuration class for the members extension."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collectivo_extensions.mila_members'

    def ready(self):
        """
        Initialize app when it is ready.

        Database calls are performed after migrations, using the post_migrate
        signal. This signal only works if the app has a models.py module.
        """
        post_migrate.connect(post_migrate_callback, sender=self)
