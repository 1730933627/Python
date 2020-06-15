from PIL import Image,ImageFont,ImageDraw
import os,sys

print("===========================")
print("文本放在同目录命名为out.txt")
print("===========================")
try:
    pxx = eval(input("导出图片像素(X):"))
    pxy = eval(input("导出图片像素(Y):"))
    try:
        mach = eval(input("缩放倍数(不加倍回车)："))
        pxx = pxx * mach
        pxy = pxy * mach
    except:
        pass
except:
    pass
fi = open("out.txt","r")
text = ""
width = 0
height = 0
for i in fi.readlines():
    text += i
    width = len(i)
    height += 1
fi.close()

print("=================================================")
print("=================正在转换···==================")
print("=================================================")

width = width*6+11
height = height*15+14

img = Image.new("RGB", (width,height), (255,255,255))
idr = ImageDraw.Draw(img)
font = ImageFont.truetype(os.path.join("C:\Windows\Fonts\simfang.ttf"), 12)
idr.text((10, 5), text, font=font, fill="#000000")
img = img.resize((pxx,pxy))
img.save('out.png')
sys.exit()
