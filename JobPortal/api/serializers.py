from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from UserProfiles.models import Profile,JobPost,JobApplication
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False,read_only=True)
    class Meta:
        model=Profile
        fields='__all__'
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobPost
        fields='__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobApplication
        fields='__all__'
