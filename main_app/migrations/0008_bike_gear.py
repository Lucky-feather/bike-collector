# Generated by Django 4.1.3 on 2022-11-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_bike_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='gear',
            field=models.ManyToManyField(to='main_app.gear'),
        ),
    ]
