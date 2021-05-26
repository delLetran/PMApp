from django.urls import path

from .views import (
  blog_list_api,
)

urlpatterns = [
    path('', blog_list_api , name='blog_list_api'),
]
