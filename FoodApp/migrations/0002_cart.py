# Generated by Django 2.2 on 2019-05-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
            ],
        ),
    ]