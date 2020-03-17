# Generated by Django 2.1.15 on 2020-03-13 19:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crawling_tweets', '0009_auto_20200314_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.BigIntegerField()),
                ('comment_content', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('link_detail', models.CharField(max_length=50)),
                ('number_of_reply', models.FloatField()),
                ('number_of_react', models.FloatField()),
                ('crawl_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.BigIntegerField()),
                ('post_content', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('link_detail', models.CharField(max_length=255)),
                ('number_of_reply', models.IntegerField()),
                ('number_of_retweet', models.IntegerField()),
                ('number_of_react', models.IntegerField()),
                ('crawl_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('keyword', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawling_tweets.Post'),
        ),
    ]