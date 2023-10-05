from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Manager)
admin.site.register(Departments)
admin.site.register(Role)
admin.site.register(Job)
admin.site.register(JobApplication)