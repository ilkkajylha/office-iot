#!/usr/bin/env python
#coding: utf-8
"""koodi printtaa tämänhetkisen ajan 5 sekunnin välein kunnes minuutti on tullut täyteen,
jonka jälkeen ohjelma printtaa viestin 'Jee'."""
import datetime
import time

#print datetime.date.today()
#print datetime.datetime.now()
#testi datetimelle

finish_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
while datetime.datetime.now() < finish_time:
	print datetime.datetime.now()
	time.sleep(5)

print 'Jee'

"""koodi by asa"""