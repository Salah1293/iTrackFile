# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PvdmUsers1
from django.db import IntegrityError
import logging



logger = logging.getLogger(__name__)

@receiver(post_save, sender=PvdmUsers1)
def create_or_update_user(sender, instance, created, **kwargs):
    if created:
        try:
            user = User.objects.create(username=instance.username)
            user.set_password(instance.password)  
            user.email = instance.email
            user.save()

            instance.user = user
            instance.save()

            logger.info(f"User created: {user.username}")
        except IntegrityError as e:
            logger.error(f"Failed to create user: {e}")
    else:
        if instance.user:
            user = instance.user
            user.username = instance.username
            user.email = instance.email

            if instance.password:
                user.set_password(instance.password) 
            user.save()

            logger.info(f"User updated: {user.username}")
        else:
            try:
                user = User.objects.create(username=instance.username)
                user.set_password(instance.password)  
                user.email = instance.email
                user.save()

                instance.user = user
                instance.save()

                logger.info(f"User created (on update): {user.username}")
            except IntegrityError as e:
                logger.error(f"Failed to create user on update: {e}")