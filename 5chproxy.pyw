from cefpython3 import cefpython as cef
import platform
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def main():
  
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://z5h64q92x9.net/proxy_u/ja-ru.en/www2.5ch.net/5ch.html",
                          window_title="Welcome to 5Ch.net!")
    cef.MessageLoop()
    cef.Shutdown()
   

top=tkinter.Tk()
top.configure(background='navajo white')
top.geometry("200x100")
top.title('5Ch.net')
opener=tkinter.Button(top,text="Open 5Ch.net",width=25,height=5,command=main)
opener.pack(side=TOP)

top.mainloop()