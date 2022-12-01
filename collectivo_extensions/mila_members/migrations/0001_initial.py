# Generated by Django 4.1.3 on 2022-12-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MemberGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberAddon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('person_type', models.CharField(choices=[('child', 'child'), ('coshopper', 'coshopper')], max_length=20)),
                ('birth_date', models.DateField(null=True)),
                ('membership_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mila_members.membercard')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('email_verified', models.BooleanField(null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('person_type', models.CharField(choices=[('natural', 'natural'), ('legal', 'legal')], default='natural', help_text='Type of person.', max_length=20)),
                ('gender', models.CharField(choices=[('diverse', 'diverse'), ('female', 'female'), ('male', 'male')], default='diverse', max_length=20)),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_number', models.CharField(max_length=255, null=True)),
                ('address_stair', models.CharField(max_length=255, null=True)),
                ('address_door', models.CharField(max_length=255, null=True)),
                ('address_postcode', models.CharField(max_length=255, null=True)),
                ('address_city', models.CharField(max_length=255, null=True)),
                ('address_country', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('birthday', models.DateField(null=True)),
                ('legal_name', models.CharField(max_length=255, null=True)),
                ('legal_type', models.CharField(max_length=255, null=True)),
                ('legal_id', models.CharField(max_length=255, null=True)),
                ('membership_start', models.DateField(null=True)),
                ('membership_cancelled', models.DateField(null=True)),
                ('membership_end', models.DateField(null=True)),
                ('membership_type', models.CharField(choices=[('active', 'active'), ('investing', 'investing')], max_length=20)),
                ('shares_number', models.IntegerField(null=True)),
                ('shares_payment_date', models.DateField(null=True)),
                ('shares_payment_type', models.CharField(choices=[('sepa', 'sepa'), ('transfer', 'transfer')], help_text='Type of payment.', max_length=20, null=True)),
                ('bank_account_iban', models.CharField(max_length=255, null=True)),
                ('bank_account_owner', models.CharField(max_length=255, null=True)),
                ('survey_contact', models.TextField(null=True)),
                ('survey_motivation', models.TextField(null=True)),
                ('admin_notes', models.TextField(null=True)),
                ('children', models.ManyToManyField(blank=True, related_name='children', to='mila_members.memberaddon')),
                ('coshoppers', models.ManyToManyField(blank=True, related_name='coshoppers', to='mila_members.memberaddon')),
                ('groups', models.ManyToManyField(blank=True, related_name='groups', to='mila_members.membergroup')),
                ('groups_interested', models.ManyToManyField(blank=True, related_name='groups_interested', to='mila_members.membergroup')),
                ('membership_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mila_members.membercard')),
                ('membership_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mila_members.memberstatus')),
                ('skills', models.ManyToManyField(blank=True, to='mila_members.memberskill')),
                ('tags', models.ManyToManyField(blank=True, to='mila_members.membertag')),
            ],
        ),
    ]
