import os
import MySQLdb
import MySQLdb.cursors
import time,datetime
from pymysql import NULL
from SendEmail import *

class get_time:
    def __init__(self):
        self.year = datetime.datetime.today().year
        self.month = datetime.datetime.today().month
        self.day = datetime.datetime.today().day
        self.time = time.strftime("%H:%M:%S", time.localtime())
    def return_alltime(self):
        return "%s/%s/%s %s" % (self.year,self.month,self.day,self.time)
    def return_year(self):
        return "%s" % (self.year)
    def return_mouth(self):
        return "%s" % (self.month)
    def return_day(self):
        return "%s" % (self.day)

class linkdata:
    def __init__(self):
        self.db = MySQLdb.connect("47.101.187.89", "myblog", "C2NTRxspBtbXkD4p", "myblog", charset='utf8',cursorclass=MySQLdb.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def finddata(self):
        get_datas = "select * from video_item order by id desc"
        try:
            self.cursor.execute(get_datas)
            datas = self.cursor.fetchall()
            return datas
        except:
            return 0
        self.db.close()
    
    def finddynamic(self):
        get_dynamic = "select * from dynamic order by id desc"
        try:
            self.cursor.execute(get_dynamic)
            datas = self.cursor.fetchall()
            return datas
        except:
            return 0
        self.db.close()

    def insert_data(self,types,name,email,texts):
        times = get_time().return_alltime()
        insert_info = "insert into info (id,types,name,email,texts,time) values(0,%s,%s,%s,%s,%s)"
        par = (types,name,email,texts,times)
        try:
            self.cursor.execute(insert_info,par)
            self.db.commit()
        except Exception:
            self.db.rollback()
        send_email().send_out(par)
        self.db.close()

    def requests_data(self):
        requests_info = "select * from info order by id desc"
        try:
            self.cursor.execute(requests_info)
            datas = self.cursor.fetchall()
            return datas
        except:
            return 0
        self.db.close()

    def send_videoitem(self,infolist):
        infolist['year'] = str(get_time().return_year())
        infolist['mouth'] = str(get_time().return_mouth())+"/"+str(get_time().return_day())
        for i in infolist:
            if infolist[i] != NULL:
                send_videoitem_tex = "insert into video_item ("+i+") values("+infolist[i]+")"
                print(send_videoitem_tex)
                self.cursor.execute(send_videoitem_tex)
            else:
                pass
        self.db.commit()
        self.db.close()
