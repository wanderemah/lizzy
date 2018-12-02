# Generated by Django 2.1 on 2018-08-20 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0029_eventimage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=30)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Grouped')),
            ],
        ),
    ]
