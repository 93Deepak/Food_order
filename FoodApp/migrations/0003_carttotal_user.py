# Generated by Django 3.0.5 on 2021-02-16 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_auto_20210217_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttotal',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
