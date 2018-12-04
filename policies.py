from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"Policies.pdf")

root = Tk()
link = Label(root, text="Policy Document Link", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()
