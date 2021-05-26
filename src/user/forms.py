from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Profile, Associate


class SignUpForm(UserCreationForm):
  
    
  class Meta:
    model = Profile
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

  # def clean(self):
  #   cleaned_data = super().clean()
  #   username = self.cleaned_data.get("username")
  #   # username = username.lower()
    
  #   if Profile.objects.filter(username=username).exists():
  #     raise ValidationError(
  #       _(" %(value), username is already taken, try another one."),
  #       params={'value': username}
  #     )
  #     print('from forms: username is already taken, try another one.')


  def clean_username(self):
    username = self.cleaned_data["username"]
    username = username.lower()
    
    if Profile.objects.filter(username=username).exists():
      raise ValidationError(
        _(f" username '{username}' is already taken, try another one.")
      )
    return username

class AssociateForm(forms.ModelForm):

  class Meta:
    model = Associate
    fields = ['status']
    
