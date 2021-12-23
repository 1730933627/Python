import requests
import bs4
import os


class Demo:
    def __init__(self):
        print("{:-^30}".format("开始获取"))
        self.html = ''
        self.url = "https://www.bh3.com/wallpapers"
        self.img_list = []

    def get_html(self):
        res = requests.get(self.url)
        res.encoding = 'utf-8'
        self.html = res.text
        return self.html

    def bs4_html(self):
        soup = bs4.BeautifulSoup(self.html, 'lxml')
        paper = soup.find_all(name='div', attrs={"class": "paper-item"})
        for line in paper:
            self.img_list.append(line.a['href'])
        return self.img_list

    def get_img(self):
        count = 1
        if not os.path.exists("./get_img"):
            os.mkdir("./get_img")
        for i in self.img_list:
            print("正在下载{:.>25}".format("第"+str(count)+"个"))
            img = requests.get(i)
            with open(f"./get_img/{count}.jpg", 'wb') as file:
                file.write(img.content)
                print("下载完成{:.>25}".format("第"+str(count)+"个"))
            count += 1

    def __del__(self):
        del self.html
        del self.img_list
        print("{:-^30}".format("全部完成"))


def main():
    demo = Demo()
    demo.get_html()
    demo.bs4_html()
    demo.get_img()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
