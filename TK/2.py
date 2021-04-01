from tkinter import *
root = Tk()
root.title("666666666666")
label = Label(
    bg = '#F0FFFF',
    width=60,height=20
    )
var = ""
def me():
    on_hit = False
    if on_hif == False:
        on_hif == True
        var.set('哈哈哈')
    else:
        on_hif ==False
        var.set('')

button = Button(
    text=var,
    bg = '#00FFFF',
    width=20,height=4,
    command=me
    )
label.pack()
button.pack()
root.mainloop()
