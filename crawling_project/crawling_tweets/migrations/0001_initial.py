# Generated by Django 3.0.4 on 2020-03-13 10:05

import builtins
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigIntegerField(primary_key=builtins.id, serialize=False)),
                ('crawl_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('keyword', models.CharField(max_length=50)),
            ],
        ),
    ]