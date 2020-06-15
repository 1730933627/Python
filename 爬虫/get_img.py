import requests
import os
import pymysql

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
db = pymysql.connect(
        host = "123.56.167.19",
        user = "PyGetimages",
        passwd = "NrC8Xh8PWchLfeFe",
        charset='utf8'
        )

class get_img:
    
    def dir():
        if os.path.isdir("img"):
            pass
        else:
            os.mkdir("img")

    def main(db):
        cur = db.cursor()
        try:
            cur.execute("use PyGetimages;")
            cur.execute("create table main(name char(20))")
        except:
            cur.execute("use PyGetimages;")
        for d in range(25,29):
            for h in range(8,22):
                if(h<10):
                    h = "0"+str(h)
                for m in range(60):
                    if(m<10):
                        m = "0"+str(m)
                    for s in range(60):
                        if(s<10):
                            s = "0"+str(s)
                        for ms in range(99):
                            if(ms<10):
                                ms = "0"+str(ms)
                            temp = "http://img.gszciot.com//media/img/202004"
                            html= temp + str(d) + str(h) + str(m) + str(s)+ "_" + str(ms) +".jpg"
                            name= "202004" + str(d) + str(h) + str(m) + str(s)+ "_" + str(ms)
                            resp = requests.post(html,headers=headers)
                            if resp:
                                res = requests.get(html,headers=headers)
                                res.encoding="utf-8"
                                fi = open("img/{0}.jpg".format(name),"wb")
                                fi.write(res.content)
                                fi.close()
                                print(">>")
                                print("成功："+str(resp)+"<{}>".format(html))
                                get_img.mysql(name,db,cur)
                            else:
                                print("失败："+str(resp)+"<{}>".format(html))
                                pass
    def mysql(name,db,cur):
        cur.execute("INSERT INTO main(name) values ('{}')".format(name))
        print("MySQL写入成功！")
        print(">>")
        db.commit()
        db.close()
        

if __name__ == "__main__":
    get_img.dir()
    get_img.main(db)
    
