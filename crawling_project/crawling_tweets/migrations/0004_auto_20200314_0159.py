# Generated by Django 2.1.15 on 2020-03-13 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawling_tweets', '0003_auto_20200314_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='crawl_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='post',
            name='crawl_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='keyword',
        ),
    ]