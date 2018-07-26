#coding:utf-8
from selenium import webdriver
import requests
from lxml import etree
import random
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import requests
import json
import time
import sys
import psycopg2
import re
import datetime
import calendar
reload(sys)
sys.setdefaultencoding('utf-8')
f=open(r'50.txt')
fr=f.read()
locate=fr.split(' ')
# print locate
# locate=['舟山']
def sele():
	conn=psycopg2.connect(database="postgres", user="postgres", password="9090", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	day,lastDay=time1()
	day1=str(day)[:7]
	try:
		cur.execute("insert into  yemo (year_month) values ('%s'); " % day1)
		conn.commit()
	except Exception,e:
		# print 'yemo'
		# print e
		conn.rollback()

	driver=webdriver.Chrome()
	# place='北京'
	for place in locate:
		url = 'http://piao.qunar.com/ticket/list.htm?keyword='+ str(place) +'&region=&from=mpl_search_suggest&page={}'
		# sightlist=[]
		i=1
		while i >0:
			html=driver.get(url.format(i))
			html=driver.page_source.encode("gbk","ignore").decode("gbk")
			selector = etree.HTML(html)
			try:
				ye = selector.xpath('.//div[@class="pager"]/a/text()')
				if i > int(ye[len(ye)-2]):
					break
				informations = selector.xpath('//div[@class="result_list"]/div')
				informations = selector.xpath('//div[@class="result_list"]/div')
				for inf in informations: #获取必要信息
					sight_name = inf.xpath('./div/div/h3/a/text()')[0]
					sight_level = inf.xpath('.//span[@class="level"]/text()')
					if len(sight_level):
						sight_level = sight_level[0].replace('景区','')
					else:
						sight_level = 0
					try:
						sight_area = inf.xpath('.//span[@class="area"]/a/text()')[0]
					except:
						sight_area='0'
					sight_hot = inf.xpath('.//span[@class="product_star_level"]//span/text()')[0].replace('热度 ','')
					sight_add = inf.xpath('.//p[@class="address color999"]/span/text()')[0]
					sight_add = re.sub('地址：|（.*?）|\(.*?\)|，.*?$|\/.*?$','',str(sight_add))
					sight_price = inf.xpath('.//span[@class="sight_item_price"]/em/text()')
					if len(sight_price):
						sight_price = sight_price[0]
					else:
						sight_price = 0
					try:
						sight_soldnum = inf.xpath('.//span[@class="hot_num"]/text()')[0]
					except:
						sight_soldnum = 0
					try:
						sight_point = inf.xpath('./@data-point')[0]
					except:
						sight_point = 0
					
					# sightlist.append([sight_name,sight_level,sight_area,float(sight_price),int(sight_soldnum),float(sight_hot),sight_add.replace('地址：',''),sight_point])
					try:
						sql="insert into attractions (sight_name,sight_level,sight_area,sight_price,sight_soldnum,sight_hot,sight_addreplace,sight_point,year_month) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s');" %\
								(str(sight_name),str(sight_level),str(sight_area),float(sight_price),int(sight_soldnum),float(sight_hot),sight_add.replace('地址：',''),sight_point,str(day1))
						cur.execute(sql)
						conn.commit()
					except Exception,e:
						print e
						conn.rollback()
						sql="update attractions set sight_level = '%s', sight_price='%s',sight_soldnum='%s',sight_hot='%s' where sight_name='%s';" % (str(sight_level),float(sight_price),int(sight_soldnum),float(sight_hot),str(sight_name))
						try:
							cur.execute(sql)
							conn.commit()
						except Exception,e:
							print e
							conn.rollback()
					try:
						cur.execute("insert into area (sight_area) values ('%s');" % str(sight_area))
						conn.commit()
					except Exception,e:
						print 'area'
						print e
						conn.rollback()
				# cur.execute('select sight_area from attractions where year_month="%s";' % day1)
				# rows=cur.fetchall()
				# print rows
			except:
				# driver.close()
				if i >int(len(ye)-2):
					break
				else:
					i += 1

					continue
			i += 1
			tim=random.randint(1,10)
			time.sleep(tim)
	cur.execute('select sight_area from attractions where year_month="%s";' % day1)
	rows=cur.fetchall()
	print len(rows)
	cur.close()
	conn.close()
	print 'done'
	time.sleep(3)
	driver.close()
def time1():	
	yea=datetime.datetime.now().year
	mont=datetime.datetime.now().month
	day=datetime.date.today()
	firstDayWeekDay, monthRange = calendar.monthrange(yea, mont)
	lastDay = datetime.date(year=yea, month=mont, day=monthRange)
	return day,lastDay
def main():
	while True:	
		try:
			sele()
			ti=1
			while ti==1:
			    day,lastDay=time1()
			    if day==lastDay:
			        ti=2
			    else:
			        # print 'sleep'
			        time.sleep(1*60*60)
		except Exception,e:
			print e
			continue		
if __name__=='__main__':
	main()
