# Generated by Django 4.0.1 on 2022-02-14 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_buyproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyproduct',
            name='user',
        ),
    ]