# Generated by Django 2.2 on 2019-05-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0003_auto_20190522_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default=1.0, max_length=30),
            preserve_default=False,
        ),
    ]