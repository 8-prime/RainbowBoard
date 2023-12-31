# Generated by Django 5.0 on 2023-12-23 22:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entry_guid', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('published', models.DateTimeField()),
                ('link', models.URLField()),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), null=True, size=None)),
                ('cold_rent', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('warm_rent', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('area', models.FloatField()),
                ('text', models.TextField()),
            ],
        ),
    ]
