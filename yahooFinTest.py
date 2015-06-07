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
import yahoo_finance as yf

''' Example is at https://pypi.python.org/pypi/yahoo-finance '''

cveo = yf.Share('CVEO')
print(cveo.get_open())
print(cveo.get_price())


