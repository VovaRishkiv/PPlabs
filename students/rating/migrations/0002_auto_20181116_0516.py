# Generated by Django 2.1.2 on 2018-11-16 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBasic',
            new_name='Rating',
        ),
        migrations.AlterModelTable(
            name='rating',
            table='rating',
        ),
    ]