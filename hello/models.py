from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    repository = models.CharField(max_length=300, blank=True)
    dag_directory_name = models.CharField(max_length=50, blank=True)
    email_confirmed = models.BooleanField(default=False)
    confirm_password = models.CharField(max_length=150, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Databases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    db_alias = models.CharField(max_length=255)
    db_type = models.CharField(max_length=120)
    db_connection_url = models.TextField()
    schemas = models.TextField()

    def __str__(self):
        return self.db_alias

class Schema(models.Model):
    database = models.ForeignKey(Databases, on_delete=models.CASCADE)
    schema_name = models.CharField(max_length=255)


class Table(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=255)
    description = models.TextField()


class Column(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=80)
    description = models.TextField()