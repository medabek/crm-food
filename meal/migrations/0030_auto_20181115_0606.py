# Generated by Django 2.1.3 on 2018-11-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0029_auto_20181115_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mealsid',
            field=models.ManyToManyField(related_name='orders', through='meal.MealsToOrder', to='meal.Meal'),
        ),
    ]
