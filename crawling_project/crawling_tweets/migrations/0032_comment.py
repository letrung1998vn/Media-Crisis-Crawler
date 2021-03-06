# Generated by Django 2.1.15 on 2020-03-26 16:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crawling_tweets', '0031_auto_20200326_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uuid_comment', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment_id', models.BigIntegerField()),
                ('comment_content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('link_detail', models.TextField()),
                ('number_of_reply', models.FloatField()),
                ('number_of_react', models.FloatField()),
                ('crawl_date', models.DateTimeField(verbose_name=['%Y-%m-%d %H:%M:%S'])),
                ('uuid_post', models.ForeignKey(blank=True, db_column='uuid_post', null=True, on_delete=django.db.models.deletion.CASCADE, to='crawling_tweets.Post')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
