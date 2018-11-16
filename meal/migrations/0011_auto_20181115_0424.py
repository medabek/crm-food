# Generated by Django 2.1.3 on 2018-11-15 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0010_auto_20181115_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealstoorder',
            name='meals',
        ),
        migrations.AddField(
            model_name='mealstoorder',
            name='meals',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mealstoorders', to='meal.Meal'),
        ),
    ]
