from django.db.models.signals import post_save
from ..models.contestModel import ContestModel
from django.dispatch import receiver

@receiver(post_save, sender=ContestModel)
def contest_post_save(sender, instance, created, **kwargs):
    if created:instance.active = True