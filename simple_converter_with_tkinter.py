# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:57:49 2020

@author: Santosh Rajkumar
"""

from tkinter import *

#initialize window

window = Tk()

def kg_conv():
    gram = float(e1_value.get())*1000
    pound = float(e1_value.get())*2.20462
    ounce = float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, str(gram)+ ' grams')
    t2.delete("1.0", END)
    t2.insert(END, str(pound) + ' pounds')
    t3.delete("1.0", END)
    t3.insert(END, str(ounce) + ' ounces')
  


b1 = Button(window, text='Convert', command= kg_conv)
b1.grid(row=0, column=2, rowspan = 1)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2 = Label(window, text = 'Enter in Kgs')
e2.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)




#end of code
window.mainloop()
