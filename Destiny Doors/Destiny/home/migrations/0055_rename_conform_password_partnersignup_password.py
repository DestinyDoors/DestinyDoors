# Generated by Django 4.0.4 on 2022-07-06 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_remove_partnersignup_partner_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partnersignup',
            old_name='Conform_password',
            new_name='Password',
        ),
    ]