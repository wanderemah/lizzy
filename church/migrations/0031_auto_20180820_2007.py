# Generated by Django 2.1 on 2018-08-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0030_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
