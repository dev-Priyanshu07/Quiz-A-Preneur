# Generated by Django 4.0.6 on 2022-12-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0003_rename_place_of_residence_registration_detail_city_of_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=255),
        ),
    ]
