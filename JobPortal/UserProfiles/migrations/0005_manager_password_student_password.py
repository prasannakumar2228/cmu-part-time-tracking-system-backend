# Generated by Django 4.2.6 on 2023-10-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0004_alter_job_options_alter_jobapplication_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='Password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
