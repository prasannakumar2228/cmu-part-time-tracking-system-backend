from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile


def CreateProfile(sender, instance, created, **kwargs):
    if created:
        profile=Profile.objects.create(
            user=instance,
            First_Name=instance.first_name,
            Last_Name=instance.last_name,
            Email=instance.email

        )




post_save.connect(CreateProfile,sender=User)