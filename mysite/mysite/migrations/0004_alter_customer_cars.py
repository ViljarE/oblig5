# Generated by Django 4.0.1 on 2022-11-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_customer_cars_alter_car_year_alter_customer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cars',
            field=models.IntegerField(),
        ),
    ]
