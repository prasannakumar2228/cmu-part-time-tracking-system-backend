# Generated by Django 4.2.6 on 2023-11-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0014_remove_jobapplication_availability_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='academicStatus',
            new_name='AcademicStatus',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='applicationStatus',
            new_name='ApplicationStatus',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='desiredWorkHours',
            new_name='DesiredWorkHours',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='experience',
            new_name='Experience',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='skills',
            new_name='Skills',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='userApplication',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='workStudyEligibility',
            new_name='WorkStudyEligibility',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='active',
            new_name='Active',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='dateOfPosting',
            new_name='DateOfPosting',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='deadline',
            new_name='Deadline',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='experience',
            new_name='Experience',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='hourlyWage',
            new_name='HourlyWage',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='userManager',
            new_name='Manager',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='numberOfApplications',
            new_name='NumberOfOpenings',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='requirement',
            new_name='Requirement',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='skills',
            new_name='Skills',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='jobTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='workHours',
            new_name='WorkHours',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='applicantStatus',
            new_name='ApplicantStatus',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='timestamp',
            new_name='Timestamp',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='role_status',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='academicStatus',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='applicationID',
        ),
        migrations.AddField(
            model_name='notification',
            name='ApplicationID',
            field=models.IntegerField(null=True),
        ),
    ]
