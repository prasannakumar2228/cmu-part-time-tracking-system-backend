# Generated by Django 4.2.6 on 2023-11-05 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0026_alter_jobpost_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='User',
            new_name='student',
        ),
    ]
