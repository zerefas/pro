# Generated by Django 4.0.3 on 2022-04-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
