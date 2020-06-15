import requests
import bs4

url = 'https://space.bilibili.com/3822341/video'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
res = requests.get(url,headers=headers)
res.encoding = "utf-8"
html = res.text
soup = bs4.BeautifulSoup(html,'lxml')

def wirte_txt():
    fi = open('yan_lin.txt','w',encoding='utf-8')
    for line in soup.find_all('li',class_='small-item fakeDanmu-item watched'):
        fi.wirte(line.get_text(),end='\n')
    fi.close()
"""
def read_fi():
    fi = open('yan_lin.txt',encoding='utf-8')
    for i in fi.readlines():
        print(i,end='\n')
    fi.close()
"""
def write_html():
    fo = open('html.txt','w',encoding='utf-8')
    fo.write(soup.prettify())
    fo.close()

def main():
    print('====================')
    try:
        wirte_txt()
        read_fi()
        write_html()
        print("{: ^18}".format('成功!'))
    except:
        print("{: ^18}".format('正在重试!'))
        main()
    print('====================')
    
if __name__=='__main__':
    main()
