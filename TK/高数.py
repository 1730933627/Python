import tkinter as tk
import sympy

# 生成主界面
window = tk.Tk()
window.title('高数计算器')
window.geometry('640x640')
window.geometry("640x640+450+90")
window.wm_resizable(False,False)
canvas1 = tk.Canvas(window,height = 340,width = 636)
canvas1.place(x = 0,y = 200)

#定义函数变量
x = sympy.Symbol('x')
y = sympy.Symbol('y')

def solve_equation(f1,f2):
    return sympy.solve([f1, f2], [x, y])

def solve_limit(f,x,num):
    return sympy.limit(f,x,num)

def solve_derivative(f,x):
    return sympy.diff(f,x)

def solve_partial_derivative(f,x,y):
    x1 = sympy.diff(f,x)
    y1 = sympy.diff(f,y)
    answer_text_pd_num.insert('insert', "对X求偏导："+"\n")
    answer_text_pd_num.insert('insert',x1)
    answer_text_pd_num.insert('insert',"\n"+"\n")
    answer_text_pd_num.insert('insert', "对Y求偏导："+"\n")
    answer_text_pd_num.insert('insert',y1)
    answer_text_pd_num.insert('insert',"\n"+"\n")

def solve_d_integral(f,x,down_num,up_num,):
    return sympy.integrate(f,(x,down_num,up_num))

def solve_b_d_integral(f,x):
    return sympy.integrate(f,x)

def hit():
    canvas1.place_forget()
    button_no.place_forget()
    button_yes.place_forget()
    button_fun.place(x = 20,y = 220)
    button_lim.place(x = 20,y = 280)
    button_der.place(x = 20,y = 340)
    button_par.place(x = 20,y = 400)
    button_itg.place(x = 20,y = 460)
    button_bitg.place(x = 20,y = 520)

#-------------方程组---------------
var = tk.StringVar
var1 = tk.StringVar
answer_text = tk.Text(window, height=12, width=42, font=12)
one = tk.Entry(window,width=25, borderwidth=3,font = 15)
two = tk.Entry(window, width=25, borderwidth=3,font = 12)
two_lable = tk.Label(window, text="方程2:", font=12)
one_lable = tk.Label(window,text = "方程1:",font = 12)
ans_lbale = tk.Label(window, text="Answer", font=12)
def func():
    answer_text.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    one.place(x = 270,y = 220)
    two.place(x=270, y=255)
    one_lable.place(x=200,y = 218)
    two_lable.place(x=200, y=253)
    button_ans.place(x= 548,y=236)
    del_fun.place(x=510, y=585)

def play():
    var = one.get()
    var1 = two.get()
    ans_f = solve_equation(var,var1)
    answer_text.insert('insert', "方程组的解为："+"\n")
    answer_text.insert('insert',ans_f)
    answer_text.insert('insert',"\n")

def del_f():
    answer_text.place_forget()
    ans_lbale.place_forget()
    one.place_forget()
    two.place_forget()
    one_lable.place_forget()
    two_lable.place_forget()
    button_ans.place_forget()
    del_fun.place_forget()
del_fun = tk.Button(window,text="点我换方法", font=12,command = del_f)
button_ans = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =play)
#-------------方程组---------------


#-------------求极限---------------
var_lim = tk.StringVar
var1_lim = tk.StringVar
lim_f = tk.Entry(window,width=25, borderwidth=3,font = 12)
lim_s = tk.Entry(window, width=25, borderwidth=3,font = 12)
lim_f_lable = tk.Label(window, text="函数:", font=12)
lim_s_lable = tk.Label(window,text = "趋向值:",font = 12)
answer_text_lim = tk.Text(window, height=12, width=42, font=12)
def lim():
    lim_f.place(x=275, y=220)
    lim_s.place(x=275, y=255)
    lim_f_lable.place(x=200, y=218)
    lim_s_lable.place(x=200, y=253)
    button_ans_lim.place(x=548, y=236)
    answer_text_lim.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    del_fun_lim.place(x=510, y=585)

def lim_play():
    var_lim = lim_f.get()
    var1_lim = (lim_s.get())
    if var1_lim =="oo":
        var1_lim = "oo"
    else:var1_lim = int(var1_lim)
    ans_lim = solve_limit(var_lim, x,var1_lim)
    answer_text_lim.insert('insert', "函数的极限为："+"\n")
    answer_text_lim.insert('insert', ans_lim)
    answer_text_lim.insert('insert', "\n")

def del_lim():
    lim_f.place_forget()
    lim_s.place_forget()
    lim_f_lable.place_forget()
    lim_s_lable.place_forget()
    button_ans_lim.place_forget()
    answer_text_lim.place_forget()
    ans_lbale.place_forget()
    del_fun_lim.place_forget()

del_fun_lim = tk.Button(window,text="点我换方法", font=12,command = del_lim)
button_ans_lim = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =lim_play)

#-------------方程组---------------


#-------------求导数---------------
var_d_num = tk.StringVar
d_num = tk.Entry(window,width=25, borderwidth=3,font = 12)
d_num_lable = tk.Label(window, text="函数:", font=12)
answer_text_d_num  = tk.Text(height=12, width=42, font=12)

def d_n():
    d_num.place(x=260, y=225)
    d_num_lable.place(x=200, y=225)
    answer_text_d_num.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    del_d_num.place(x=510, y=585)
    d_num_ans.place(x=548, y=220)

def play_d_num():
    var_d_num = d_num.get()
    ans_d = solve_derivative(var_d_num,x)
    answer_text_d_num.insert('insert', "求导后的函数为："+"\n")
    answer_text_d_num.insert('insert', ans_d)
    answer_text_d_num.insert('insert', "\n")

