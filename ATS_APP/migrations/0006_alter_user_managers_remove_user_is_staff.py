# Generated by Django 4.0 on 2022-06-22 09:05

import ATS_APP.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS_APP', '0005_user_is_active_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', ATS_APP.models.userManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
