# Generated by Django 4.0.4 on 2022-07-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_alter_adoptform_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptform',
            name='Category',
            field=models.CharField(choices=[('Nri', 'nri'), ('Indian', 'indian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Document',
            field=models.CharField(choices=[('Passport', 'passport'), ('Aadhar', 'aadhar'), ('PAN', 'pan'), ('voter', 'voter')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Martital_Status',
            field=models.CharField(choices=[('Married', 'married'), ('Divorcee', 'divorcee'), ('Single', 'single'), ('Widow', 'widow')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Category',
            field=models.CharField(choices=[('Nri', 'nri'), ('Indian', 'indian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Document',
            field=models.CharField(choices=[('Passport', 'passport'), ('Aadhar', 'aadhar'), ('PAN', 'pan'), ('voter', 'voter')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10),
        ),
    ]