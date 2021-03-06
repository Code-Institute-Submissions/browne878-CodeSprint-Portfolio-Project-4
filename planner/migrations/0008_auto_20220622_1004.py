# Generated by Django 3.2 on 2022-06-22 10:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_auto_20220621_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emplyee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('client', 'CLIENT'), ('developer', 'DEVELOPER'), ('admin', 'ADMIN')], default='client', max_length=9)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='planner.company')),
            ],
        ),
        migrations.DeleteModel(
            name='Emplyee',
        ),
    ]
