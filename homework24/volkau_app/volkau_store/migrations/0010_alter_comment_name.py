# Generated by Django 4.1.5 on 2023-02-14 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volkau_store', '0009_alter_games_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
