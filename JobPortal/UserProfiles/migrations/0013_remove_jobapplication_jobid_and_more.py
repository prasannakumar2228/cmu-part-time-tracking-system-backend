# Generated by Django 4.2.6 on 2023-11-04 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0012_remove_profile_role_profile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='jobID',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='userManagerID',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserProfiles.jobpost'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='userManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserProfiles.profile'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='userApplication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserProfiles.profile'),
        ),
    ]
