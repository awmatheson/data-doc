# Generated by Django 2.0.7 on 2018-08-04 18:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0002_auto_20180804_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Databases',
            new_name='Database',
        ),
    ]
