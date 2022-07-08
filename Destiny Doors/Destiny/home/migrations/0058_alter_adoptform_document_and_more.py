# Generated by Django 4.0.4 on 2022-07-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_partner_delete_partnersignup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptform',
            name='Document',
            field=models.CharField(choices=[('PAN', 'pan'), ('voter', 'voter'), ('Aadhar', 'aadhar'), ('Passport', 'passport')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Martital_Status',
            field=models.CharField(choices=[('Single', 'single'), ('Widow', 'widow'), ('Divorcee', 'divorcee'), ('Married', 'married')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Document',
            field=models.CharField(choices=[('PAN', 'pan'), ('voter', 'voter'), ('Aadhar', 'aadhar'), ('Passport', 'passport')], max_length=10),
        ),
    ]
