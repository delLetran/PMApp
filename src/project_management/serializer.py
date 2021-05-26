from .models import Project, ProjectGroup
# from project_components.models import Schedule, Activity, Task
from rest_framework import serializers

from django.contrib.auth.models import User

# from user.models import Profile

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'job_title']

class ProjectGroupSerializer(serializers.ModelSerializer):
  member = UserSerializer(read_only=True) 
  class Meta:
    model = ProjectGroup
    fields = "__all__"



# class TaskSerializer(serializers.ModelSerializer):

#   class Meta:
#     model = Task
#     fields = "__all__"

# class ActivitySerializer(serializers.ModelSerializer):
#   task = TaskSerializer(read_only=True) 

#   class Meta:
#     model = Activity
#     fields = "__all__"
    
# class ScheduleSerializer(serializers.ModelSerializer):
#   activity = ActivitySerializer(read_only=True) 

#   class Meta:
#     model = Schedule
#     fields = "__all__"




########################--- Project Serializer ---##########################################

class ProjectSerializer(serializers.ModelSerializer):
  group = ProjectGroupSerializer(read_only=True)
  # schedule = ScheduleSerializer(read_only=True)
   
  # project_member = serializers.StringRelatedField(read_only=True, many=True) 

  class Meta:
    model = Project
    fields = "__all__"
    # fields = ['id', 'name', 'description', 'status', 'team']

########################--- End of Project Serializer  ---##########################################
