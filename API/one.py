import bilibili_api as bl
import flask
from flask import request
from flask_cors import CORS
import json

server = flask.Flask(__name__)
CORS(server)

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
        return "<h1>"+"获取粉丝数"+relation+"</h1>"
    else:
        return "<h1>这是get</h1>"

@server.route('/bl-api', methods=['post'])
def post():
    uid = request.values.get("uid")
    relation = request.values.get("relation")
    vinfo = request.values.get("vinfo")
    dynamic = request.values.get("dynamic")
    if uid:
        data = bl.user.get_videos(uid)
        datas = []
        for i in range(len(data)):
            datas.append([data[i]["title"],"https:"+data[i]["pic"],data[i]["bvid"]])

        resu = {'code': 200, 'message': datas}
        return json.dumps(resu, ensure_ascii=False)
    if relation:
        data = bl.user.get_relation_info(relation)
        datas = data["follower"]
        resu = {'code': 200, 'message': datas}
        return json.dumps(resu, ensure_ascii=False)
    if vinfo:
        data = bl.video.get_video_info(vinfo)
        resu = {'code': 200, 'message': data}
        return json.dumps(resu, ensure_ascii=False)
    if dynamic:
        data = bl.dynamic.get_info(dynamic)
        resu = {'code': 200,'message':data}
        return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code':-1 ,'message':"无参数"}
        return json.dumps(resu, ensure_ascii=False)
 
if __name__ == '__main__':
    server.run(debug=True, port=8856, host='0.0.0.0')
