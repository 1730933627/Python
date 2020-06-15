from tkinter import *

def method():
    bv = bvr.get()
    txt=""
    dicta = {"1":13,"2":12,"3":46,"4":31,"5":43,"6":18,"7":40,"8":28,"9":5,\
             "A":54,"B":20,"C":15,"D":8,"E":39,"F":57,"G":45,"H":36,"J":38,"K":51,"L":42,"M":49,\
             "N":52,"P":53,"Q":7,"R":4,"S":9,"T":50,"U":10,"V":44,"W":34,"X":6,"Y":25,"Z":1,\
             "a":26,"b":9,"c":56,"d":3,"e":24,"f":0,"g":47,"h":27,"i":22,"j":41,"k":16,"m":11,"n":37,\
             "o":2,"p":35,"q":21,"r":17,"s":33,"t":30,"u":48,"v":23,"w":55,"x":32,"y":14,"z":19}
    lista = [bv[2],bv[3],bv[4],bv[5],bv[6],bv[7],bv[8],bv[9],bv[10],bv[11]]
    listb=[pow(58,6),pow(58,2),pow(58,4),pow(58,8),pow(58,5),pow(58,9),pow(58,3),pow(58,7),58,1]
    listc=[]
    count=0
    for i in lista:
        listc += [dicta[i]*listb[count]]
        count += 1
    temp = sum(listc) - 100618342136696320
    temp = temp ^ 177451812
    news.insert(0,"av{}".format(temp))

if __name__ == "__main__":
    root = Tk()
    root.title("BV号转AV号-Yan_Lin")
    lone = Label(root,text="输入BV号")
    lone.grid(row=0,column=0,padx=2,pady=3)  
    ltwo = Label(root,text="此AV号为")
    ltwo.grid(row=1,column=0,padx=2,pady=3)
    bvr = Entry(root,bd = 1)
    bvr.grid(row=0,column=1)
    news = Entry(root,bd = 1)
    news.grid(row=1,column=1)
    but = Button(root,text="计算",width=10,command=method)
    but.grid(row=0,column=2,padx=5,pady=5)
    butt = Button(root,text="退出",width=10,command=root.quit)
    butt.grid(row=1,column=2,padx=5,pady=5)
    root.mainloop()
