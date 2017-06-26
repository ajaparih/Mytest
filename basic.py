#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
ckey = 'pEXHtKtQCphx7qR9QdZQa6yDX'
csecret = '3rkHc7Jh2zcxMc7qiRT6maZWogCIblz9UJPGqrrW6dNdIJsjxJ'
atoken = '760904492141252608-vYulAbTid2OT4uA6OL3FhbUwIG38p3e'
asecret = '1HxWsWsE0LC8TZIB8dx27l6speDwC6ozOaZa0L47SzBVz'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['ransomeware', 'malware', 'ddos'])
