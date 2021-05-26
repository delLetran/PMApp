from rest_framework import serializers

from .models import Profile, Associate


class AssociateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Associate
    fields = '__all__'


class PeerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'job_title']


class ProfileSerializer(serializers.ModelSerializer):
  associates = PeerSerializer(read_only=True, many=True)

  class Meta:
    model = Profile
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'job_title', 'projects', 'joined_projects', 'associates']




