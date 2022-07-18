# Generated by Django 4.0.4 on 2022-07-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_alter_adoptform_category_alter_adoptform_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptform',
            name='Document',
            field=models.CharField(choices=[('PAN', 'pan'), ('Aadhar', 'aadhar'), ('Passport', 'passport'), ('voter', 'voter')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Martital_Status',
            field=models.CharField(choices=[('Single', 'single'), ('Widow', 'widow'), ('Divorcee', 'divorcee'), ('Married', 'married')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Document',
            field=models.CharField(choices=[('PAN', 'pan'), ('Aadhar', 'aadhar'), ('Passport', 'passport'), ('voter', 'voter')], max_length=10),
        ),
    ]
