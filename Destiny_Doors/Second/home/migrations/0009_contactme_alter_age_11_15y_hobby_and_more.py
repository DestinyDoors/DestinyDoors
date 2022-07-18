# Generated by Django 4.0.4 on 2022-06-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_age_6_10_age_11_15y_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=150)),
                ('Last_name', models.CharField(max_length=150)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='age_11_15y',
            name='Hobby',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_11_15y',
            name='description',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='age_11_15y',
            name='taught',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_16_18y',
            name='Hobby',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_16_18y',
            name='description',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='age_16_18y',
            name='taught',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_3_5y',
            name='Hobby',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_3_5y',
            name='description',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='age_3_5y',
            name='taught',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_6_10y',
            name='Hobby',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='age_6_10y',
            name='description',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='age_6_10y',
            name='taught',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newboarn',
            name='Hobby',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newboarn',
            name='description',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='newboarn',
            name='taught',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
