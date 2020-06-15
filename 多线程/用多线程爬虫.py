import bs4
import requests
import threading
import time

exitFalg = 0
url = "https://www.runoob.com/python3/python3-multithreading.html"

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print("开始线程:"+self.name)
        myThread.get_html(self.name,self.counter)
        print("{0}结束进程".format(self.threadID))

    def get_html(self):
        html = requests.get(url)
        html.encoding = 'utf-8'
        soup = bs4.BeautifulSoup(html.text,'lxml')
        for each in soup.find_all('pre',class_='prettyprint prettyprinted'):
            print(each.get_text())

thread1 = myThread(1,"thread1",1)

thread1.start()
thread1.join()
print("完成")



