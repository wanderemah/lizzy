# Generated by Django 2.1 on 2018-08-11 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('query', models.TextField(max_length=255, primary_key=True, serialize=False)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='church.signUp')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='church.signUp')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Comment')),
            ],
        ),
    ]
