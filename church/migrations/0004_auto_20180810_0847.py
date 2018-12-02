# Generated by Django 2.1 on 2018-08-10 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_auto_20180810_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='service',
        ),
        migrations.AlterField(
            model_name='attendancelist',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='church.signUp'),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]