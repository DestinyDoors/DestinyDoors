# Generated by Django 4.0.4 on 2022-07-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_adoptform_delete_partnerdnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
                ('Email', models.EmailField(max_length=80)),
                ('Phone', models.IntegerField()),
                ('Password', models.CharField(max_length=80)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='partnersignup',
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Document',
            field=models.CharField(choices=[('Passport', 'passport'), ('voter', 'voter'), ('Aadhar', 'aadhar'), ('PAN', 'pan')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Martital_Status',
            field=models.CharField(choices=[('Married', 'married'), ('Single', 'single'), ('Widow', 'widow'), ('Divorcee', 'divorcee')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptform',
            name='Spouse_Document',
            field=models.CharField(choices=[('Passport', 'passport'), ('voter', 'voter'), ('Aadhar', 'aadhar'), ('PAN', 'pan')], max_length=10),
        ),
    ]
