# Generated by Django 4.0.5 on 2022-08-17 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0007_remove_userdata_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubmission',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='usersubmission',
            name='verdict',
        ),
    ]