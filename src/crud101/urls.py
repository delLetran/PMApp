
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    # path('api/', include('api.urls')),
    path('', include('project_management.urls')),
    path('', include('user.urls')),
    path('login/', TemplateView.as_view(template_name="components/google_login.html")),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
]
