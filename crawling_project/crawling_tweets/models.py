from django.db import models
import uuid
class Post(models.Model):
    uuid_post = models.UUIDField(primary_key=True , default = uuid.uuid4, editable = False)
    post_id = models.BigIntegerField()
    post_content = models.TextField()
    create_date = models.DateTimeField()
    link_detail = models.TextField()
    number_of_reply = models.FloatField()
    number_of_retweet = models.FloatField()
    number_of_react = models.FloatField()
    crawl_date = models.DateTimeField(['%Y-%m-%d %H:%M:%S'])
    keyword = models.CharField(max_length=50)
    class Meta:
        db_table = "Post"
    def __str__(self): 
        return self.uuidPost

class Comment(models.Model):
    uuid_comment = models.UUIDField(primary_key=True , default = uuid.uuid4, editable = False)
    uuidPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_id = models.BigIntegerField()
    comment_content = models.TextField()
    create_date = models.DateTimeField()
    link_detail = models.TextField()
    number_of_reply = models.FloatField()
    number_of_react = models.FloatField()
    crawl_date = models.DateTimeField(['%Y-%m-%d %H:%M:%S'])
    class Meta:
        db_table = "Comment"

class Keyword_Crawler(models.Model):
    keyword = models.CharField(max_length=50, primary_key=True, editable=False)
    class Meta:
        db_table = "Keyword_Crawler"        