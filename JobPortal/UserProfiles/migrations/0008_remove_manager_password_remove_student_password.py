# Generated by Django 4.2.6 on 2023-10-17 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0007_alter_departments_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Password',
        ),
    ]
