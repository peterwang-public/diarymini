from tkinter import *
from tkinter import ttk
import os
import sys
import datetime

if hasattr(sys, 'frozen'):
    path = os.path.dirname(sys.executable)
elif __file__:
    path=os.path.dirname(os.path.abspath(__file__))
file_dir=os.path.join(path,'diarymini_data')
def setup():
    try:
        os.mkdir(file_dir)
    except:
        pass
main = Tk()
s_w = int(main.winfo_screenwidth())
s_h = int(main.winfo_screenheight())
setup()

global te1,c_b
def ref():
    global names
    names = os.listdir(file_dir)
def wind(width,height):
    pl_x = int((s_w-width)/2)
    pl_y = int((s_h-height)/2)
    return f"{width}x{height}+{pl_x}+{pl_y}"
def bg_open():
    cishu = 0
    t7 = Toplevel(main)
    t7.title("日记报告")
    t7.geometry(wind(500,500))
    ref()
    time_m = int(datetime.datetime.now().strftime("%m"))
    for i in names:
        li1 = i.split("-")
        if int(li1[1]) == time_m:
            cishu += 1
    l4 = Label(t7, text="一共写了" + str(len(names)) + "篇日记,这个月写了" + str(cishu) + "次日记").pack()
    c_b = Button(t7, text="关闭",command=t7.destroy).pack()
def compl():
    t4 = Toplevel(main)
    t4.title("Diary Result")
    t4.geometry(wind(250,200))
    l2 = Label(t4,text='保存成功',font=("Arial", 25)).pack()
    c_b = Button(t4, text="关闭",command=t4.destroy).pack()
def save_c():
    content = te1.get('1.0', 'end-1c')
    time = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    file_path=os.path.join(file_dir,time+".txt")
    f = open(file_path,"a")
    f.write(content)
    f.close()
    compl()
    t2.destroy()
def save_o():
    global te2
    content = te2.get('1.0', 'end-1c')
    file_path=os.path.join(file_dir,f_n)
    f = open(file_path,"w")
    f.write(content)
    f.close()
    compl()
def create():
    global t2,te1
    t2 = Toplevel(main)
    t2.title("Diary Create")
    t2.geometry(wind(500,500))
    te1 = Text(t2,height=30,width=500)
    te1.pack()
    te1.insert(1.0, "今日天气<晴/阴/雨/多云/雪>   今日心情<开心/难过/一般/生气>\n请输入日记")
    b4 = Button(t2, text="保存", command=save_c).pack()
    c_b = Button(t2, text="关闭",command=t2.destroy).pack()
def get_open():
    global te2,f_n
    f_n = c1.get()
    file_path=os.path.join(file_dir,f_n)
    f = open(file_path,"r")
    cont = f.read()
    f.close()
    t5 = Toplevel(main)
    t5.title("Diary open/change")
    t5.geometry(wind(500,500))
    te2 = Text(t5,height=30,width=500)
    te2.pack()
    b6 = Button(t5, text="保存", command=save_o).pack()
    te2.insert(1.0,cont)
    c_b = Button(t5, text="关闭",command=t5.destroy).pack()
def open_f():
    global t3,c1
    ref()
    if len(names) == 0:
            t8 = Toplevel(main)
            t8.geometry(wind(250,200))
            t8.title("没有创建")
            l5 = Label(t8, text="还没有创建文件哦").pack()
            c_b = Button(t8, text="关闭",command=t8.destroy).pack()
            return None
    t3 = Toplevel(main)
    t3.title("Diary open")
    t3.geometry(wind(250,200))
    ref()
    names1=sorted(names,reverse=True)
    names2=tuple(names1)
    c1 = ttk.Combobox(t3,values=names2)
    c1.pack()
    c1.current(0)
    b5 = Button(t3,text="确认",command=get_open).pack()
    c_b = Button(t3, text="关闭",command=t3.destroy).pack()
def choose():
    global t1
    t1 = Toplevel(main)
    t1.title("Diary Option")
    t1.geometry(wind(250,200))
    t1.resizable(0, 0)
    b2 = Button(t1, text="创建日记", command=create)
    b2.pack()
    b3 = Button(t1, text="查看日记", command=open_f)
    b3.pack()
    b7 = Button(t1, text="日记报告",command=bg_open)
    b7.pack()
    c_b = Button(t1, text="关闭",command=t1.destroy).pack()
    

main.title("Diary Mini")
main.geometry(wind(500,500))
main.resizable(0,0)
l1 = Label(main, text="Diary Mini", font=("Arial", 50))
l1.pack()
b1 = Button(main, text="开始",command=choose)
b1.pack()
b2 = Button(main, text="明天再写",command=main.destroy).pack()
main.mainloop()