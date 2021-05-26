from django.db import models
from django.utils.translation import ugettext_lazy as _


# from django.contrib.postgres.fields import ArrayField
# from user.models import Profile
MAX_LENGTH_NAME = 120
MAX_LENGTH_USERNAME = 50
MAX_LENGTH_JOB = 120
MAX_LENGTH_DESC = 255
MAX_LENGTH_TEXT = 255

USER = 'user.Profile'
# REQUIREMENT = 'project_components.Requirement'
# SCHEDULE = 'project_components.Schedule'

class ProjectManager(models.Manager):
  def create_project(self, user,  name, desc):
    project = self.create(name=self.name, desc=self.desc, admin=self.user)
    return project

class Project(models.Model):
  class TYPE(models.IntegerChoices):
    SOFTDEV = 2, _('Software Development'),
    EQUIP = 3, _('Equipment / System Installation')

  class STATUS(models.IntegerChoices):
    OG = 1, _('Ongoing Project'),
    OH = 2, _('Project On-hold'),
    CP = 3, _('Project Completed'),
    PD = 4, _('Project Delivered')

  name = models.CharField(max_length=MAX_LENGTH_NAME)
  description = models.TextField(max_length=MAX_LENGTH_DESC, blank=True, null=True)
  admin = models.ForeignKey(USER, related_name='admin', blank=True, on_delete=models.CASCADE)
  group = models.ManyToManyField("ProjectGroup", related_name='project_group',  default=[0], blank=True, null=True)
  status =  models.PositiveSmallIntegerField(_("project status"), default=STATUS.OG, choices=STATUS.choices)
  project_type =  models.PositiveSmallIntegerField(_("project type"), default=TYPE.SOFTDEV, choices=TYPE.choices)
  # requirments = models.OneToOneField(REQUIREMENT, on_delete=models.CASCADE, blank=True, null=True)
  # schedlule = models.ForeignKey(SCHEDULE, on_delete=models.CASCADE, blank=True, null=True)
  # requirment = models.ManyToManyField(REQUIREMENT, blank=True, default=[0])
  # progress = models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
  objects = ProjectManager()
  class Meta:
    ordering = ['-pk']

  def __str__(self):
      return self.name

class ProjectGroup(models.Model): 
  class POSITION(models.IntegerChoices):
    PM = 1, _('Project Manager'),
    ADM = 2, _('Project Admin'),
    PL = 3, _('Project Leader'),
    MEM = 4, _('Member')

  
  member = models.ForeignKey(USER, related_name='member', on_delete=models.CASCADE)
  position = models.PositiveSmallIntegerField(choices=POSITION.choices, default=POSITION.MEM)
  permission_1 = models.BooleanField(_("permission level 1"), default=False)
  permission_2 = models.BooleanField(_("permission level 2"), default=False)
  permission_3 = models.BooleanField(_("permission level 3"), default=True)

  class Meta:
      verbose_name = _("ProjectGroup")
      verbose_name_plural = _("ProjectGroups")

  def __str__(self):
      return str(self.member)





# class UserQuerySet(models.QuerySet):
#   def published(self):
#     return self.filter(publish__lte=timezone.now())

#   def is_manager(self):
#     return self.filter(position='project manager')

# class TeamManager(models.Manager):
#   def get_queryset(self):
#     return ArticleQuerySet(self.model, using=self._db)

#   def published(self):
#     return self.get_queryset().published()

#   def featured(self):
#     return self.get_queryset().featured()









# class RiskManagement(models.Model):
#   risk = models.OneToOneField("Risk", on_delete=models.CASCADE)
#   mitigation = models.ManyToManyField("Mitigation")

#   def __str__(self):
#     pass

#   class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'RiskAndMitigation'
#     verbose_name_plural = 'RiskAndMitigations'

# class Mitigation(models.Model):
#   # action = 
#   def __str__(self):
#     pass

#   class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'Mitigation'
#     verbose_name_plural = 'Mitigations'

# class Risk(models.Model):
#   # hazard = 

#   def __str__(self):
#     pass

#   class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'Risk'
#     verbose_name_plural = 'Risks'