# Generated by Django 3.2.4 on 2021-07-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210707_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='email',
            field=models.CharField(max_length=30, verbose_name='Email'),
        ),
    ]
