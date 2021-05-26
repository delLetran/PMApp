from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Profile, Associate

admin.site.register(Associate)

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
  fieldsets = (
    (None, {'fields': ('username', 'email', 'password',)}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'birth_date')}),
    (_('Projects '), {'fields': ( 'projects', 'joined_projects')}),
    (_('Qualifications'), {'fields': ( 'job_title', 'about')}),
    (_('Associates'), {'fields': ( 'associates', )}),
    (_('Permissions'), {
      'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login', 'start_date')}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')}
    ),
  )

