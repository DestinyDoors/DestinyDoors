# Generated by Django 4.0.4 on 2022-06-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_gateway_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='moneyc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Amount', models.CharField(max_length=50)),
            ],
        ),
    ]
