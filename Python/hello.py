import tweepy
import json
import logging
import time
import pyodbc
from tweepy import Stream , StreamListener

class TwitterAuthenticate():

    def authenticate_twitter_app():
        auth = tweepy.OAuthHandler("AlyWx6jjnYtLDXth2p7XT33xD",
                           "Ofz2WoZ4PzhXzpKWlAbDvRvQFa0CO3RgvCzv8Nbfes2f2u9NPe")
        auth.set_access_token("1220190253228494850-Ta7PGsjS8X9ZIr6g4S6nV6mhBA0XCy", 
                      "bwgxLkJiRU86VYyu3ptqIIM0atlv8LTjlVmzHR9XuOhf3")
        return auth
class TwitterStreamer():

    def stream_tweets(keyword):
        auth = TwitterAuthenticate.authenticate_twitter_app()
        listener = StdOutListener()
        stream = Stream(auth , listener, tweet_mode='extended')
        # stream.filter(track=keyword , follow=, languages=['en'])
        stream.filter(track=keyword , languages=['en'])

class StdOutListener(StreamListener):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 100
    def on_data(self , data):
        try:
            jsonData = json.loads(data)
            complete = json.dumps(jsonData, indent=4, sort_keys=True)
            print('Statusssssssssssssssssssssssssssssssssssssssssss')
            print('username:',jsonData['user']['screen_name'])
            print(jsonData['user']['id'])
            print(jsonData['extended_tweet']['full_text'])
            print(jsonData['id'])
            print('Tweet Create At: ',jsonData['created_at'])
            api = tweepy.API(TwitterAuthenticate.authenticate_twitter_app())
            replies =  tweepy.Cursor(api.search, q='to:{}'.format(jsonData['user']['screen_name']),
                                             since_id=jsonData['id'], tweet_mode='extended', lang='en').items(500)
            while True:
                try:
                    reply = replies.next()
                    if not hasattr(reply, 'in_reply_to_status_id'):
                        continue
                    if reply.in_reply_to_status_id == jsonData['id']:
                        print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                        print(reply.user.screen_name,':')
                        print(reply.full_text)
                        print("this is reply tweet's share: ", reply.retweet_count)
                        print("this is reply tweet's like: ", reply.favorite_count)
                except tweepy.RateLimitError as e:
                    logging.error("Twitter api rate limit reached".format(e)) 
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
            self.counter += 1
            if self.counter < self.limit:
                return True
            else :
                return False
        except BaseException as e:
            print('failed on_status,',str(e))
            time.sleep(5)
        return True
    

    def on_error(self, status_code):
        if(status_code == 420):
            return False
        print(status_code)




if __name__ == "__main__":
  
    twitter_streamer = TwitterStreamer;
    twitter_streamer.stream_tweets('covid')
    


























































# keyword = 'hospital '
# query = keyword
# max_tweets = 200
# api = tweepy.API(TwitterAuthenticate.authenticate_twitter_app())
# searched_tweets = [status for status in tweepy.Cursor(api.search , q=query, tweet_mode='extended',lang='en').items(max_tweets)]
# for x in range(len(searched_tweets)):
#             # print("STATUSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")  
#             # tweet_id = searched_tweets[x].id
#             # print('The Original Tweet ID: ', tweet_id)
#             # username = searched_tweets[x].user.screen_name
#             # print('The Original Tweet Username: ', username)
#             # print('The Original Tweet Text: ',searched_tweets[x].full_text.encode('utf-8'))
#             # if not hasattr(searched_tweets[x], 'retweeted_status'): 
#             #     print("The Original Tweet share: ", searched_tweets[x].retweet_count)
#             # print("The Original Tweet like: ", searched_tweets[x].favorite_count)  
#             # print("The Original Tweet Reply: ", searched_tweets[x].reply_count)
#             replies =  tweepy.Cursor(api.search, q='to:{}'.format('NikkiGlaser'),since_id=1239052761054040064, tweet_mode='extended', lang='en').items(500)
#             while True:
#                 try:
#                     reply = replies.next()
#                     if not hasattr(reply, 'in_reply_to_status_id_str'):
#                         continue
#                     if reply.in_reply_to_status_id == 1239052761054040064:
#                         print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
#                         print(reply.user.screen_name,':')
#                         print(reply.full_text)
#                         print("this is reply tweet's share: ", reply.retweet_count)
#                         print("this is reply tweet's like: ", reply.favorite_count)
#                 except tweepy.RateLimitError as e:
#                     logging.error("Twitter api rate limit reached".format(e)) 
#                     time.sleep(60) 
#                     continue
#                 except tweepy.TweepError as e:
#                     logging.error("Tweepy error occured:{}".format(e))
#                     break
#                 except StopIteration :  
#                     break
#                 except Exception as e:
#                     logging.error("Failed while fetching replies {}".format(e))
#                     break
            

