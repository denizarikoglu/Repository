import json
import sqlite3
import webbrowser
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

#==================================VARIABLES==========================================
Ilog = StringVar()
Ipass = StringVar()
idEm = StringVar()
var = StringVar()

#==================================FRAME==============================================
Forms = Frame(window, width=200, height=150)
Forms.pack(side=TOP)
Message = Frame(window, width=200, height=50)
Message.pack()

#==================================LABEL WIDGET========================================
txt_ilog = Label(Forms, text="Log:", font=('arial', 16), bd=15)
txt_ilog.grid(row=0, stick="e")
txt_ipass = Label(Forms, text="Password:", font=('arial', 16), bd=15)
txt_ipass.grid(row=1, stick="e")
ErrorLabel = Label(Message, textvariable=var, fg="red")
ErrorLabel.pack()

#==================================ENTRY WIDGET=======================================
ilog = Entry(Forms, textvariable=Ilog, width=30)
ilog.grid(row=0, column=1)
ipass = Entry(Forms, show="*", textvariable=Ipass, width=30)
ipass.grid(row=1, column=1)

def Database():
    global conn, cursor
    conn = sqlite3.connect("Ufixltd.s3db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Employee` (idEmployee INTEGER PRIMARY KEY  AUTOINCREMENT ,firstNameEmployee	VARCHAR ( 50 ),lastNameEmployee	VARCHAR ( 50 ),emailEmployee	VARCHAR ( 50 ),phoneEmployee	VARCHAR ( 20 ),idTeam	VARCHAR(50),log	VARCHAR(50),pass    VARCHAR(50),connect    INTEGER)")

def conc():
    Database()
    cursor.execute("select pass From `Employee` WHERE  log = '" + Ilog.get() + "'")
    fetch = cursor.fetchone()
    if not fetch:
        var.set("Not LOG")
    else:
        fetch = fetch[0]
        mdp = Ipass.get()
        mdp = mdp.encode()
        if fetch == hashlib.sha1(mdp).hexdigest():
            cursor.execute("select idEmployee From `Employee` WHERE  log = '" + Ilog.get() + "'")
            id = cursor.fetchone()
            idEm.set(id[0])
            cursor.execute("select connect From `Employee` WHERE  idEmployee = '" + idEm.get() + "'")
            connect = cursor.fetchone()
            connect = connect[0]
            if connect == 0:
                letter()
            cursor.execute("UPDATE `Employee` set connect = connect+1 WHERE  idEmployee = '" + idEm.get() + "'")
            conn.commit()
            data = {"user": idEm.get()}
            with open("data_file.json", "w") as write_file:
                json.dump(data, write_file)
            window.destroy()
            os.system("policies.py")
            os.system("welcomePage.py")
        else:
            var.set("WRONG PASSWORD")
    conn.commit()
    Ipass.set("")
    Ilog.set("")
    conn.close()
def letter():
    webbrowser.open_new(r"Policies\Welcome letter.pdf")


#==================================BUTTONS WIDGET=====================================
button = Button(window, text="conn", width=20,command=conc)
button.pack()
#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    window.mainloop()
