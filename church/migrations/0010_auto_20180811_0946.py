# Generated by Django 2.1 on 2018-08-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0009_auto_20180811_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancelist',
            name='person',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='person_in_charge',
            field=models.CharField(max_length=30),
        ),
    ]
