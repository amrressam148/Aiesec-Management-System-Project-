# Generated by Django 2.0.3 on 2022-12-31 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20230101_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name',), 'verbose_name_plural': 'Teams'},
        ),
    ]
