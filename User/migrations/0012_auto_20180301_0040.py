# Generated by Django 2.0 on 2018-03-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20180228_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, unique=True),
        ),
    ]
