class New:
    def hi():                       #打招呼
        print("Hello World")
    def tupian():                   #框架
        import tkinter         
        from PIL import Image, ImageTk  
        root = tkinter.Tk()
        root.title('')
        canvas = tkinter.Canvas(root,  
            width = 1920,
            height = 1080,
            bg = 'white')  
        image = Image.open(".Img\1.jpg")  
        im = ImageTk.PhotoImage(image)
        
        canvas.create_image(960,540,image = im)
        canvas.create_text(95,77,
                           text = "稽智的琰凛"
                           ,fill = 'gray')
        canvas.pack() 
        root.mainloop()  
    def jiujiu():                   #九九乘法表
        for a in range(1,10):
            for b in range(1,a+1):
                print('{}*{}={}\t'.format(b,a,a*b),end='')
            print()
    def caishu():                   #猜数游戏
        import random
        i = 1
        a = random.randint(0,20)
        b = int( input('请输入0-20中的一个数字\n然后看看是否与我想的一样：'))
        while a != b:
            if a > b:
                print('你第%d输入的数字小于我想的数字'%i)
                b = int(input('请再次输入一次:'))
            else:
                print('你第%d输入的数字大于我想的数字'%i)
                b = int(input('请再次输入一次:'))
            i+=1
        else:
            print('恭喜你，你第%d次输入的数字与我想的数字%d一样'%(i,b))
    def jinzhi():                   #进制转换
        num = int(input("输入数字："))
        print("十进制数为：", num,"(D)")
        print("转换为二进制为：", bin(num),"(B)")
        print("转换为八进制为：", oct(num),"(O)")
        print("转换为十六进制为：", hex(num),"(H)")
    def runnian():                  #闰年判断
        year = int(input("请输入一个年份："))
        if (year % 4)== 0:
            if(year % 100)== 0:
                if(year % 400)== 0:
                    print("{0}是闰年".format(year))
                else:
                    print("{0} 不是闰年".format(year))
            else:
                print("{0} 是闰年".format(year))
        else:
            print("{0} 不是闰年".format(year))        
    def ip():                       #IP地址
        import socket
        import uuid

        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        def get_mac_address():
            mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
            return ":".join([mac[e:e+2] for e in range(0,11,2)])
        print("IP:"+ip)
        print("计算机名："+hostname)
        print("Mac地址："+get_mac_address())
