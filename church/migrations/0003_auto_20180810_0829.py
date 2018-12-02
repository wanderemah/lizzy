# Generated by Django 2.1 on 2018-08-10 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0002_auto_20180810_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendanceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='chosenGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='serviceTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.URLField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Service')),
            ],
        ),
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('full_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('profile', models.TextField()),
                ('tel_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='church.signUp')),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Group')),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='person_in_charge',
            field=models.OneToOneField(on_delete=None, to='church.signUp'),
        ),
        migrations.AddField(
            model_name='chosengroup',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='church.Group'),
        ),
        migrations.AddField(
            model_name='chosengroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.signUp'),
        ),
        migrations.AddField(
            model_name='attendancelist',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Event'),
        ),
        migrations.AddField(
            model_name='attendancelist',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='church.Contact'),
        ),
    ]
