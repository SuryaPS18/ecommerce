# Generated by Django 4.1.6 on 2023-02-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_customercard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercard',
            name='cardexpiry',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customercard',
            name='cardnumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customercard',
            name='code',
            field=models.CharField(max_length=30),
        ),
    ]