from tkinter import *
import sys


root = Tk()
root.title('')

var_name = StringVar()
var_pwd =  StringVar()

get_name = var_name.get()
get_pwd = var_pwd.get()

width=280
height=120

def login():
    pass


def sign_up():
    pass


screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)

l1=Label(root,text='账号:',padx=7,pady=5).grid(row=0,column=0)
l2=Label(root,text='密码:',padx=7,pady=5).grid(row=1,column=0)

e1=Entry(root,textvariable=var_name)
e2=Entry(root,show='*',textvariable=var_pwd)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(root,text='注册',width=10,height=2,command=sign_up).grid(row=1,column=2,padx=5,pady=5)
Button(root,text='登录',width=10,height=2,command=login).grid(row=0,column=2,padx=5,pady=5)

root.mainloop()