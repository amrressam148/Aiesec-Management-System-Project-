# Generated by Django 2.0.3 on 2022-12-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20180403_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(default='Members', max_length=20),
            preserve_default=False,
        ),
    ]