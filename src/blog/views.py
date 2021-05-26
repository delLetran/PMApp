from django.shortcuts import render


def blog_list_api(request, *args, **kwargs):
  template_name= "pages/index.html"
  context={'object_list': None}
  return render(request, template_name, context) 