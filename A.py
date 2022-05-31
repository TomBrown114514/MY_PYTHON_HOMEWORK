import tkinter as tk
win=tk.Tk()
win.title("查看消息")
win.geometry("320x300")

a=[1]
b=""

def pa():
    mes1.config(text=a) #pc里若是写成“a=[]”则仍会显示初始赋值(a内被赋两个了两个值 )
                        #但若使用内置函数则会删除初始值
def pb():
    mes1.config(text=b)
def pc():
    a.pop()             #a=[]不同效果，重新赋值与使用内置函数更改的效果不同
    mes1.config(text=a)
def pd():
    win.destroy()

but1=tk.Button(win,text="展开",command=pa)
but1.grid(row=0,column=0)
but1=tk.Button(win,text="收起",command=pb)
but1.grid(row=0,column=1)
but1=tk.Button(win,text="删除",command=pc)
but1.grid(row=0,column=2)
but1=tk.Button(win,text="退出",command=pd)
but1.grid(row=0,column=3)
mes1=tk.Message(win,text=b)
mes1.grid(row=1,column=0,columnspan=4)

win.mainloop() 