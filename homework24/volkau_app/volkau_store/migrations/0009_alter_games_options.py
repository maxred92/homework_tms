# Generated by Django 4.1.5 on 2023-02-09 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volkau_store', '0008_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('name',), 'verbose_name': 'Game', 'verbose_name_plural': 'Games'},
        ),
    ]
