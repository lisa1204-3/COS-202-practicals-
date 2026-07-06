#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
from tkinter import *

# ==========================
# MATHEMATICAL CALCULATOR
# ==========================

root = Tk()
root.title("Mathematical Calculator")
root.geometry("350x500")
root.configure(bg="lightblue")
root.resizable(False, False)

Label(root,
      text="MATHEMATICAL CALCULATOR",
      font=("Arial", 16, "bold"),
      bg="lightblue").pack(pady=10)

entry = Entry(root,
              font=("Arial", 22),
              bd=8,
              relief=RIDGE,
              justify="right")

entry.pack(fill=X, padx=15, pady=10)


# ==========================
# FUNCTIONS
# ==========================

def press(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def equal():
    try:
        expression = entry.get().replace("^", "**")
        answer = eval(expression)
        entry.delete(0, END)
        entry.insert(0, answer)

    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Cannot Divide by Zero")

    except:
        entry.delete(0, END)
        entry.insert(0, "Invalid Input")

def off():
    root.destroy()


# ==========================
# BUTTON FRAME
# ==========================

frame = Frame(root, bg="lightblue")
frame.pack()

buttons = [

["7","8","9","/"],
["4","5","6","*"],
["1","2","3","-"],
["0",".","%","+"],
["^","⌫","C","="],
["OFF"]

]

for r in range(len(buttons)):
    for c in range(len(buttons[r])):

        text = buttons[r][c]

        if text == "=":
            Button(frame,text=text,width=8,height=3,bg="lightgreen",
                   command=equal).grid(row=r,column=c,padx=2,pady=2)

        elif text == "C":
            Button(frame,text=text,width=8,height=3,bg="orange",
                   command=clear).grid(row=r,column=c,padx=2,pady=2)

        elif text == "⌫":
            Button(frame,text=text,width=8,height=3,bg="yellow",
                   command=backspace).grid(row=r,column=c,padx=2,pady=2)

        elif text == "OFF":
            Button(frame,text=text,width=35,height=2,bg="red",
                   fg="white",command=off).grid(row=r,column=0,
                   columnspan=4,pady=8)

        else:
            Button(frame,text=text,width=8,height=3,
                   command=lambda t=text: press(t)
                   ).grid(row=r,column=c,padx=2,pady=2)

root.mainloop()