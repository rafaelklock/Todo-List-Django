# Generated by Django 2.2.7 on 2019-11-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0005_auto_20191113_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_name',
            field=models.CharField(help_text='s', max_length=100),
        ),
    ]
