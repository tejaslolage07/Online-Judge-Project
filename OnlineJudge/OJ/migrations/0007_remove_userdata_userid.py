# Generated by Django 4.0.5 on 2022-08-17 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0006_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='userID',
        ),
    ]
