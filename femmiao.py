from tkinter import *
from tkinter.messagebox import *


def min_to_second():
    try:
        minute = int(a.get())
        second = minute * 60
        showinfo("info",f"{minute}分钟={second:02d}秒" if second < 100 else f"{minute}分钟={second // 100}分{second % 100}秒")
    except Exception as e:
        showwarning("info","请输入正确的秒数")


win = Tk()
Label(win, text="请输入分钟数").pack()
a = Entry(win)
a.pack()
Button(win,text="转换",command=min_to_second).pack()
win.mainloop()
