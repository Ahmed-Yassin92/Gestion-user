# Generated by Django 4.0.4 on 2022-04-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
    ]
