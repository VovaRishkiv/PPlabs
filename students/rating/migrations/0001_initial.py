# Generated by Django 2.1.2 on 2018-11-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'UserBasic',
            },
        ),
    ]