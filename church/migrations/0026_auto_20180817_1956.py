# Generated by Django 2.1 on 2018-08-17 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0025_auto_20180816_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancelist',
            name='event',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.RemoveField(
            model_name='chosengroup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RemoveField(
            model_name='image',
            name='group',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='query',
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
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='attendanceList',
        ),
        migrations.DeleteModel(
            name='chosenGroup',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Grouped',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Responses',
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