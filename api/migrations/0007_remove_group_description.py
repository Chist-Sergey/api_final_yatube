# Generated by Django 3.1.7 on 2021-03-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210316_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
    ]
