from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User



class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    DOB=models.DateField(null=True)
    Gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    active = models.BooleanField(default=True)
    City=models.CharField(max_length=1000,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    Zipcode=models.CharField(max_length=100,null=True,blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
    Role=models.CharField(max_length=10, choices=ROLE_CHOICES,null=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural="Profiles"
        ordering = ['user']
    def __str__(self):
        return f"{self.user.username}"



class JobPost(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('filled', 'Filled'),
    )

    ACADEMIC_STATUS_CHOICES = (
        ('freshman', 'Freshman'),
        ('sophomore', 'Sophomore'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('graduate', 'Graduate'),
    )

    id = models.AutoField(primary_key=True)
    Manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)  
    Title = models.CharField(max_length=100)
    Description = models.TextField(null=False)
    DateOfPosting = models.DateTimeField(auto_now_add=True)
    Deadline = models.DateTimeField(null=False)
    NumberOfOpenings = models.IntegerField(default=0,null=False)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    Requirement = models.TextField(null=False)
    HourlyWage = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    WorkHours = models.PositiveSmallIntegerField()
    Skills = models.TextField(null=False)
    Experience = models.TextField()
    Active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.Title



class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('waitlist', 'Waitlist')
    )
    ACADEMIC_STATUS_CHOICES = (
        ('freshman', 'Freshman'),
        ('sophomore', 'Sophomore'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('graduate', 'Graduate'),
    )
    id = models.AutoField(primary_key=True)
    jobPost= models.ForeignKey(JobPost,blank=True,null=True,on_delete=models.CASCADE)  # You might want to link this to the JobPostCreation model
    Student = models.ForeignKey(Profile,blank=True,null=True,on_delete=models.CASCADE)  # You might want to link this to the User model
    ApplicationStatus = models.CharField(max_length=20,null=True, choices=STATUS_CHOICES, default='applied')
    AcademicStatus = models.CharField(max_length=20,null=True, choices=ACADEMIC_STATUS_CHOICES)
    Skills = models.TextField(null=False)
    Experience = models.TextField()
    DesiredWorkHours = models.PositiveSmallIntegerField()
    WorkStudyEligibility = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"Application for {self.jobPost} by {self.Student.First_Name} {self.Student.Last_Name}"



class Notification(models.Model):
    APPLICANT_STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    id = models.AutoField(primary_key=True)
    jobID = models.IntegerField()  # You might want to link this to the JobPostCreation model
    ApplicationID = models.IntegerField(null=True)  # You might want to link this to the JobApplication model
    ApplicantStatus = models.CharField(max_length=20, choices=APPLICANT_STATUS_CHOICES)
    Description = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"Notification {self.id}"











