# Generated by Django 5.0.7 on 2024-07-31 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_app', '0002_hotel_tenant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='tenant',
        ),
    ]
