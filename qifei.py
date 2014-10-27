__author__ = 'lehong'
import sys
import time
import re
import optparse
import oauth2 as oauth
import urllib
import json

"""
This function is designed to analyze general public feeling toward certain stock.
"""

""" --- Parsing cmdLine options --- """
parser = optparse.OptionParser()
parser.add_option('-i', '--in', dest='sname',  default='MENT',                                  help='Stock symble.')
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

# Here %23 == '#'
encodedQuery = '%24BABA'

request, response = Request(
    'https://api.twitter.com/1.1/search/tweets.json?q=' + encodedQuery,
    'Gdwmom36VPbk9p7XODaHf1qs7',
    '4cZ8I713Du6LIsPHnt9LCelfU8rAnFURyII1XOXlgzXw1cdOTr')
print(request)
print(response)

# decode with utf8 is needed for Python 3
data = json.loads(response.decode('utf8'))
print('ok')
tweets = data['statuses']
for d in tweets:
    print(d.keys())
    for k in d.keys():
        print(k, '--->' , d[k])
    print('\n\n')
