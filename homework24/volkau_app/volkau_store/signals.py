from django.db.models import signals
from django.dispatch import receiver
from volkau_store.models import Category, Games


@receiver(signals.post_save, sender=Games)
def games_number_save(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        category.games_number += 1
        category.save()



@receiver(signals.post_delete, sender=Games)
def games_number_delete(sender, instance, **kwargs):
        category = instance.category
        category.games_number -= 1
        category.save()