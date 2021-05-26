from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

MAX_LENGTH_NAME = 120
MAX_LENGTH_USERNAME = 50
MAX_LENGTH_JOB = 120
MAX_LENGTH_DESC = 255
# USER = settings.AUTH_USER_MODEL
USER = User

class Project(models.Model):
  name = models.TextField(max_length=MAX_LENGTH_NAME)
  description = models.TextField(max_length=MAX_LENGTH_DESC, blank=True, null=True)
  lead = models.ForeignKey("Staff", related_name='stafflead', default=1, on_delete=models.CASCADE)
  member = models.ManyToManyField("Staff", related_name='staffmember', blank=True, null=True)
  
  class Meta:
    ordering = ['-pk']
    # unique_together = ['lead', 'member']

  # def __str__(self):
  #     return self.name

  # def get_absolute_url(self):
  #     return reverse("Project_detail", kwargs={"pk": self.pk})


class ProjectLead(models.Model):
  '''
  '''
  bio = models.OneToOneField("Staff", default=1, on_delete=models.CASCADE, blank=True, null=True)
  project = models.ManyToManyField("Project", blank=True, null=True)
 
  class Meta:
    ordering = ['pk']

  # def __str__(self):
  #     return str(self.bio.job_title)


class ProjectMember(models.Model):
  '''
  '''
  bio = models.OneToOneField("Staff", default=2, on_delete=models.CASCADE, blank=True, null=True)
  project = models.ManyToManyField("Project", blank=True, null=True)

  class Meta:
    ordering = ['pk']

  # def __str__(self):
  #     return str(self.bio.job_title)


class Staff(models.Model):
  '''
  '''
  profile = models.OneToOneField(USER, on_delete=models.CASCADE, unique=True, blank=True, null=True)
  # username = models.SlugField(max_length=MAX_LENGTH_USERNAME, unique=True, blank=False, null=False)  
  # first_name = models.TextField(max_length=MAX_LENGTH_JOB, blank=True, null=True)
  # last_name = models.TextField(max_length=MAX_LENGTH_JOB, blank=True, null=True)
  job_title = models.TextField(max_length=MAX_LENGTH_JOB)
  job_description = models.TextField(max_length=MAX_LENGTH_DESC, blank=True, null=True)

  class Meta:
    ordering = ['pk']

  # def __str__(self):
    # if (self.profile.first_name != None and self.profile.last_name != None ):
    #   return f'{self.profile.first_name} {self.profile.last_name}'
    # return self.profile