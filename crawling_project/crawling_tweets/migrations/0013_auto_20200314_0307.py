# Generated by Django 2.1.15 on 2020-03-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling_tweets', '0012_auto_20200314_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='crawl_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='crawl_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]