# Generated by Django 4.0.3 on 2022-04-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
