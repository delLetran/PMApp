from django.db import models

MAX_LENGTH_NAME = 120

class Project(models.Model):
  name = models.TextField(max_length=MAX_LENGTH_NAME)
  

  class Meta:
    ordering = ['-pk']
    verbose_name = _("Project")
    verbose_name_plural = _("Projects")

  def __str__(self):
      return self.name

  # def get_absolute_url(self):
  #     return reverse("Project_detail", kwargs={"pk": self.pk})


class ProjectLead(models.Model):
  '''
  name textfield will be change to User
  '''
  name = models.TextField(max_length=MAX_LENGTH_NAME) 
    
  class Meta:
      verbose_name = _("ProjectLead")
      verbose_name_plural = _("ProjectLeads")

  def __str__(self):
      return self.name

  # def get_absolute_url(self):
  #     return reverse("ProjectLead_detail", kwargs={"pk": self.pk})


class ProjectMember(models.Model):
  '''
  name textfield will be change to User
  '''
  name = models.TextField(max_length=MAX_LENGTH_NAME) 
    

  class Meta:
      verbose_name = _("ProjectMember")
      verbose_name_plural = _("ProjectMembers")

  def __str__(self):
      return self.name

  # def get_absolute_url(self):
  #     return reverse("ProjectMember_detail", kwargs={"pk": self.pk})
