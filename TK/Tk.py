from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
ver = StringVar()
on_hit = False

def print_a():
    print("やみの ほうのに だかれでけいぇる！")

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        ver.set("かわいい")
    else:
        on_hit = False
        ver.set("ばが")

button = Button(root,text="へい",command=hit_me,width=8,height=1)
button.pack()

lable = Label(root,textvariable=ver,width=15,height=2)
lable.pack()
root.mainloop()                 # 进入消息循环
