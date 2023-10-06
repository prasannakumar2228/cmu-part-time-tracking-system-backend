from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from UserProfiles.models import Student,Manager,Role
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['Name']
class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    Role=RoleSerializer()
    class Meta:
        model=Student
        fields="__all__"
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        role_data = validated_data.pop('Role')
        user_instance, created = User.objects.update_or_create(
            username=user_data['username'],
            defaults=user_data
        )
        role_instance, created = Role.objects.update_or_create(
            Name=role_data['Name'],
            defaults=role_data
        )
        student_instance = Student.objects.create(user=user_instance, Role=role_instance, **validated_data)
        return student_instance
    # def create(self, validated_data):
    #     # Hash the password before saving
    #     validated_data['Password'] = make_password(validated_data['Password'])
    #     user = Student.objects.create(**validated_data)
    #     return user

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="__all__"
    def create(self, validated_data):
        # Hash the password before saving
        validated_data['Password'] = make_password(validated_data['Password'])
        user = Student.objects.create(**validated_data)
        return user