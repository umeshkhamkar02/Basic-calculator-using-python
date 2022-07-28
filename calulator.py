from tkinter import *

def click(event):
    global scvalue #global variable
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("450x780")
root.resizable(False,False)
photo = PhotoImage(file = "calculate.png")
root.iconphoto(False, photo)
root.title("Calculator By Umesh Khamkar")



scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="white")
b = Button(f, text="9", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="white")
b = Button(f, text="6", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="white")
b = Button(f, text="3", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="white")
b = Button(f, text="0", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="white")
b = Button(f, text="/", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=22, pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=22, pady=12, font="lucida 35 bold", bg = "#e07945", fg = "white")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="white")
b = Button(f, text="=", padx=180, pady=12, font="lucida 35 bold",bg = "#888c98", fg = "white")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()