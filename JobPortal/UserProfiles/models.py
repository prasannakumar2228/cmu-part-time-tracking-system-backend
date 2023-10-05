from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Departments(models.Model):
    Department_id=models.UUIDField(default=uuid.uuid4,primary_key=True,blank=False,null=False,editable=False)
    Department_Name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Departments"
    def __str__(self):
        return self.Department_Name

class Role(models.Model):
    Department_id=models.UUIDField(default=uuid.uuid4,primary_key=True,blank=False,null=False,editable=False)
    Department_Name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Roles"
    def __str__(self):
        return self.Department_Name

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Zipcode=models.CharField(max_length=100,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    DOB=models.DateField(null=True)
    Role=models.ForeignKey('Role',blank=True,null=True,on_delete=models.SET_NULL)
    class Meta:
        verbose_name_plural='Students'
    def __str__(self):
        return f'{self.Last_Name}, {self.First_Name}'
    
class Manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Department=models.ForeignKey(Departments,on_delete=models.SET_NULL,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Zipcode=models.CharField(max_length=100,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    DOB=models.DateField(null=True)
    Role=models.ForeignKey('Role',blank=True,null=True,on_delete=models.SET_NULL)
    class Meta:
        verbose_name_plural='Managers'
    def __str__(self):
        return f'{self.Last_Name}, {self.First_Name}'
    

