from django.shortcuts import render , redirect 
from django.utils import timezone
from .models import Post , Comment , Keyword_Crawler, Keyword
from urllib.request import urlopen
import tweepy
import json
import logging
import time
import pyodbc
import uuid
import pytz
ACCESS_TOKEN = "1220190253228494850-Ta7PGsjS8X9ZIr6g4S6nV6mhBA0XCy"
ACCESS_TOKEN_SECRET = "bwgxLkJiRU86VYyu3ptqIIM0atlv8LTjlVmzHR9XuOhf3"
CONSUMER_KEY = "AlyWx6jjnYtLDXth2p7XT33xD"
COMSUMER_SECRET= "Ofz2WoZ4PzhXzpKWlAbDvRvQFa0CO3RgvCzv8Nbfes2f2u9NPe"




auth = tweepy.OAuthHandler(CONSUMER_KEY,COMSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)

def home(request):
    return render(request, 'tweets/home.html')

# tweets/home.html là tên folder chứa trang html
def about(request):
    max_tweets = 10
    list_keyword = Keyword_Crawler.objects.all()
    for item in list_keyword:
        number_of_reply = 0
        query = item.keyword
        for status in tweepy.Cursor(api.search , q=query, tweet_mode='extended',lang='en').items(max_tweets):
                print("STATUSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")  
                tweet_id = status.id
                username = status.user.screen_name
                number_of_retweet = status.retweet_count
                create_date = status.created_at.replace(tzinfo=pytz.UTC)
                link_detail = 'https://twitter.com/',username,'/status/',tweet_id
                post_content = status.full_text.encode('utf-8')
                print('The Original Tweet User: ', username)
                print('The Original Tweet Post ID: ',tweet_id)
                print('keyword:', query)
                if not hasattr(status, 'retweeted_status'):
                    number_of_react = status.favorite_count
                if hasattr(status, 'retweeted_status'):
                    number_of_react = status.retweeted_status.favorite_count
                crawl_date = timezone.now()   
                p = Post.objects.create( 
                    uuid_post= uuid.uuid4(), post_id = tweet_id ,post_content= post_content,create_date= create_date,
                    link_detail= link_detail, number_of_reply= 0,
                    number_of_retweet=number_of_retweet,number_of_react= number_of_react,crawl_date= crawl_date, keyword= query)
                p.save()
                uuid_post = p.uuid_post
                uuid_post_in_reply = Post.objects.only('uuid_post').get(uuid_post = uuid_post)
                
                for reply in tweepy.Cursor(api.search, q='to:{}'.format(username),
                                             since_id=tweet_id, tweet_mode='extended', lang='en').items():                         
                        try:
                            if not hasattr(reply, 'in_reply_to_status_id_str'):
                                continue
                            if reply.in_reply_to_status_id == tweet_id:
                                print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                                print(reply.user.screen_name,':')
                                print(reply.full_text.encode('utf-8'))
                                link_reply_detail = 'https://twitter.com/',reply.user.screen_name,'/status/',reply.id
                                print("this is reply tweet's share: ", reply.retweet_count)
                                print("this is reply tweet's like: ", reply.favorite_count)
                                reply_create = reply.created_at.replace(tzinfo=pytz.UTC)
                                c = Comment.objects.create(
                                uuid_comment= uuid.uuid4(), uuid_post = uuid_post_in_reply, comment_id=reply.id,
                                comment_content= reply.full_text.encode('utf-8'), create_date =reply_create,
                                link_detail= link_reply_detail , 
                                number_of_reply =reply.retweet_count, number_of_react=reply.favorite_count,
                                crawl_date= crawl_date)
                                c.save()    
                                number_of_reply += 1;
                        except tweepy.RateLimitError as e:
                            logging.error("Twitter api rate limit reached {}".format(e)) 
                            time.sleep(900) 
                            continue
                        except tweepy.TweepError as e:
                            logging.error("Tweepy error occured:{}".format(e))
                            break
                        except tweepy.TweepError:
                            time.sleep(120)
                            continue
                        except Exception as e:
                            logging.error("Failed while fetching replies {}".format(e))
                            break
                updateReply = Post.objects.get(uuid_post = uuid_post)
                updateReply.number_of_reply = number_of_reply
                updateReply.save(update_fields=['number_of_reply'], force_update = True)            
    return redirect('blog-home')

   
