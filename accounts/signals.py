from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserExtension

@receiver(post_save, sender=User)
def create_user_extension(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(
            user=instance,
            full_name=instance.first_name,
            email=instance.email,
            user_type='normal'  # default
        )
