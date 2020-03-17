import tweepy

class MaxListener(tweepy.StreamListener):

    def on_data(seft , raw_data):
        self.process_data(raw_data)

        return True
    
    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if(status_code == 420):
            return False

class MaxStream():

    def __init__(self, auth, listener):
        self.stream  = tweepy.Stream(auth = auth, listener = listener)