# Generated by Django 4.0.4 on 2022-06-23 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_contactme2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactme2',
        ),
        migrations.AddField(
            model_name='detail',
            name='Donatebox',
            field=models.CharField(default='', max_length=50),
        ),
    ]
