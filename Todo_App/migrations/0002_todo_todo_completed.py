# Generated by Django 3.1.3 on 2021-02-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_completed',
            field=models.BooleanField(default=False),
        ),
    ]
