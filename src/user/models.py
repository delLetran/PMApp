from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
  User,
  AbstractUser,
  AbstractBaseUser,
  PermissionsMixin,
  BaseUserManager
)
from django.utils.translation import ugettext_lazy as _
from django.db.models.functions import Lower

from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import (
  post_save,
  pre_save,
  m2m_changed
)


PROJECT = 'project_management.Project'


class CustomUserManager(BaseUserManager): 
  def create_superuser(self, email, username, first_name, last_name, password, **kwargs):
    kwargs.setdefault('is_staff', True)
    kwargs.setdefault('is_superuser', True)
    kwargs.setdefault('is_active', True)

    if kwargs.get('is_staff') is not True:
      raise ValueError('is_staff must be set True for superuser')
    if kwargs.get('is_superuser') is not True:
      raise ValueError('is_superuser must be set True for superuser')
    return self.create_user(email, username, first_name, last_name, password, **kwargs)

  def create_user(self, email, username, first_name, last_name, password, **kwargs):
    return self._create_user(email, username, first_name, last_name, password, **kwargs)

  def _create_user(self, email, username, first_name, last_name, password, **kwargs):
    if not email:
      raise ValueError(_('Enter a valid email address'))
  
    email = self.normalize_email(email)
    user = self.model(
      email=email,
      username=username,
      first_name=first_name,
      last_name=last_name,
      **kwargs
    )
    user.set_password(password)
    user.save()
    return user


class Profile(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_('email address'), max_length=60, unique=True)
  username = models.CharField( max_length=60, unique=True)
  first_name = models.CharField(max_length=60, blank=True, null=True)
  last_name = models.CharField(max_length=60, blank=True, null=True)
  about = models.TextField(_("about"), max_length=512, blank=True, null=True)
  start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  birth_date = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False, blank=True, null=True)
  job_title = models.CharField(max_length=50, blank=True, null=True)
  projects = models.ManyToManyField(PROJECT, verbose_name=_("projects"), related_name='project_list', blank=True, null=True)
  associates = models.ManyToManyField("Profile", verbose_name=_("associates"), blank=True, null=True)
  joined_projects = models.ManyToManyField(PROJECT, verbose_name=_("projects joined"), related_name='joined_project', default=[0], blank=True)
   
  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
  def __str__(self):
    return self.username
 
  class Meta:
    ordering = ['-pk']
    db_table = 'auth_user'
    managed = True
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'

@receiver(pre_save, sender=Profile)
def pre_save_user(sender, instance, *args, **kwargs):
  _username = instance.username.lower()
  instance.username = _username

@receiver(post_save, sender=Profile)
def post_save_user(sender, instance, created, *args, **kwargs):
  if created:
    print(f"{instance.username} created!")

@receiver(post_save, sender=Profile)
def create_auth_token(sender, instance, created, *args, **kwargs):
  if created:
    Token.objects.create(user=instance)
  

# class PeerInvite(models.Model):
#   class STATUS(models.TextChoices):
#     ONHOLD = 'Waiting', 
#     ACCEPTED = 'Accepted',
#     DECLINED = 'Declined',
#   inviter = models.ForeignKey("Profile", verbose_name=_("inviters"), related_name="inviter", on_delete=models.CASCADE)
#   invitee = models.ForeignKey("Profile", verbose_name=_("invitees"), related_name="invitee", on_delete=models.CASCADE)
#   is_active = models.BooleanField(_("invite sent"), default=True)
#   status = models.CharField(_("invite status"), max_length=50, choices=STATUS.choices, default=STATUS.ONHOLD)

#   def __str__(self):
#     return f"{str(self.inviter)}-->{str(self.invitee)}"

#   class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'PeerInvite'
#     verbose_name_plural = 'PeerInvites'

# @receiver(post_save, sender=PeerInvite)
# def post_save_peer_invite(sender, instance, created, *args, **kwargs):
#   _sender = instance.inviter
#   _receiver = instance.invitee
#   _status = instance.status
#   print(f'{_sender} sent an invitation to {_receiver}--{_status}')
#   if not created:
#     if _status=='Accepted':
#       _sender.associates.add(_receiver)
#       _receiver.associates.add(_sender)
#     elif _status=='Declined':
#       _sender.invites.remove(_receiver)
#       _receiver.invites.remove(_sender)

class Associate(models.Model):
  class STATUS(models.TextChoices):
    ONHOLD = 'Waiting', 
    ACCEPTED = 'Accepted',
    DECLINED = 'Declined',
    DISSOCIATED = 'Dissociated'
  sender = models.ForeignKey("Profile", verbose_name=_("sender"), related_name="sender", on_delete=models.CASCADE)
  receiver = models.ForeignKey("Profile", verbose_name=_("receiver"), related_name="receiver", on_delete=models.CASCADE)
  is_active = models.BooleanField(_("invitation active"), default=True)
  status = models.CharField(_("invite status"), max_length=50, choices=STATUS.choices, default=STATUS.ONHOLD)

  def __str__(self):
    return f"{str(self.sender)} -- {str(self.receiver)}"

  class Meta:
    unique_together = ['sender', 'receiver']
    db_table = ''
    managed = True
    verbose_name = 'Associate'
    verbose_name_plural = 'Associates'

  def get_sent_invites(self, user):
    return self.objects.filter(sender=user)

  def get_received_invites(self, user):
    return self.objects.filter(receiver=user)

  def get_invite_status(self, pk):
    return self.objects.status(pk=pk)
    

@receiver(pre_save, sender=Associate)
def pre_save_associate(sender, instance, *args, **kwargs):
  _sender = instance.sender
  _receiver = instance.receiver
  _status = instance.status
  if _status=='Accepted' or  _status=='Declined':
    instance.is_active = False #sender & receiver can't send another invite
    print(f'Invitation inactive')
  else:
    instance.is_active = True
    print(f'Invitation active') 


@receiver(post_save, sender=Associate)
def post_save_associate(sender, instance, created, *args, **kwargs):
  _sender = instance.sender
  _receiver = instance.receiver
  _status = instance.status
  if not created:
    print(f'{_sender} sent an invitation to {_receiver}--{_status}')
    if _status=='Accepted':
      _sender.associates.add(_receiver)
      _receiver.associates.add(_sender)
      print(f'Status changed to -->{_status}')

    elif _status=='Declined':
      _sender.associates.remove(_receiver)
      _receiver.associates.remove(_sender)
      print(f'Invitation Declined')

    elif _status=='Dissociated':
      _sender.associates.remove(_receiver)
      _receiver.associates.remove(_sender)
      print(f'Status changed to -->{_status}')


@receiver(m2m_changed, sender=Profile.associates.through)
def user_associates_change(sender, instance, action, *args, **kwargs):
  if action == 'pre_add':
    qs = kwargs.get("model").objects.filter(pk__in=kwargs.get('pk_set'))
    print(qs.count())

    