# Generated by Django 3.2.7 on 2022-04-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]