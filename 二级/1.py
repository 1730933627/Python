#"""①"""#

x = pow((3**4 + 5*(6**7))/8, 0.5)
print("{:.3f}".format(x))

""""""

import jieba
s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{}，中文词语数为{}。".format(n, m))

""""""

print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))

""""""

import turtle
d = 0
for i in range(4):
    turtle.fd(200)
    d = d + 90
    turtle.seth(d)

print(4, 200, 'd + 90')

""""""

ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", \
      "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合", \
      "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范", \
      "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合", \
      "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
d = {}
for word in ls:
    d[word] = d.get(word, 0) + 1
for k in d:
    print("{}:{}".format(k, d[k]))

""""""

fi = open("论语-网络版.txt", "r", encoding="utf-8")
fo = open("论语-提取版.txt", "w")
wflag = False            #写标记
for line in fi:
    if "【" in line:     #遇到【时，说明已经到了新的区域，写标记置否
        wflag = False
    if "【原文】" in line:  #遇到【原文】时，设置写标记为True
        wflag = True
        continue
    if wflag == True:    #根据写标记将当前行内容写入新的文件
        for i in range(0,25):
            for j in range(0,25):
                line = line.replace("{}·{}".format(i,j),"**")
        for i in range(0,10):
            line = line.replace("*{}".format(i),"")
        for i in range(0,10):
            line = line.replace("{}*".format(i),"")
        line = line.replace("*","")
        fo.write(line)
fi.close()
fo.close()

""

fi = open("论语-提取版.txt", "r")
fo = open("论语-原文.txt", "w")
for line in fi:   #逐行遍历
    for i in range(1,23):  #对产生1到22数字
        line=line.replace("({})".format(i), "")  #构造(i)并替换
    fo.write(line)
fi.close()
fo.close()


#"""②"""#


