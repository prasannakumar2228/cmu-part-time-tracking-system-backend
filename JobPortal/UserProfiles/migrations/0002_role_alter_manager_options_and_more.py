# Generated by Django 4.2.6 on 2023-10-05 23:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('Department_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Department_Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name_plural': 'Managers'},
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='Department_id',
            new_name='Department',
        ),
        migrations.AddField(
            model_name='manager',
            name='Role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserProfiles.role'),
        ),
        migrations.AddField(
            model_name='student',
            name='Role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserProfiles.role'),
        ),
    ]
