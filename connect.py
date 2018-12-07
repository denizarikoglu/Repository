from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import webbrowser


root = Tk()
root.title("Welcome page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect('Ufixltd.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Employee` (idEmployee INTEGER PRIMARY KEY  AUTOINCREMENT ,firstNameEmployee	VARCHAR ( 50 ),lastNameEmployee	VARCHAR ( 50 ),emailEmployee	VARCHAR ( 50 ),phoneEmployee	VARCHAR ( 20 ),idTeam	VARCHAR(50))")


def Create():
    if FirstName.get() == "" or LastName.get() == "" or Email.get() == "" or Phone.get() == "" or Team.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `Employee` (firstNameEmployee, lastNameEmployee, emailEmployee, phoneEmployee, idTeam) VALUES(?, ?, ?, ?, ?)",
                       (str(FirstName.get()), str(LastName.get()), str(Email.get()), str(Phone.get()), str(Team.get())))
        conn.commit()
        FirstName.set("")
        LastName.set("")
        Email.set("")
        Phone.set("")
        Team.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Employee Record is Created!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `Employee`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]), tag=('click',))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the records from Welcome page Database", fg="green")

def Update():
    if FirstName.get() == "" or LastName.get() == "" or Email.get() == "" or Phone.get() == "" or Team.get() == "":
        txt_result.config(text="Please select a row!", fg="red")
    else:
        Database()
        cursor.execute("UPDATE `Employee` set firstNameEmployee = ?,lastNameEmployee = ? ,emailEmployee = ? ,phoneEmployee = ? ,idTeam = ? where idEmployee = ?",
            (str(FirstName.get()), str(LastName.get()), str(Email.get()), str(Phone.get()), str(Team.get()),tree.set(tree.selection(), 'Id')))
        conn.commit()
        FirstName.set("")
        LastName.set("")
        Email.set("")
        Phone.set("")
        Team.set("")
        cursor.close()
        conn.close()
        Read()
        txt_result.config(text="Successfully update the records from Welcome page Database", fg="green")

def on_click(event):
    FirstName.set(tree.set(tree.selection(), 'FirstName'))
    LastName.set(tree.set(tree.selection(), 'LastName'))
    Email.set(tree.set(tree.selection(), 'Email'))
    Phone.set(tree.set(tree.selection(), 'Phone'))
    Team.set(tree.set(tree.selection(), 'Team'))

def Delete():
    if FirstName.get() == "" or LastName.get() == "" or Email.get() == "" or Phone.get() == "" or Team.get() == "":
        txt_result.config(text="Please select a row!", fg="red")
    else:
        Database()
        cursor.execute("DELETE from Employee where idEmployee = "+tree.set(tree.selection(), 'Id')+"")
        conn.commit()
        cursor.close()
        conn.close()
        Read()
        txt_result.config(text="Successfully delete the records from Welcome page Database", fg="green")

def Exit():
    result = tkMessageBox.askquestion('Welcome page', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def callback(event):
    webbrowser.open_new(r"Policies.pdf")
#==================================VARIABLES==========================================

FirstName = StringVar()
LastName = StringVar()
Email = StringVar()
Phone = StringVar()
Team = StringVar()
Id = StringVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(root, width=900, height=400, bd=8, relief="raise")
Middle.pack()
Left = Frame(Middle, width=300, height=400, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(Middle, width=600, height=400, bd=8, relief="raise")
Right.pack(side=RIGHT)
Bottom = Frame(root, width=300, height=50, bd=4, relief="raise")
Bottom.pack(side=BOTTOM)
Forms = Frame(Left, width=300, height=400)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=50, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Welcome Page")
txt_title.pack()
txt_firstName = Label(Forms, text="First Name:", font=('arial', 16), bd=15)
txt_firstName.grid(row=0, stick="e")
txt_lastName = Label(Forms, text="Last Name:", font=('arial', 16), bd=15)
txt_lastName.grid(row=1, stick="e")
txt_email = Label(Forms, text="Email:", font=('arial', 16), bd=15)
txt_email.grid(row=2, stick="e")
txt_phone = Label(Forms, text="Phone:", font=('arial', 16), bd=15)
txt_phone.grid(row=3, stick="e")
txt_team = Label(Forms, text="Team:", font=('arial', 16), bd=15)
txt_team.grid(row=4, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)
link = Label(Bottom, width=900, text="Policies", fg="blue", cursor="hand2")
link.bind("<Button-1>", callback)
link.pack()

#==================================ENTRY WIDGET=======================================
firstName = Entry(Forms, textvariable=FirstName, width=30)
firstName.grid(row=0, column=1)
lastName = Entry(Forms, textvariable=LastName, width=30)
lastName.grid(row=1, column=1)
email = Entry(Forms, textvariable=Email, width=30)
email.grid(row=2, column=1)
phone = Entry(Forms, textvariable=Phone, width=30)
phone.grid(row=3, column=1)
team = Entry(Forms, textvariable=Team, width=30)
team.grid(row=4, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", command=Update)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", command=Delete)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("Id", "FirstName", "LastName", "Email", "Phone", "Team"), selectmode="extended", height=17, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('FirstName', text="FirstName", anchor=W)
tree.heading('LastName', text="LastName", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.heading('Phone', text="Phone", anchor=W)
tree.heading('Team', text="Team", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.bind("<Button-1>", on_click)
tree.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
