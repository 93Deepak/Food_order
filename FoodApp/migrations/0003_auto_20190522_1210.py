# Generated by Django 2.2 on 2019-05-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pic',
            field=models.FileField(default=-1.0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]