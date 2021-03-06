# Generated by Django 4.0.4 on 2022-07-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_alter_adoptform_category_alter_adoptform_document_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='givemoney',
        ),
        migrations.DeleteModel(
            name='partnerreg',
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Category',
            field=models.CharField(choices=[('Nri', 'nri'), ('Indian', 'indian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Document',
            field=models.CharField(choices=[('voter', 'voter'), ('PAN', 'pan'), ('Passport', 'passport'), ('Aadhar', 'aadhar')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Martital_Status',
            field=models.CharField(choices=[('Single', 'single'), ('Widow', 'widow'), ('Divorcee', 'divorcee'), ('Married', 'married')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Category',
            field=models.CharField(choices=[('Nri', 'nri'), ('Indian', 'indian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Document',
            field=models.CharField(choices=[('voter', 'voter'), ('PAN', 'pan'), ('Passport', 'passport'), ('Aadhar', 'aadhar')], max_length=10),
        ),
    ]
