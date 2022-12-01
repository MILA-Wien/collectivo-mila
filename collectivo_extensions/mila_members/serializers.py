"""Serializers of the members extension."""
from rest_framework import serializers
from . import models


# Fields for all members
editable_fields = (
    'gender',
    'phone', 'email',
    'address_street', 'address_number',
    'address_stair', 'address_door', 'address_postcode',
    'address_city', 'address_country',
)

legal_fields = ('legal_name', 'legal_type', 'legal_id')
natural_fields = ('birthday', )
sepa_fields = ('bank_account_iban', 'bank_account_owner')

optional_fields = (
    'address_stair', 'address_door', 'phone',
    'groups_interested', 'skills'
) + legal_fields + natural_fields + sepa_fields

registration_fields = (
    'first_name', 'last_name', 'person_type',
    'shares_number', 'shares_payment_type',
    'survey_contact', 'membership_type',
    'survey_motivation',
    'groups_interested',
    'skills',
) + legal_fields + natural_fields + sepa_fields

readonly_fields = ('id', 'membership_start',) + registration_fields

summary_fields = (
    'id',
    'first_name', 'last_name',
    'person_type', 'membership_status',
    'membership_start',
    'membership_cancelled',
    'membership_end',
    'tags',
)
tag_fields = {
    'statutes_approved': 'Statutes approved',
    'public_use_approved': 'Public use approved',
    'data_use_approved': 'Data use approved',
    'founding_event': 'Founding event'
}
many_to_many_fields = (
    'skills', 'groups', 'groups_interested', 'children', 'coshoppers'
)
# Create conditions
schema_attrs = {}


def add_conditions(fields, condition_field, value):
    """Add conditions to schema attributes."""
    condition = {
        'field': condition_field, 'condition': 'exact', 'value': value}
    schema_attrs.update({
        attr: {'condition': condition} for attr in fields})


add_conditions(legal_fields, 'person_type', 'legal')
add_conditions(natural_fields, 'person_type', 'natural')
add_conditions(sepa_fields, 'shares_payment_type', 'sepa')


class MemberSerializer(serializers.ModelSerializer):
    """Base serializer for member serializers."""

    schema_attrs = schema_attrs


class MemberRegisterSerializer(MemberSerializer):
    """Serializer for users to register themselves as members."""

    # Tag fields
    statutes_approved = serializers.BooleanField(write_only=True)
    public_use_approved = serializers.BooleanField(write_only=True)
    data_use_approved = serializers.BooleanField(write_only=True)
    founding_event = serializers.BooleanField(write_only=True)

    class Meta:
        """Serializer settings."""

        model = models.Member
        fields = editable_fields + registration_fields \
            + tuple(tag_fields.keys()) + ('id',)
        read_only_fields = ('id',)
        extra_kwargs = {
            field: {'required': field not in optional_fields}
            for field in fields
        }
        extra_kwargs['shares_number']['min_value'] = 1

    def validate(self, attrs):
        """Remove tag fields before model creation."""
        # TODO Include checkboxes in validation
        attrs['tags'] = []
        for field, tag_label in tag_fields.items():
            value = attrs[field]
            attrs.pop(field, None)
            if value is True:
                tag_id = models.MemberTag.objects.get(label=tag_label).id
                attrs['tags'].append(tag_id)
        return super().validate(attrs)


class MemberProfileSerializer(MemberSerializer):
    """Serializer for members to manage their own data."""

    class Meta:
        """Serializer settings."""

        model = models.Member
        fields = registration_fields + editable_fields + readonly_fields
        read_only_fields = registration_fields + readonly_fields


class MemberSummarySerializer(MemberSerializer):
    """Serializer for admins to get member summaries."""

    class Meta:
        """Serializer settings."""

        model = models.Member
        fields = summary_fields


class MemberAdminSerializer(MemberSerializer):
    """Serializer for admins to manage members in detail."""

    class Meta:
        """Serializer settings."""

        model = models.Member
        fields = '__all__'


class MemberTagCreateSerializer(serializers.ModelSerializer):
    """Serializer for new dashboard tiles."""

    class Meta:
        """Serializer settings."""

        model = models.MemberTag
        fields = '__all__'


class MemberTagSerializer(serializers.ModelSerializer):
    """Serializer for member tags."""

    class Meta:
        """Serializer settings."""

        model = models.MemberTag
        fields = '__all__'


class MemberSkillSerializer(serializers.ModelSerializer):
    """Serializer for member skills."""

    class Meta:
        """Serializer settings."""

        model = models.MemberSkill
        fields = '__all__'


class MemberGroupSerializer(serializers.ModelSerializer):
    """Serializer for member groups."""

    class Meta:
        """Serializer settings."""

        model = models.MemberGroup
        fields = '__all__'


class MemberStatusSerializer(serializers.ModelSerializer):
    """Serializer for member status."""

    class Meta:
        """Serializer settings."""

        model = models.MemberStatus
        fields = '__all__'
