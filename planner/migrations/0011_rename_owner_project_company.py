# Generated by Django 3.2 on 2022-06-22 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0010_rename_userprofile_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='company',
        ),
    ]
