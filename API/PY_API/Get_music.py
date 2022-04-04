from dataclasses import dataclass
import requests
import json

def read_json(json_name):
    filename =  json_name + '.json'
    directory = "json"
    try:
        with open (directory+"/"+filename,encoding='utf-8') as f:
            info = json.load(f)
            return json.dumps(info,ensure_ascii=False)
    except Exception as e:
        return json.dumps("Exception is:{}".format(e), ensure_ascii=False)

def write_info(id):
    music = Music(id)
    music.save_data(music.get_songlist())

class Music():
    def __init__(self,id=2984712321):
        self.id = str(id)
        self.url = "https://music.yanlinn.com/playlist/detail?id="+ self.id
        self.song_info,self.playlist = [],[]
        self.mp3 = None

    def save_data(self,data):
        data=json.dumps(data,ensure_ascii=False)
        with open('json/music_list.json','w',encoding='utf-8') as f:
            f.write(data)
            f.close()

    def get_songurl(self,song_id):
        url = "https://music.yanlinn.com/song/detail?ids=" + str(song_id)
        songdata = requests.get(url).json()
        name = songdata["songs"][0]["name"]
        art = songdata["songs"][0]["ar"][0]["name"]
        pic = songdata["songs"][0]["al"]["picUrl"]
        self.song_info.append({"name":name,"art":art,"pic":pic})

    def get_musicurl(self,music_id):
        url = "https://music.yanlinn.com/song/url?id=" + str(music_id)
        music_req = requests.get(url).json()
        self.mp3 = music_req["data"][0]["url"]

    def get_songlist(self):
        req = requests.get(self.url).json()
        songlistarr = req["playlist"]["trackIds"]
        for i in range(len(songlistarr)):
            self.get_songurl(songlistarr[i]["id"])
            self.get_musicurl(songlistarr[i]["id"])
            temp = {
                "title":self.song_info[i]["name"],
                "artist":self.song_info[i]["art"],
                "mp3": self.mp3,
                "cover":self.song_info[i]["pic"]
            }
            if self.mp3!=None:
                self.playlist.append(temp)
        self.save_data(self.playlist)
        return self.playlist
