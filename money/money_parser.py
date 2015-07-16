## -*- coding: utf-8 -*-
from grab import Grab
from selection import *

def gomoney():
	g = Grab(log_file="out.html")
	g.setup(post={'login': '0041703721', 'pass': 'kisses85'})
	g.go("http://www.wimagic.com.ua/1.php")
	try:
		f=open("/home/yegor/.virtualenvs/www-slice/slice/money/money.txt", "w")
	except IOError:
		f = False
		return f
	if f:
		try:
			f.write(g.doc.select('//html/body/pre/h2').text()[-6:])
		except IndexError:
			f.write('Not found')


def mymoney():
	try:
		f=open("/home/yegor/.virtualenvs/www-slice/slice/money/money.txt", "r")
		return f.readlines()[0]
	except IOError:
		return False
