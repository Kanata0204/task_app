# Generated by Django 2.2.2 on 2020-10-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='posted_date',
        ),
        migrations.AddField(
            model_name='task',
            name='time_limit',
            field=models.DateTimeField(null=True),
        ),
    ]
