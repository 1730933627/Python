import bilibili_api as bl #Version - 2.1.4
import json,os,flask
from flask import request,render_template,send_from_directory
from flask_cors import CORS,cross_origin
from pymysql import NULL
from LinkData import *
from Process import *

server = flask.Flask(__name__)
CORS(server, resources={r'/*': {"origins": "*"}}, supports_credentials=True)

@server.route('/', methods=['get'])
def index():
    return render_template('index.html')
    
@server.route('/getvideoinfo', methods=['post'])
def getvideoinfo():
    videoinfo_res = {'status': 200,'err':0,'msg':"success",'data': linkdata().finddata()}
    return json.dumps(videoinfo_res, ensure_ascii=False)

@server.route('/getdynamic', methods=['post'])
def getdynamic():
    dynamic_res = {'status': 200,'err':0,'msg':"success",'data': linkdata().finddynamic()}
    return json.dumps(dynamic_res, ensure_ascii=False)

@server.route('/requests', methods=['post'])
def requests():
    requests_res = {'status': 200,'err':0,'msg':"success",'data': linkdata().requests_data()}
    return json.dumps(requests_res, ensure_ascii=False)

@server.route('/insert', methods=['post'])
def insert():
    types = request.form['types']
    name = request.form['name']
    email = request.form['email']
    texts = request.form['texts']
    insert_res = {'status': 200,'err':0,'msg':"success"}
    linkdata().insert_data(types,name,email,texts)
    return json.dumps(insert_res,ensure_ascii=False)

@server.route('/send_videoinfo', methods=['post'])
def send_videoinfo():
    datalist = request.form.to_dict()
    linkdata().send_videoitem(Process().getdata(datalist))
    insert_res = {'status': 200,'err':0,'msg':"success"}
    return json.dumps(insert_res,ensure_ascii=False)

@server.route('/bl-api', methods=['get'])
def get():
    uid = request.values.get("uid")
    vinfo = request.values.get("vinfo")
    relation = request.values.get("relation")
    if uid:
        return "<h1>"+"获取用户视频:"+uid+"</h1>"
    if vinfo:
        return "<h1>"+"获取视频信息"+vinfo+"</h1>"
    if relation:
        return "<h1>"+"获取粉丝和视频数"+relation+"</h1>"
    else:
        return "<h1>这是Get</h1>"

@server.route('/bl-api', methods=['post'])
def post():
    uid = request.values.get("uid")
    relation = request.values.get("relation")
    vinfo = request.values.get("vinfo")
    if uid:
        data = bl.user.get_videos(uid)
        datas = []
        for i in range(len(data)):
            datas.append([data[i]["title"],data[i]["pic"],data[i]["bvid"]])

        resu = {'code': 200, 'message': datas}
        return json.dumps(resu, ensure_ascii=False)
    if relation:
        
        follower = bl.user.get_relation_info(relation)
        sum_video = bl.user.get_overview(relation)
        datas = [follower["follower"],sum_video["video"]]
        resu = {'code': 200, 'message': datas}
        return json.dumps(resu, ensure_ascii=False)
    if vinfo:
        data = bl.video.get_video_info(vinfo)
        resu = {'code': 200, 'message': data}
        return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code':-1 ,'message':"无参数"}
        return json.dumps(resu, ensure_ascii=False)
 
if __name__ == '__main__':
    server.run(debug=True, port=8856, threaded=True,host='0.0.0.0')