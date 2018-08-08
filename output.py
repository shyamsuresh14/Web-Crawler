from tkinter import Grid, Label, Button, Tk, Entry
from crawler import main

def Print(op,e,e2):
        e.grid(row=0,column=1)
        e2.grid(row=1,column=1)
        label = Label(op,text = "Enter the base URL:")
        label2 = Label(op,text = "Enter the Keyword:")
        label.grid(row=0,column=0)
        label2.grid(row=1,column=0)
        b1 = Button(text = "Crawl",fg = "green",command = GET)
        #b2 = Button(text="Stop",fg = "red",command = END)
        b1.grid(row = 3,column=0,columnspan =2)
        #b2.grid(row = 4, column=0, columnspan =2)
                
                
Op = Tk()
Op.title("Web Crawler")
#Op.geometry("500x500")

def GET():
        main(e.get(),e2.get())
        
e=Entry(Op)
e2=Entry(Op)
Print(Op,e,e2)

