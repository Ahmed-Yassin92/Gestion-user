# Generated by Django 4.0.4 on 2022-05-19 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_remove_users_date_users_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='noms',
            new_name='nom',
        ),
    ]
