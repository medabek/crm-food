# Generated by Django 2.1.3 on 2018-11-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0007_remove_order_tablename'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tablename',
            field=models.CharField(default='table1', max_length=250),
        ),
    ]
