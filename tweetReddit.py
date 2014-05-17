import tweepy
import requests
import json
import re

def tweet(i, data):
    pub = api.home_timeline()
    post = data['data']['children'][i]['data']

    try:
        if len('\n'.join([post['title'], post['url']])) <= 140:
            try:
                if '\n'.join([post['title'], post['url']]) not in pub:
                    api.update_status('\n'.join([post['title'], post['url']]))
            except Exception, e:
                print "It's too long"
                tweet(i+1, data)
            pass
        elif len('\n'.join([re.search(r'^.*?[\.!\?](?:\s|$)',post['title']).group(0),
            post['url']])) <= 140:
            try:
                if '\n'.join([re.search(r'^.*?[\.!\?](?:\s|$)',post['title']).group(0), post['url']]) not in pub:
                    api.update_status('\n'.join([re.search(r'^.*?[\.!\?](?:\s|$)',post['title']).group(0), post['url']]))
            except Exception, e:
                print 'Not even the first sentence.'
                tweet(i+1, data)
            pass
        else:
            print i
            print 'Could not resolve 140 rule issue.'
            tweet(i+1, data)
    except Exception, e:
        print 'Could not resolve 140 rule.'
        tweet(i+1, data)
        pass

if __name__ == '__main__':
    consumer_key = 'mq37G4cLvQ3TDCzTKYwCATJkk'
    consumer_secret = 'SmX9yjFfcFep72kinT50E0sJ7aqibgtwO1z5rO9yhIXGZAd86j'

    access_token='2497666189-UeD429YRQvzuTOvruwb30h6iFFPmoNEDViZh2fv'
    access_token_secret='c2uTONBxxRsCmyNpP9Wptb8IZLsGBvKNq27Ko6QTMYUMN'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    r = requests.get(r'http://www.reddit.com/r/futurology/.json')
    data = json.loads(r.text)

    tweet(1, data)
