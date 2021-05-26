from django.db import models
from django.utils.translation import ugettext_lazy as _


# class Requirement(models.Model):
#   start_date = models.DateField(_("project start date"), auto_now=False, auto_now_add=False)
#   end_date = models.DateField(_("project end date"), auto_now=False, auto_now_add=False, blank=True, null=True)
#   people = models.PositiveIntegerField(_("number of people"), default=5)
#   funds = models.PositiveIntegerField(_("project funds"), default=100000, blank=True, null=True)
#   others = models.TextField(_("addtional requirements"),max_length=255, blank=True, null=True)

#   # def __str__(self):
#   #     return self.name
  
#   class Meta:
#     db_table = 'db_proj_req'
#     managed = True
#     verbose_name = 'Requirement'
#     verbose_name_plural = 'Requirements'



# class Schedule(models.Model):
#   name = models.CharField(max_length=50)
#   activities = models.ForeignKey("Activity", on_delete=models.CASCADE, blank=True, null=True)
#   # deliverables = 

#   def __str__(self):
#     return self.name

#   class Meta:
#     db_table = 'db_proj_sched'
#     managed = True
#     verbose_name = 'Schedule'
#     verbose_name_plural = 'Schedules'


class Activity(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  initial = models.OneToOneField("Task", related_name="initial_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 1}, default=1) 
  planning = models.OneToOneField("Task", related_name="planning_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 2}, default=1) 
  execution = models.OneToOneField("Task", related_name="execution_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 3}, default=1) 
  control = models.OneToOneField("Task", related_name="control_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 4}, default=1) 
  closing = models.OneToOneField("Task", related_name="closing_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 5}, default=1) 
  others = models.OneToOneField("Task", related_name="others_phase", on_delete=models.CASCADE, limit_choices_to={'phase': 6}, default=1) 
  # initial_phase = models.ForeignKey("FirstPhase", on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
      verbose_name = _("Activity")
      verbose_name_plural = _("Activities")

class Task(models.Model):
  class PHASE(models.IntegerChoices):
    PHASE1 = 1, _("Initial"),
    PHASE2 = 2, _("Planning"),
    PHASE3 = 3, _("Execution"),
    PHASE4 = 4, _("Control and Monitoring"),
    PHASE5 = 5, _("Closing"),
    PHASE6 = 6, _("Others")

  name = models.CharField(_("task"), max_length=60)
  desc = models.TextField(_("task description"), max_length=255, blank=True, null=True)
  phase = models.PositiveSmallIntegerField(_("project phase"), choices=PHASE.choices, default=1)
  created_date = models.DateTimeField(auto_now_add=True)
  modified_daste = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(_("task status"), default=False)


  def __str__(self):
    return self.name

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'