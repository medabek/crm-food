# Generated by Django 2.1.3 on 2018-11-13 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('login', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=400)),
                ('dateofadd', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=150)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='user.Role')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]
