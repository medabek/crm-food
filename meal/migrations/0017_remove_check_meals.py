# Generated by Django 2.1.3 on 2018-11-15 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0016_auto_20181115_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='meals',
        ),
    ]
