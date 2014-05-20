import tweepy
import requests
import json
import re

def hashIt(s):
    for word in s:
        if len(word) > 8:
            word = ''.join(['#', word])
    return s

def standard(post):
    if len('\n'.join([post['title'], post['url']])) <= 140:
        try:
            txt = '\n'.join([post['title'], post['url']])
            txt = hashIt(txt)
            if txt not in pub:
                api.update_status('\n'.join([post['title'], post['url']]))
        except Exception, e:
            return 0

def short(post):
    match = re.match(r'^.*?[\.!\?](?:\s|$)',post['title']).group(0)

    if len('\n'.join([match, post['url']])) <= 140 and match is not None:
        txt = '\n'.join([match, post['url']])
        txt = hashIt(txt)
        if txt not in pub:
            api.update_status('\n'.join([match, post['url']]))
            return 1
        else: return 0
    else:
        return 0

def tweet(i, data):
    pub = api.home_timeline()
    post = data['data']['children'][i]['data']

    if standard(post) == 1:
        return 1
    elif short(post) == 1:
        return 1

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
