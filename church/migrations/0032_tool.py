# Generated by Django 2.1 on 2018-08-22 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0031_auto_20180820_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool', models.FileField(blank=True, upload_to='groups')),
                ('link', models.URLField(blank=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Grouped')),
            ],
        ),
    ]
