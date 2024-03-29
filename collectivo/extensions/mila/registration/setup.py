"""Setup function for the MILA registration extension."""
from collectivo.dashboard.models import DashboardTile
from collectivo.extensions.models import Extension
from collectivo.memberships.models import MembershipStatus

from .models import SurveyGroup, SurveySkill


def setup(sender, **kwargs):
    """Initialize extension after database is ready."""

    extension = Extension.objects.register(
        name="mila_registration",
        label="MILA Registration",
        description="Membership registration for MILA.",
        version="1.0.0",
    )

    DashboardTile.objects.register(
        name="mila_membership_tile",
        label="Membership",
        extension=extension,
        source="component",
        component="mila_membership_tile",
    )

    for status in ["Aktiv", "Investierend"]:
        MembershipStatus.objects.register(name=status)

    # Create survey skills
    for sname in [
        "Immobilien/Architektur/Planung",
        "Einzelhandel",
        "Handwerk (Elektrik, Tischlerei, …)",
        "Genossenschaft/Partizipation/Organisationsentwicklung",
        "Kommunikation (Medien, Grafik, Text,…)",
        "IT/Digitales",
        "Finanzen (BWL, Buchhaltung,…)",
    ]:
        SurveySkill.objects.register(name=sname)

    # Create survey groups
    for gname in [
        "Sortiment",
        "Öffentlichkeitsarbeit",
        "Finanzen",
        "Genossenschaft",
        "IT und Digitales",
        "Events/Infogespräche",
        "Standort",
        "Minimarkt",
        "Diversität",
    ]:
        SurveyGroup.objects.register(name=gname)
