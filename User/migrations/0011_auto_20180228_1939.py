# Generated by Django 2.0 on 2018-02-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20180228_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='region',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=None, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
