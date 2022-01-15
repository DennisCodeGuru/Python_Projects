import tkinter as tk
from tkinter import *
import webbrowser
  




def clicked():
    usertext = txt.get()
    htmlcode = "<html><body><h1>"+ usertext +"</h1></body></html>"
    f = open('test.html','w')
    f.write(htmlcode) 
    f.close()     
    webbrowser.open_new_tab('test.html')  
  
window = Tk()  
window.title("Wellcome Python")  
window.geometry('400x250')  
lbl = Label(window, text="Hello: ")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Submit!", command=clicked)  
btn.grid(column=2, row=0)  
window.mainloop()
