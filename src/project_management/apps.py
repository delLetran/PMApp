from django.apps import AppConfig
# from . import signals as signals

class ProjectManagementConfig(AppConfig):
  name = 'project_management'
  
  def ready(self):
    import project_management.signals