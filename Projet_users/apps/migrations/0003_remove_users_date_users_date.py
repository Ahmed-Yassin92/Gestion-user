# Generated by Django 4.0.4 on 2022-05-18 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_users_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date',
        ),
        migrations.AddField(
            model_name='users',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]