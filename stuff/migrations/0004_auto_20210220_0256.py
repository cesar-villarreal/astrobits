# Generated by Django 3.1.5 on 2021-02-20 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_circuits_constructorresults_constructors_constructorstandings_drivers_driverstandings_laptimes_pitst'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Circuits',
        ),
        migrations.DeleteModel(
            name='Constructorresults',
        ),
        migrations.DeleteModel(
            name='Constructors',
        ),
        migrations.DeleteModel(
            name='Constructorstandings',
        ),
        migrations.DeleteModel(
            name='Drivers',
        ),
        migrations.DeleteModel(
            name='Driverstandings',
        ),
        migrations.DeleteModel(
            name='Laptimes',
        ),
        migrations.DeleteModel(
            name='Pitstops',
        ),
        migrations.DeleteModel(
            name='Qualifying',
        ),
        migrations.DeleteModel(
            name='Races',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.DeleteModel(
            name='Seasons',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
