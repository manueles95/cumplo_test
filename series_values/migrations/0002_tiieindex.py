# Generated by Django 3.0.1 on 2019-12-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series_values', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiieIndex',
            fields=[
                ('tiie_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('term', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
