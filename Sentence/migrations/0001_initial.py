# Generated by Django 2.0 on 2018-03-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=512)),
                ('author', models.CharField(max_length=32)),
                ('reference', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='sentence',
            name='tags',
            field=models.ManyToManyField(to='Sentence.Tag'),
        ),
    ]
