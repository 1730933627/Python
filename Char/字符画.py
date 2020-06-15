from PIL import Image
import sys

char_list = list("$WMB8Q0&D#CJUXY@6%4hkbdftoapqzcxrvun?1/~\[]{}()<>+l-i;:,_\"^`'.  ")

def get_char(r, g, b, alpha=255):
   if alpha == 0:
       return ' '
   length = len(char_list)
   gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
   unit = (256.0 + 1) / length
   return char_list[int(gray / unit)]
print("====================================================================")
print("=图片重命名为img，文本会保存到同目录后缀名为.txt，只支持jpg,png,bmp=")
print("====================================================================")

if __name__ == "__main__":
   try:
      width = int(eval(input("图片像素(X)：")) / 10)
      height = int(eval(input("图片像素(Y)：")) / 20)
      try:
         much = eval(input("缩放倍数(不加倍回车)："))
         if type(much)==type(1):
            width = width * much
            height = height * much
      except:
         pass
   except:
      height = 120
      width = 60
   try:
      img = Image.open("img.jpg")#图片路径
   except:
      try:
         img = Image.open("img.png")
      except:
         try:
            img = Image.open("img.bmp")
         except:
            with open("out.txt","w") as f:
               f.write("没有文件可以被打开")
               f.close()
   imgs = img.resize((width,height), Image.NEAREST)
   txt = ""
   for a in range(height):
       for b in range(width):
           txt += get_char(*imgs.getpixel((b, a)))
       txt += "\n"
   
   with open("out.txt","w") as f:
       f.write(txt)
       f.close()
sys.exit()
