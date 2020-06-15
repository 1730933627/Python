import requests
import json
import re

def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    res = requests.get(url=url, headers=headers)
    return res

def get_cid(BV):
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={BV}&jsonp=jsonp'
    res = download_page(url)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid

def get_dan_mu(cid):
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = download_page(url)
    res_xml = res.content.decode('utf-8')
    pattern = re.compile('<d.*?>(.*?)</d>')
    dan_mu_list = pattern.findall(res_xml)
    print("弹幕获取成功")
    return dan_mu_list

def save_to_file(dan_mu_list, filename):
    print("正在写入文件")
    with open(filename, mode='w', encoding='utf-8') as f:
        for one_dan_mu in dan_mu_list:
            f.write(one_dan_mu+"\n")

def dan_mu_spider(BV):
    cid = get_cid(BV)
    dan_mu_list = get_dan_mu(cid)
    save_to_file(dan_mu_list, f'{BV}.txt')
    print("保存成功")


if __name__ == '__main__':
    try:
        BV = input("输入BV号：")
        dan_mu_spider(BV)
    except:
        print("BV号输出错误")
