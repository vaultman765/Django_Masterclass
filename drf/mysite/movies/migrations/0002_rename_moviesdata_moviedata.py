# Generated by Django 3.2.4 on 2021-06-08 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moviesdata',
            new_name='Moviedata',
        ),
    ]