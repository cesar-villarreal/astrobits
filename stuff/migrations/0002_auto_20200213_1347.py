# Generated by Django 3.0.3 on 2020-02-13 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pictures',
            new_name='Picture',
        ),
    ]