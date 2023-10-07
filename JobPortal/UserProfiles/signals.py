from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Student,Manager
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def UpdateUser(sender, instance, created, **kwargs):
    user = User.objects.get(username=instance.user)
    if created==False:
        user.first_name=instance.First_Name
        user.last_name=instance.Last_Name
        user.email=instance.Email
        user.save()

def DeleteProfile(sender, instance,**kwargs):
    user=instance.user
    user.delete()




post_save.connect(UpdateUser,sender=Student)
post_delete.connect(DeleteProfile,sender=Student)