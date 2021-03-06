#图形界面---Tkinter

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()  #把Widget加入到父容器中，并实现布局。
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
        # self.helloLabel=Label(self,text='Hello,world!')
        # self.helloLabel.pack()
        # self.quitButton=Button(self,text='Quit',command=self.quit)
        # self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'% name)

app=Application()

# 设置窗口标题
app.master.title('hello,world')
#主消息循环
app.mainloop()