N = eval(input())   # N取值范围是0—100，整数
print("{:>3}%@{}".format(N,"="*(N//5)))

""""""

s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
n = 0  # 汉字个数
m = 0  # 标点符号个数
m = s.count(',') + s.count('?')
n = len(s) - m
print("字符数为{}，标点符号数为{}。".format(n, m))

""""""

N = input("请输入一个整数：")
s=0
for i in range(eval(N),eval(N)+100):
    if i%2==1:
        s += i
print(s)

""""""

import turtle as t
for i in range(6):
    t.fd(200)
    t.left(60)

""""""

def getInput():
    try:
        txt = input()   # "请输入整数: "
        while eval(txt) != int(txt):
            txt = input()   # "请输入整数: "
    except:
        return getInput()
    return eval(txt)
print(getInput())

""""""
fi = open("天龙八部-网络版.txt", "r", encoding='utf-8')
fo = open("天龙八部-汉字统计.txt", "w", encoding='utf-8')
txt = fi.read()
d = {}
for c in txt:
    d[c] = d.get(c, 0) + 1
del d[' ']
del d['\n']
ls = []
for key in d:
    ls.append("{}:{}".format(key, d[key]))
fo.write(",".join(ls))
fi.close()
fo.close()


#"""③"""#


s = input()  # "请输入一个字符串:"
print("{:=^15}".format(s[0:15]))

""""""

a, b = 0, 1
while a<=100:
    print(a, end=',')
    a, b = b, a + b

""""""

import time
timestr = "2020-10-10 10:10:10"
t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y年%m月%d日%H时%M分%S秒", t))

""""""

import turtle as t
for i in range(3):
    t.seth(i * 120)
    t.fd(200)

""""""

d = {"数学":101, "语文":202, "英语":203, "物理":204, "生物":206}
d["化学"] = 205
d["数学"] = 201
del d["生物"]
for key in d:
    print("{}:{}".format(d[key], key))

""""""

import random
random.seed(0x1010)
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
ls = []
excludes = ""
while len(ls) < 10:
    pwd = ""
    for i in range(10):
        pwd += s[random.randint(0, len(s)-1)]
    if pwd[0] in excludes:
        continue
    else:
        ls.append(pwd)
        excludes += pwd[0]

# 直接打印
print("\n".join(ls))

# 或写入文件
fo = open("随机密码.txt", "w")
fo.write("\n".join(ls))
fo.close()


#"""④"""#


n = input()  # 请输入整数
print("{:->20,}".format(eval(n)))

""""""

print("pyinstaller –i a.ico –F a.py")

""""""

import random
random.seed(123)
for i in range(10):
    print(random.randint(1,999), end=",")

""""""

import turtle as t
t.right(-30)
for i in range(2):
    t.fd(200)
    t.right(60*(i+1))
for i in range(2):
    t.fd(200)
    t.right(60*(i+1))

""""""

a = [[1,2,3], [4,5,6], [7,8,9]]
b = [3,6,9]
s = 0
for c in a:
    for j in range(3):
        s += c[j]*b[j]
print(s)

""""""

names = ["命运", "寻梦"]
for name in names:
    fi = open(name+"-网络版.txt", "r", encoding="utf-8")
    fo = open(name+"-字符统计.txt", "w", encoding="utf-8")
    txt = fi.read()
    d = {}
    for c in txt:
        d[c] = d.get(c, 0) + 1
    del d['\n']
    ls = list(d.items())
    ls.sort(key=lambda x:x[1], reverse=True)
    for i in range(100):
        ls[i] = "{}:{}".format(ls[i][0], ls[i][1])
    fo.write(",".join(ls[:100]))
    fi.close()
    fo.close()


#""""⑤"""#


n = input("")
nums = n.split(",")
s = 0
for i in nums:
    s += eval(i)
print(s)

""""""

def GreatCommonDivisor(a,b):
    if a > b:
        a,b = b,a
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a
m = eval(input())
n = eval(input())
print(GreatCommonDivisor(m,n))

""""""

import jieba
s = "世界冠军运动员的乒乓球拍卖完了"
ls = jieba.lcut(s,True)
print(ls)

""""""

import turtle as t
for i in range(4):
    t.seth(90 * (i + 1))
    #90,180,270，360
    t.circle(200,90)
    #-90,0,90,180
    t.seth(-90 + i * 90)
    t.circle(200,90)

""""""

def is_prime(n):
    for i in range(2,n):   #此处可为多行函数定义代码
        if i % 2==0:
            return False
        return True
ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i)== True:
        ls.remove(i)   #此处为一行代码
print(len(ls))

""""""

#读入CSV格式数据到列表中
fo = open("SunSign.csv","r", encoding='utf-8')
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()

while True:
    InputStr = input() # 请输入星座名称,例如双子座
    InputStr.strip()
    flag = False
    if InputStr == 'exit':
        break
    for line in ls:
        if InputStr == line[0]:
             print("{}座的生日位于{}-{}之间。".format(chr(eval(line[3])),line[1],line[2]))
             flag = True
    if flag == False:
        print("输入星座名称有误！")


#"""⑥""" #


#请输入一个汉字
s = input("")
print("\"{}\"汉字的Unicode编码：{}".format(s,ord(s)))

""""""

#请输入第一个正整数：
#请输入第一个正整数：
def gcd(x,y):
    if x < y:
        x,y = y,x
    while x % y != 0:
        r = x % y
        x = y
        y = r
    return y
a = eval(input(""))
b = eval(input(""))
gcdab = gcd(a,b)
print("{}与{}的最大公约数是{}".format(a,b,gcd(a,b)))

""""""

def mean(numlist):
    s = 0.0
    for num in numlist:
        s = s + num
    return s/len(numlist)
#请输入一个列表：
ls = eval(input(""))
print("平均值为：",mean(ls))

""""""

#import turtle
#for i in range(4):
#    turtle.right(90)
#    turtle.circle(50,180)
print(4,90,180)

""""""

# 从1.csv文件中读取考勤数据
with open("1.csv","r",encoding = "utf-8") as fo:
    foR =fo.readlines()
ls = []
for line in foR:
    line = line.replace("\n","")
    ls.append(line.split(","))

# 从name.txt文件中读取所有同学的名单
with open("Name.txt","r",encoding = "utf-8") as foName:
    foNameR = foName.readlines()
lsAll = []
for line in foNameR:
    line = line.replace("\n","")
    lsAll.append(line)

#求出第一次缺勤同学的名单
for l in ls:
    if l[0] in lsAll:
        lsAll.remove(l[0])

#print("第一次缺勤同学有：",end ="")
for l in lsAll:
    print(l,end=" ")

""""""

import jieba
with open("sgld.txt","r",encoding ="utf-8")as f:
    lssgld = f.readlines()
n = 0
for ls in lssgld:
    wordlist = jieba.cut(ls)
    for word in wordlist:
        if "人" in word:
            n = n + 1
print("人:" + str(n) + "次")