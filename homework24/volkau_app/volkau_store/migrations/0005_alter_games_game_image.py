# Generated by Django 4.1.5 on 2023-01-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volkau_store', '0004_alter_games_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='game_image',
            field=models.ImageField(upload_to='media', verbose_name='Game Image'),
        ),
    ]
