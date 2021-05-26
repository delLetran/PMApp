from django.test import TestCase
from .models import Profile

class ProfileModel(TestCase):

  def test_string_representation(self):
    user = Profile(
      email='user101.gov.edu', 
      username='user101',
      password1='handsome365',
      password2='handsome365', 
    )
    user2 = Profile(
      email='user101.gov.edu', 
      username='user101',
      password1='handsome365',
      password2='handsome365', 
    )
    self.assertTrue() 
    