# Generated by Django 2.0.3 on 2022-12-31 22:14

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('projects', '0003_auto_20180403_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='company',
            new_name='team',
        ),
    ]
