# Generated by Django 2.1.15 on 2020-03-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling_tweets', '0018_auto_20200314_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='link_detail',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='link_detail',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(max_length=5000),
        ),
    ]
