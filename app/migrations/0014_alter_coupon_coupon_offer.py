# Generated by Django 4.0.1 on 2022-02-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_coupon_coupon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_offer',
            field=models.IntegerField(default=0),
        ),
    ]