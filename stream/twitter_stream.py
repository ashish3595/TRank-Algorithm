#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time

#Variables that contains the user credentials to access Twitter API 
access_token = "140600080-MjqVYv70t4ngHhOjyqQ7VYNPa0ISfdYMn0nwyzLK"
access_token_secret = "FbeK7nWFec0ryYww5JdTb4jQRS6eVbIxHeSV4mXVdrugs"
consumer_key = "BfZpE2cQGMOtGnGNICgi1tGmn"
consumer_secret = "VdC07qWSUPRomgewYHUmzXzhMFc722E3YbDw4jFiwmvFZ8ZsxX"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet=all_data["text"]
        user_name = all_data["user"]["screen_name"]
        user_id = str(all_data["user"]["id"])
        user_foll_count = str(all_data["user"]["followers_count"])
        tweet_fav_count = str(all_data["favorite_count"])
        tweet_ret_count = str(all_data["retweet_count"])
        print user_id + "  " + user_name + "  " + tweet + "   " + user_foll_count + "   " + tweet_fav_count + " " + tweet_ret_count
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['car'])