# Generated by Django 2.0.7 on 2018-08-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0020_auto_20180802_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database',
            name='user',
        ),
        migrations.AddField(
            model_name='database',
            name='user',
            field=models.ManyToManyField(to='hello.Profile'),
        ),
    ]