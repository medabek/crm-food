# Generated by Django 2.1.3 on 2018-11-16 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0030_auto_20181115_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={},
        ),
        migrations.AlterModelOptions(
            name='mealstoorder',
            options={},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='check',
            name='meals',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tablename',
        ),
    ]
