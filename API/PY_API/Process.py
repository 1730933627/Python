from pymysql import NULL

class Process:
    def __init__(self):
        self.ls = ['id','name','type','img_url','video_url','bdy_photo','photo_password','bdy_video','video_password']

    def getdata(self,datalist):
        for x in self.ls:
            if x in datalist:
                pass
            else:
                datalist[x] = NULL

        infolist = {
                'id' : datalist['id'],
                'name' : datalist['name'],
                'type' : datalist['type'],
                'img_url' : datalist['img_url'],
                'video_url' : datalist['video_url'],
                'bdy_photo' : datalist['bdy_photo'],
                'photo_password' : datalist['photo_password'],
                'bdy_video' : datalist['bdy_video'],
                'video_password' : datalist['video_password']
        }
        return infolist