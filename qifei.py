#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4
__author__ = 'lehong'
import sys
import time
import re
import optparse
import oauth2 as oauth
import urllib
import json
import sqlite3
import pprint

"""
This function is designed to analyze general public feeling toward certain stock.
"""

""" --- Parsing cmdLine options --- """
parser = optparse.OptionParser()
parser.add_option('-i', '--in', dest='sname',  default='MENT',                                  help='Stock symble.')
parser.add_option('-t',         dest='t',      default=60,    action='store',      type='int',  help='Time span in secs')
# parser.add_option('-l',         dest='doLive', default=False, action='storr_true',              help='live chart for stock')
# parser.add_option('-x',         dest='x',      default=0,     action='storre',     type='int',  help='Index to grab x value')

(opts, args) = parser.parse_args()
if not opts.__dict__['sname']:
    print ("mandatory option -i <file>")
    parser.print_help()
    sys.exit (-1)
"""--------------------------------"""

print(opts.sname)

def Request(url, key, secret, http_method = 'GET', post_body = '', http_headers = ''):
    consumer = oauth.Consumer(key = 'Gdwmom36VPbk9p7XODaHf1qs7', secret = '4cZ8I713Du6LIsPHnt9LCelfU8rAnFURyII1XOXlgzXw1cdOTr')
    token = oauth.Token(key = '11585502-XJ81s46PsZ5tqNqJYnYiUOmhKGkpsbFJhib8jo91v', secret = '6eDAmP9Q43wKCUJwPKfodJ2TJTbU57p7xZ8m4mGEceINr')
    client = oauth.Client(consumer, token)

    request = client.request(
        url,
        method = http_method,
        body = post_body,
        headers = http_headers)

    return request

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="Gdwmom36VPbk9p7XODaHf1qs7",
    secret="4cZ8I713Du6LIsPHnt9LCelfU8rAnFURyII1XOXlgzXw1cdOTr")

""" Here is the method posted on twitter page, not yet know how to make it work
# Request token URL for Twitter.
request_token_url = "http://twitter.com/oauth/request_token"
# Create our client.
client = oauth.Client(consumer)
# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
#print(resp)
print(content)
print('ok')
"""

# Here %23 == '#' %24 == '$' http://meyerweb.com/eric/tools/dencoder/ helps encode or decode rul.
# encodedQuery = '%24CVEO'
encodedQuery = '%24'+opts.sname

while True:
    time.sleep(60)
    request, response = Request(
        'https://api.twitter.com/1.1/search/tweets.json?q=' + encodedQuery,
        'Gdwmom36VPbk9p7XODaHf1qs7',
        '4cZ8I713Du6LIsPHnt9LCelfU8rAnFURyII1XOXlgzXw1cdOTr')
    # print(request)
    # print(response)

    # decode with utf8 is needed for Python 3
    data = json.loads(response.decode('utf8'))

    tweets = data['statuses']
    tweets2sq = []
    for d in reversed(tweets):
        # print(d.keys())
        print('text --->',d['text'])
        print('created_at --->',d['created_at'])
        print('user/screen_name --->', d['user']['screen_name'])
        print('user/friends_count',    d['user']['friends_count'])
        print('user/followers_count',  d['user']['followers_count'])
        print('user/id_str',           d['user']['id_str'])
        print('user/favourites_count', d['user']['favourites_count'])
        # for k in d.keys():
        #     if (k == 'text'):
        #         print(k, '--->' , d[k].replace('\n', ' '))
        tweets2sq.append((opts.sname, d['created_at'], d['user']['screen_name'], int(d['user']['friends_count']), int(d['user']['followers_count']), int(d['user']['id_str']), int(d['user']['favourites_count']), d['text'].replace('\n', ' ')))
        print('\n')

    print(encodedQuery)
    print(tweets[0].keys())
    pprint.pprint(tweets2sq)
    # Test changes.

    # Project 1 will attempt to use yahoo-finance to retrieve stock data. These data will be stored alone with twitter data.
    # Testing code will be written in yahooFinTest.py

    # Project 2 Will attempt to use https://docs.python.org/2/library/sqlite3.html for database storage.
    # Test sqlite3
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create Table tw is not exist
    # This table is designed to store twitter info on stock symbols.
    # The table is also designed to be cumulative, so future data fishing is possible.
    # Table format
    c.execute('''CREATE TABLE IF NOT EXISTS tw (symbol text, created_at text, screen_name text, friends_count integer, followers_count integer, id_str integer, favourites_count integer, text text)''' )
    c.executemany('INSERT OR IGNORE INTO tw VALUES (?,?,?,?,?,?,?,?)', tweets2sq)
    conn.commit()
    conn.close()

