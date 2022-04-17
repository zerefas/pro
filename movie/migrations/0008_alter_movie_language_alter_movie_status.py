# Generated by Django 4.0.3 on 2022-04-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('eng', 'ENGLISH'), ('deu', 'Deutsch')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('recently', 'RECENTLY WATCH'), ('most', 'MOST WATCHED'), ('top', 'TOP RATED')], max_length=10),
        ),
    ]