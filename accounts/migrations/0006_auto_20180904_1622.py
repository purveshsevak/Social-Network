# Generated by Django 2.0 on 2018-09-04 10:52

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('mumbai', django.db.models.manager.Manager()),
            ],
        ),
    ]