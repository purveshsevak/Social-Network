# Generated by Django 2.0 on 2018-09-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180918_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
    ]
