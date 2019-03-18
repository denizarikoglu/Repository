from tkinter import*
import sqlite3
import os
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox



root = Tk()
root.title("Dispinary : Add new action")  # name for the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 300
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def Database_Users(): #gets all users from the database
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UFIX_PIM")


def Login():
    global txtname
    global txtPass
    print("login")
    user_Name = []  # used to hold all the names
    user_pass = []  #usedf to hold all passwords
    Database_Users()
    results = cursor.fetchall()
    for row in results:
        user_Name.append(row[10])
        user_pass.append(row[11])
    # print (row[0])
    cursor.close()  # closes database conection
    conn.close()
    if ((txtname.get("1.0", "end-1c")) in (user_Name)) and  ((txtPass.get("1.0", "end-1c")) in (user_pass)):
        root.destroy()
        os.system('Gui.py')
    else:
        tkMessageBox.showinfo("Bad login", "incorect login details")
def show_policy():
    os.system('poilcy.py')

Top = Frame(root, width=290, height=390, bd=8, relief="raise")
Top.pack(side=TOP)


labName = Label(Top,font=('arial', 12),text="User Name")
labName.pack(side=TOP)
txtname = Text(Top,width=30, height=1 ) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtname.pack(side=TOP)

labPass = Label(Top,font=('arial', 12),text="Password")
labPass.pack(side=TOP)
txtPass = Text(Top,width=30, height=1 ) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtPass.pack(side=TOP)

btnLogin = Button(Top, width=15, text="Login", command=Login)#should show up on bottom frame but dosnet
btnLogin.pack(side=BOTTOM)

btnpolicy = Button(Top, width=15, text="show policy", command=show_policy)#should show up on bottom frame but dosnet
btnpolicy.pack(side=BOTTOM)

root.mainloop()