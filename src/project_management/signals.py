from django.contrib.auth.models import User
from .models import Project

from django.dispatch import receiver
from django.db.models.signals import (
  post_save,
  pre_save,
)


@receiver(pre_save, sender=Project)
def create_project_group(sender, instance, **kwargs):
  '''
  create new ProjectGroup
  '''



@receiver(post_save, sender=Project)
def add_admin_to_project_group(sender, created, instance, **kwargs):
  '''
  add admin to ProjectGroup
  '''