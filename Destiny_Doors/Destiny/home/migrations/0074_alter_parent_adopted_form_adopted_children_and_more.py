# Generated by Django 4.0.4 on 2022-07-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_parent_adopted_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_adopted_form',
            name='Adopted_Children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='parent_adopted_form',
            name='Biological_Childrens',
            field=models.IntegerField(),
        ),
    ]