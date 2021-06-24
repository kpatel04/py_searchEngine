# Python code for search engine


#import youtube_dl
import urllib
import shutil
import webbrowser
import tkinter
from tkinter import filedialog
from tkinter import *
import webbrowser
from googlesearch import search
root=Tk()
root.geometry("600x125")
root.title('Py Search Engine')
root.configure(bg='#a5b886')
L1=Label(root,text='Enter Search Text Below',bg='#a5b886',fg='#ffffff',font=("times",20))
e=Entry(root,width=80,bg="white",fg="#0000ff",border=10)
def pas():
    for j in search(e.get(), tld='com', lang='en', num=5, stop=5):
        #webbrowser.open(j)
        print(j)

mybutton=Button(root,text="Search",bg='#cb464e',fg='#fff1c9',command=pas,font=("times",20))
L1.grid(row=0,column=0)
e.grid(row=1,column=0)
mybutton.grid(row=1,column=1)
root.mainloop()