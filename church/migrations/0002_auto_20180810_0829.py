# Generated by Django 2.1 on 2018-08-10 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancelist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='chosengroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='chosengroup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='service',
        ),
        migrations.RemoveField(
            model_name='event',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='servicetool',
            name='service',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.DeleteModel(
            name='attendanceList',
        ),
        migrations.DeleteModel(
            name='chosenGroup',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='serviceTool',
        ),
        migrations.DeleteModel(
            name='signUp',
        ),
    ]
