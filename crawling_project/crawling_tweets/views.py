from django.shortcuts import render , redirect
from .models import Post , Comment
import datetime
from .tstream import MaxListener
def home(request):

    return render(request, 'tweets/home.html')
import tweepy 
import Stream
import json
import logging
import time
import pyodbc
auth = tweepy.OAuthHandler("AlyWx6jjnYtLDXth2p7XT33xD",
                           "Ofz2WoZ4PzhXzpKWlAbDvRvQFa0CO3RgvCzv8Nbfes2f2u9NPe")
auth.set_access_token("1220190253228494850-Ta7PGsjS8X9ZIr6g4S6nV6mhBA0XCy",
                      "bwgxLkJiRU86VYyu3ptqIIM0atlv8LTjlVmzHR9XuOhf3")
api = tweepy.API(auth)
listener = MaxListener()
stream = Stream(auth, listener)
# tweets/home.html là tên folder chứa trang html
def about(request):
    max_tweets = 10

    if request.GET:
        keyword = request.GET['keyword']
        print(keyword,'KEYWORDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
        query = keyword
        searched_tweets = [status for status in tweepy.Cursor(api.search , q=query, tweet_mode='extended',lang='en').items(max_tweets)]
        for x in range(len(searched_tweets)):
                print("STATUSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")  
                tweet_id = searched_tweets[x].id
                username = searched_tweets[x].user.screen_name
                number_of_retweet = searched_tweets[x].retweet_count
                create_date = searched_tweets[x].created_at
                link_detail = 'https://twitter.com/',username,'/status/',tweet_id
                post_content = searched_tweets[x].full_text.encode('utf-8')
                print('The Original Tweet ID: ', tweet_id)
                print('The Original Tweet Username: ', username)
                print('The Original Tweet Text: ',post_content)
                print("The Original Tweet share: ", number_of_retweet)
                if not hasattr(searched_tweets[x], 'retweeted_status'):
                    number_of_react = searched_tweets[x].favorite_count
                    print("The Original Tweet like: ", number_of_react)
                if hasattr(searched_tweets[x], 'retweeted_status'):
                    number_of_react = searched_tweets[x].retweeted_status.favorite_count    
                    print("The Original Tweet like: ", number_of_react)
                crawl_date = datetime.datetime.now()   
                replies =  tweepy.Cursor(api.search, q='to:{}'.format(searched_tweets[x].user.screen_name),
                                             since_id=searched_tweets[x].id, tweet_mode='extended', lang='en').items()                         
                number_of_reply  = 0
                p = Post.objects.create(post_id = tweet_id,post_content= post_content,create_date= create_date,link_detail= link_detail, number_of_reply= number_of_reply,
                 number_of_retweet=number_of_retweet,number_of_react= number_of_react,crawl_date= crawl_date, keyword= keyword)
                p.save()
                uuidPost = p.uuid_post
                if Keyword_Crawler.objects.filter(keyword = keyword).exists():
                    print('This Keyword has already existed on Keyword_Crawler table')
                else:
                    kc = Keyword_Crawler.objects.create(keyword = keyword)
                    kc.save()
                while True:
                    try:
                        reply = replies.next()
                        if not hasattr(reply, 'in_reply_to_status_id_str'):
                            continue
                        if reply.in_reply_to_status_id == searched_tweets[x].id:
                            print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                            print(reply.user.screen_name,':')
                            print(reply.full_text.encode('utf-8'))
                            reply_crawl_date = datetime.datetime.now() 
                            link_reply_detail = 'https://twitter.com/',reply.user.screen_name,'/status/',reply.id
                            print("this is reply tweet's share: ", reply.retweet_count)
                            print("this is reply tweet's like: ", reply.favorite_count)
                            c = Comment(uuidPost , reply.id, reply.full_text.encode('utf-8'), reply.create_at, link_reply_detail , 
                                reply.retweet_count, reply.favorite_count, reply_crawl_date)
                            c.save()    
                    except tweepy.RateLimitError as e:
                        logging.error("Twitter api rate limit reached {}".format(e)) 
                        time.sleep(60) 
                        continue
                    except tweepy.TweepError as e:
                        logging.error("Tweepy error occured:{}".format(e))
                        break
                    except StopIteration :  
                        break
                    except Exception as e:
                        logging.error("Failed while fetching replies {}".format(e))
                        break
    return redirect('blog-home')

   
