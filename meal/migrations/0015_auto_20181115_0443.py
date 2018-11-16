# Generated by Django 2.1.3 on 2018-11-15 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0014_check_meals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mealsid',
        ),
        migrations.AddField(
            model_name='order',
            name='mealsid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meal.Meal'),
        ),
    ]
