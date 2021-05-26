from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import logout

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectGroup
from .serializer import ProjectSerializer
from .forms import ProjectForm



# @authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def authenticate_api(request, *args, **kwargs):
  content = {
      'user': str(request.user),  # `django.contrib.auth.User` instance.
      'auth': str(request.auth),  # None
  }
  print(content)
  return Response({'details': f'{request.user} is logged in'})



@api_view(['GET'])
def project_api(request, *args, **kwargs):
  queryset = get_list_or_404(Project)
  serializer = ProjectSerializer(queryset, many=True) 

  return Response(serializer.data)


def project_list_view(request, *args, **kwargs):
  user = request.user
  if request.method == 'GET':
    project_list = get_list_or_404(Project, admin=user)
  context = {
    'object_list': project_list,
  }
  return render(request, 'project_management/project-list.html', context)


def project_detail(request, id, *args, **kwargs):
  user = request.user
  if request.method == 'GET':
    project = get_object_or_404(Project, id=id)
    members = get_list_or_404(ProjectGroup)
  context = {
    'project': project,
    'group': members
  }
  return render(request, 'project_management/project-detail.html', context)


def project_create_view(request, *args, **kwargs):
  user = request.user
  form = ProjectForm()
  if user.is_authenticated:
    if request.method == 'POST':
      form = ProjectForm(request.POST)
      instance = form.save(commit=False)
      instance.admin = user
      form.save()
      message = 'Project successfuly created!'
    else: 
      message = 'Create a New Project'
  else:
    message = 'Login to add a new project'
  context = {
    'form': form,
    'message': message
  }
  return render(request, 'project_management/project.html', context)