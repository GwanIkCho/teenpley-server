# Generated by Django 5.0.2 on 2024-03-20 11:33

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_alter_club_club_info'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='clubpost',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='clubpostreply',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]