# Generated by Django 2.1 on 2018-08-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0010_auto_20180811_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chosengroup',
            name='group',
            field=models.CharField(max_length=30),
        ),
    ]
