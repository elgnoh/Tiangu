#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4
__author__ = 'lehong'
# A minimal SQLite shell for experiments
import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print ("Enter your SQL commands to execute in sqlite3.")
print ("Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print (cur.fetchall())
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
        buffer = ""

con.close()

# Example: sqlite operations in shell
# The following lines can be tried.
# CREATE TABLE stocks2 (date text, trans text, symbol text, qty real, price real, UNIQUE(date));
# INSERT INTO stocks2 VALUES ('2006-01-05','BUY','RHAT',100,35.14);
# SELECT * FROM stocks2;
# .schema tbName # prints table title
# SELECT * FROM stock2 where symbl = 'CVEO'
# SELECT created_at,screen_name,followers_count,text from tw where symbol = 'CVEO' AND followers_count > 500;