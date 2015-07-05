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
import re

"""
This function is designed to clean up data collected from tweeter, and reform a new refined database.
"""

# This filter is designed to filter out those text that has nothing to do with the symbol
# Return 0: no filtering, 1:text line matched filtering option.
# This filter is likely to filter out 60% of the junk data
def Filter1 (row):
    # find all stock symbol in the text
    # Ex: "b'$SUTI Has Gained 66.67%, Since Our Penny Stock Blog Alert! Huge News: http://t.co/llIxl7cUOL $QIHU $IBM $GWW $ACN'"
    # symbList = ['$SUTI', '$QIHU', '$IBM', '$GWW', '$ACN']
    p = re.compile(r'\$\w+')
    symbList = p.findall(str(row[-1]))
    # print(symbList)
    if (len(symbList) <= 1):
        # only 1 or no symbol is found, here we assume the text is 100% relevant and should be kept.
        return 0
    else:
        if (symbList[0] == '$' + row[0]):
            # the first symbol list is matching the symbol we search for.
            return 0
        else:
            # Here we assume the text has no relevance as shown in the example.
            # We set out to find text relevant to ACN.
            # However the text is really talking about SUTI.
            # Note: ACN is at the end of the matched findall Symbol list.
            return 1

# Connect to data base
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

j = 0
for i,row in enumerate(cursor.execute("select * from tw")):
    if Filter1(row):
        # print('>>del>> ' + row[0] + ' || ' + str(row[-1]))
        # print('>>del>> ' + str(row))
        pass
    else:
        # print('        ' + row[0] + ' || ' + str(row[-1]))
        # print('        ' + str(row))
        print(str(i) + ' ' + str(j) + ' ' + row[0] + ' || ' + str(row[-1]))
        j +=1

# print (cursor.fetchall())
