import sqlite3
from tkinter import *
import os
import hashlib

window = Tk()
window.title("Connection to UFIX")
window.geometry('200x200')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 400
height = 200
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)
Ilog = StringVar()
Ipass = StringVar()
Forms = Frame(window, width=200, height=200)
Forms.pack(side=TOP)
txt_ilog = Label(Forms, text="Log:", font=('arial', 16), bd=15)
txt_ilog.grid(row=0, stick="e")
txt_ipass = Label(Forms, text="Password:", font=('arial', 16), bd=15)
txt_ipass.grid(row=1, stick="e")
ilog = Entry(Forms, textvariable=Ilog, width=30)
ilog.grid(row=0, column=1)
ipass = Entry(Forms, textvariable=Ipass, width=30)
ipass.grid(row=1, column=1)

def Database():
    global conn, cursor
    conn = sqlite3.connect("Ufixltd.s3db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Employee` (idEmployee INTEGER PRIMARY KEY  AUTOINCREMENT ,firstNameEmployee	VARCHAR ( 50 ),lastNameEmployee	VARCHAR ( 50 ),emailEmployee	VARCHAR ( 50 ),phoneEmployee	VARCHAR ( 20 ),idTeam	VARCHAR(50),log	VARCHAR(50),pass    VARCHAR(50))")

def conc():
    Database()
    cursor.execute("select pass From `Employee` WHERE  log = '" + Ilog.get() + "'")
    fetch = cursor.fetchone()
    if not fetch:
        print("not log")
    else:
        fetch = fetch[0]
        mdp = Ipass.get()
        mdp = mdp.encode()
        if fetch == hashlib.sha1(mdp).hexdigest():
            window.destroy()
            os.system("welcomePage.py")
        else:
            print("wrong pass")

    Ipass.set("")
    Ilog.set("")
    cursor.close()
    conn.close()

button = Button(window, text="conn", width=20,command=conc)
button.pack()
#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    window.mainloop()