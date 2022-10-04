from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import EmpUser


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        EmpUser.objects.create(empUser=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.empuser.save()
