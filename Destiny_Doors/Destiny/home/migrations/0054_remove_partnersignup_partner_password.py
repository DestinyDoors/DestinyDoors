# Generated by Django 4.0.4 on 2022-07-06 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_partnersignup_delete_partnersignupform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnersignup',
            name='Partner_password',
        ),
    ]
