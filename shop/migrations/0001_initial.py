# Generated by Django 4.2.7 on 2023-12-03 05:06

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=150)),
                ('stars', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]