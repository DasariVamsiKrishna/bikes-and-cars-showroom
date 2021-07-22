# Generated by Django 3.0 on 2021-07-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0005_auto_20210718_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnames', models.CharField(max_length=30)),
                ('carmodels', models.IntegerField()),
                ('carcolours', models.CharField(max_length=30)),
                ('carprice', models.IntegerField()),
                ('deliveryaddress', models.CharField(max_length=100)),
            ],
        ),
    ]
