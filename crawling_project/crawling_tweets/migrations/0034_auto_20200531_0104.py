# Generated by Django 2.1.15 on 2020-05-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling_tweets', '0033_post_isnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='language',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.TextField(null=True),
        ),
    ]
