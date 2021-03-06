# Generated by Django 3.0.5 on 2021-02-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_total', models.FloatField(null=True)),
                ('master_quantity', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='master_quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='master_total',
        ),
    ]
