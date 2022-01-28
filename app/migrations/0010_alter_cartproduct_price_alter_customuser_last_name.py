# Generated by Django 4.0.1 on 2022-01-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_customuser_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='price',
            field=models.PositiveIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.EmailField(max_length=100),
        ),
    ]
