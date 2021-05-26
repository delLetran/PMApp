from django.urls import path
from .views import (
  project_api,
  authenticate_api,
  project_list_view,
  project_create_view,
  project_detail,
)


urlpatterns = [
    path('api/project/', project_api, name="project_api"),
    path('api/authenticate/', authenticate_api, name="authenticate-api"),
    path('project/', project_list_view, name="project_list"),
    path('project/<int:id>/', project_detail, name="project_detail"),
    path('project/new/', project_create_view, name="project_create"),
]
