from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Clients')
    Group.objects.get_or_create(name='Doctors')