def del_ds_num():
    d_num.place_forget()
    d_num_lable.place_forget()
    answer_text_d_num.place_forget()
    ans_lbale.place_forget()
    del_d_num.place_forget()
    d_num_ans.place_forget()

del_d_num = tk.Button(window,text="点我换方法", font=12,command = del_ds_num)
d_num_ans = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =play_d_num)
#-------------求导数---------------


#-------------求偏导数---------------
var_pd_num = tk.StringVar
pd_num = tk.Entry(window,width=25, borderwidth=3,font = 12)
answer_text_pd_num  = tk.Text(window, height=12, width=42, font=12)

def pd_n():
    pd_num.place(x=260, y=225)
    d_num_lable.place(x=200, y=225)
    answer_text_pd_num.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    del_pd_num.place(x=510, y=585)
    pd_num_ans.place(x=548, y=220)

def play_pd_num():
    var_pd_num = pd_num.get()
    solve_partial_derivative(var_pd_num,x,y)

def del_pds_num():
    pd_num.place_forget()
    d_num_lable.place_forget()
    answer_text_pd_num.place_forget()
    ans_lbale.place_forget()
    del_pd_num.place_forget()
    pd_num_ans.place_forget()

del_pd_num = tk.Button(window,text="点我换方法", font=12,command = del_pds_num)
pd_num_ans = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =play_pd_num)
#-------------求偏导数---------------

#-------------求定积分---------------
var_din_num1 = tk.StringVar
var_din_num2 = tk.StringVar
var_din_num3 = tk.StringVar
din_fun = tk.Entry(window,width=25, borderwidth=3,font = 12)
din_up = tk.Entry(window,width=6, borderwidth=3,font = 12)
din_down = tk.Entry(window,width=6, borderwidth=3,font = 12)
answer_text_din = tk.Text(window, height=12, width=42, font=12)
din_lbale = tk.Label(window, text="函数:", font=12)
din_lbale_up = tk.Label(window, text="上标:", font=12)
din_lbale_down = tk.Label(window, text="下标:", font=12)

def din():
    din_fun.place(x=260, y=210)
    din_up.place(x=260, y=250)
    din_down.place(x=450, y=250)
    answer_text_din.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    din_lbale.place(x=200,y=210)
    din_lbale_up.place(x=200,y=250)
    din_lbale_down.place(x=380,y=250)
    del_din_num.place(x=510, y=585)
    din_num_ans.place(x=548, y=223)

def play_din():
    var_din_num1=din_fun.get()

    var_din_num2=int(din_up.get())
    var_din_num3=int(din_down.get())
    din_ans = solve_d_integral(var_din_num1,x,var_din_num3,var_din_num2)
    answer_text_din.insert("insert","定积分的结果为："+"\n")
    answer_text_din.insert("insert",din_ans)
    answer_text_din.insert("insert","\n")

def del_din():
    din_fun.place_forget()
    din_up.place_forget()
    din_down.place_forget()
    answer_text_din.place_forget()
    din_lbale_up.place_forget()
    din_lbale_down.place_forget()
    del_din_num.place_forget()
    din_num_ans.place_forget()
    ans_lbale.place_forget()
    din_lbale.place_forget()

del_din_num = tk.Button(window,text="点我换方法", font=12,command = del_din)
din_num_ans = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =play_din)
#-------------求定积分---------------


#-------------求不定积分---------------

var_bdin = tk.StringVar
bdin = tk.Entry(window,width=25, borderwidth=3,font = 12)
bdin_lable = tk.Label(window, text="函数:", font=12)
answer_text_bdin = tk.Text(window, height=12, width=42, font=12)

def b_din():
    bdin.place(x=260, y=225)
    bdin_lable.place(x=200, y=225)
    answer_text_bdin.place(x=200, y=315)
    ans_lbale.place(x=200, y=285)
    del_bdin_num.place(x=510, y=585)
    bdin_num_ans.place(x=548, y=220)

def play_bdin():
    var_bdin = bdin.get()
    bdin_ans = solve_b_d_integral(var_bdin,x)
    answer_text_bdin.insert("insert","求不定积分的结果为："+"\n")
    answer_text_bdin.insert("insert",bdin_ans)
    answer_text_bdin.insert("insert","\n")
def del_bdin():
    bdin.place_forget()
    bdin_lable.place_forget()
    answer_text_bdin.place_forget()
    ans_lbale.place_forget()
    del_bdin_num.place_forget()
    bdin_num_ans.place_forget()


del_bdin_num = tk.Button(window,text="点我换方法", font=12,command = del_bdin)
bdin_num_ans = tk.Button(window,text = "点我计算",bd = 1,font = ("Microsoft YaHei",12),activebackground = 'Light green',command =play_bdin)
#-------------求不定积分---------------

no = tk.Entry(window)
button_no = tk.Button(window,text = "NO",width = 10,height = 2,command=window.quit,
                      activebackground = 'red',font =("arial",12),bd = 3)
button_no.place(x = 100,y = 565)

button_yes = tk.Button(window,text = "YES",width = 10,height = 2,
                       activebackground = 'Light green' ,font =("arial",12),bd = 3,command = hit)
button_yes.place(x = 445,y = 565)



button_fun = tk.Button(window,text = "解方程",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command = func)
button_lim = tk.Button(window,text = "求极限",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command = lim)
button_der = tk.Button(window,text = "求导数",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command = d_n)
button_par = tk.Button(window,text = "求偏导",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command = pd_n)
button_itg = tk.Button(window,text = "求定积分",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command = din)
button_bitg = tk.Button(window,text = "求不定积分",font =("Microsoft YaHei",12),activebackground = 'Light green',bg="#fc9d9a",command =b_din)

window.mainloop()