# for r in range(len(replies)):json_str = json.dumps(replies[r]._json)
# parsed = json.loads(json_str)
# complete = json.dumps(parsed, indent=4, sort_keys=True)
# print(complete)


# ==================================================================================
# for x in range(len(searched_tweets)):
#         print("STATUSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
#         json_str = json.dumps(searched_tweets[x]._json)
#         parsed = json.loads(json_str)
#         complete = json.dumps(parsed, indent=4, sort_keys=True)
#         # print(complete)        
#         print("Result of this crawling: ", len(searched_tweets))
#         print("Reply's ID Original : ",searched_tweets[x].in_reply_to_status_id_str)
#         tweet_id = str(searched_tweets[x].id)
#         print("This tweet's ID Original  id is: ", tweet_id)
#         user_name = searched_tweets[x].user.screen_name
#         print("this tweet's username is: ", user_name)
#         print("this is tweet's text", searched_tweets[x].full_text)
#         print("this is tweet's share: ", searched_tweets[x].retweet_count)
#         print("this is tweet's like: ", searched_tweets[x].favorite_count)
#             # cursor = conn.cursor()

#             # cursor.execute('''
#             #     INSERT INTO TestDB.dbo.Status(id,text ,share, like )
#             #     VALUES
#             #     (?,?,?,?)
#             #     ''')
#             # cursor.execute(query, [tweet_id, searched_tweets[x].text,
#             # searched_tweets[x].retweet_count,searched_tweets[x].favorite_count])            
#             # conn.commit()
#             # in_reply_to_status_id
#         print("Reply count: ", searched_tweets[x].reply_count)
#         replies = [status for status in tweepy.Cursor(api.search, q='to:{}'.format(user_name),
#                                              since_id=tweet_id, tweet_mode='extended', lang='en').items()]
#         for x in range(len(replies)): 
#             print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
#             json_str = json.dumps(replies[x]._json)
#             parsed = json.loads(json_str)
#             complete = json.dumps(parsed, indent=4, sort_keys=True)
#             print(complete)        
#         for x in range(len(replies)): 
#             if hasattr(replies[x], 'in_reply_to_status_id_str'):
#                 if(replies[x].in_reply_to_status_id_str == tweet_id):
#                     print("REPLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
#                     tweet_id = replies[x].id
#                     print("This reply tweet's id is: ", tweet_id)
#                     print("This is tweet's id orginally: ", replies[x].in_reply_to_status_id_str)
#                     user_name = replies[x].user.screen_name
#                     print("this reply tweet's username is: ", user_name)
#                     print("this is reply tweet's text", replies[x].full_text)
#                     print("this is reply tweet's share: ", replies[x].retweet_count)
#                     print("this is reply tweet's like: ", replies[x].favorite_count)

#             # cursor = conn.cursor()


            #     INSERT INTO TestDB.dbo.Reply(id,text ,share, like )
            #     VALUES
            #     (?,?,?,?)
            #     ''')
            # cursor.execute(query, [tweet_id, replies[x].full_text,
            # replies[x].retweet_count, replies[x].favorite_count])            
            # conn.commit()