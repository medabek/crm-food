# Generated by Django 2.1.3 on 2018-11-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0019_auto_20181115_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='meals',
            field=models.ManyToManyField(default=0, to='meal.Meal'),
        ),
    ]
