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
print(cveo.get_price()                        )
print(cveo.get_change()                       )
print(cveo.get_volume()                       )
print(cveo.get_prev_close()                   )
print(cveo.get_open()                         )
print(cveo.get_avg_daily_volume()             )
print(cveo.get_stock_exchange()               )
print(cveo.get_market_cap()                   )
print(cveo.get_book_value()                   )
print(cveo.get_ebitda()                       )
print(cveo.get_dividend_share()               )
print(cveo.get_dividend_yield()               )
print(cveo.get_earnings_share()               )
print(cveo.get_days_high()                    )
print(cveo.get_days_low()                     )
print(cveo.get_year_high()                    )
print(cveo.get_year_low()                     )
print(cveo.get_50day_moving_avg()             )
print(cveo.get_200day_moving_avg()            )
print(cveo.get_price_earnings_ratio()         )
print(cveo.get_price_earnings_growth_ratio()  )
print(cveo.get_price_sales()                  )
print(cveo.get_price_book()                   )
print(cveo.get_short_ratio()                  )

