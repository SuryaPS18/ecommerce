# Generated by Django 4.1.6 on 2023-02-10 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_shpregmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shpregmodel',
            old_name='Password',
            new_name='password',
        ),
    ]
