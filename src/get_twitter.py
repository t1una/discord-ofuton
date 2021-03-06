from lib.twitter import Twitter
from lib.tw_message import tw_message
from lib.dataset.tweet import Tweet
from lib.settings import settings
import requests.exceptions
import schedule
import time
import requests.exceptions

setting = settings.get_setting()
def read_twitter():
        try:
                twitter = Twitter()
                twitter.get_list_id(setting['TWITTER_LIST'])
                messages =  twitter.read_list_tl()
                tweet = Tweet()
                tweet.add_values(messages)
        except requests.exceptions.ConnectionError:
                pass

def main():
        count=setting['TWITTER_READ_TIME_MINUTE']
        try:
                read_twitter()
                time.sleep(count)
                schedule.every(count).minutes.do(read_twitter)
                while True:
                        schedule.run_pending()
                        time.sleep(1)
        except requests.exceptions.ConnectionError:
                pass

if __name__ == "__main__":
    main()
