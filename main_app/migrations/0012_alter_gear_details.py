# Generated by Django 4.1.3 on 2022-11-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_gear_details_alter_bike_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='details',
            field=models.CharField(default='write details here', max_length=200),
        ),
    ]
