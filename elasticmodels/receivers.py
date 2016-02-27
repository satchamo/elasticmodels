from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .indexes import registry


@receiver(post_save)
def update_indexes(sender, **kwargs):
    instance = kwargs['instance']
    registry.update(instance)


@receiver(post_delete)
def delete_from_indexes(sender, **kwargs):
    instance = kwargs['instance']
    # if a delete fails because it can't be found in the index, we don't really
    # care, hence raise_on_error=False
    registry.delete(instance, raise_on_error=False)
