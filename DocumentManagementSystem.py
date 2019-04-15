from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Ufix Ltd. Document Manager")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 400
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


# ==================================METHODS============================================
def database():
    global conn, cursor
    conn = sqlite3.connect('DocumentManagementSystem.db')
    cursor = conn.cursor()


def create():
    if FileID.get() == "" or FileName.get() == "" or FileOwner.get() == "" or DateCreated.get() == "" or Shared.get() == "" or FileLocation.get() == "":
        txt_result.config(text="Please Complete the Required Field(s)!", fg="red")
    else:
        database()
        cursor.execute("INSERT INTO `File` VALUES(?, ?, ?, ?, ?, ?)", (str(FileID.get()), str(FileName.get()), str(FileOwner.get()), str(DateCreated.get()), str(Shared.get()),str(FileLocation.get())))
        conn.commit()
        FileID.set = ""
        FileName.set = ""
        FileOwner.set = ""
        DateCreated.set = ""
        Shared.set = ""
        FileLocation.set = ""
        cursor.close()
        conn.close()
        txt_result.config(text="File Record Has Been Successfully Created!", fg="green")


def read():
    tree.delete(*tree.get_children())
    database()
    cursor.execute("SELECT * FROM `File` ORDER BY `FileID` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully Read the Records From the Document Management System Database", fg="green")

def update():
    tree.selection()

def exit():
    result = tkMessageBox.askquestion('Document Management System', 'Are You Sure You Want To Exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


#def policies():
# ==================================VARIABLES==========================================
FileID = StringVar()
FileName = StringVar()
FileOwner = StringVar()
DateCreated = StringVar()
Shared = StringVar()
FileLocation = StringVar()
Policies = 'D:\Computer Science Year 2\Professional Practice And Employability, Team Based Software Development Workshop\
            Assignments\Assignment 1\Policies\Policies.docx'
# ==================================FRAME==============================================
Top = Frame(root, width=1280, height=100, bd=2, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=100, height=720, bd=2, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=500, height=720, bd=2, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Right, width=500, height=720)
Forms.pack(side=TOP)
Buttons = Frame(Right, width=500, height=100, bd=2)
Buttons.pack(side=BOTTOM)
# ==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=1280, font=('arial', 24, 'bold'), text="File Browser")
txt_title.pack()
txt_FileID = Label(Forms, text="File ID:", font=('arial', 16))
txt_FileID.grid(row=0, stick="e")
txt_FileName = Label(Forms, text="File Name:", font=('Trebuchet MS', 16))
txt_FileName.grid(row=1, stick="e")
txt_FileOwner = Label(Forms, text="File Owner:", font=('Trebuchet MS', 16))
txt_FileOwner.grid(row=2, stick="e")
txt_DateCreated = Label(Forms, text="Date Created:", font=('Trebuchet MS', 16))
txt_DateCreated.grid(row=3, stick="e")
txt_Shared = Label(Forms, text="Shared:", font=('Trebuchet MS', 16))
txt_Shared.grid(row=4, stick="e")
txt_FileLocation = Label(Forms, text="File Location:", font=('Trebuchet MS', 16))
txt_FileLocation.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

# ==================================ENTRY WIDGET=======================================
FileID = Entry(Forms, textvariable=FileID, width=30)
FileID.grid(row=0, column=1)
FileName = Entry(Forms, textvariable=FileName, width=30)
FileName.grid(row=1, column=1)
FileOwner = Entry(Forms, textvariable=FileOwner, width=30)
FileOwner.grid(row=2, column=1)
DateCreated = Entry(Forms, textvariable=DateCreated, width=30)
DateCreated.grid(row=3, column=1)
Shared = Entry(Forms, textvariable=Shared, width=30)
Shared.grid(row=4, column=1)
FileLocation = Entry(Forms, textvariable=FileLocation, width=30)
FileLocation.grid(row=5, column=1)

# ==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=read)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update")
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete")
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=exit)
btn_exit.pack(side=LEFT)
btn_policies = Button(Left, width=10, text="Policies")
btn_policies.pack(side=BOTTOM)
# ==================================LIST WIDGET========================================
scrollbary = Scrollbar(root, orient=VERTICAL)
scrollbarx = Scrollbar(root, orient=HORIZONTAL)
tree = ttk.Treeview(root, columns=("FileID", "FileName", "FileOwner", "DateCreated", "Shared", "FileLocation"),
                    selectmode="extended", height=1280,
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('FileID', text="FileID", anchor=W)
tree.heading('FileName', text="FileName", anchor=W)
tree.heading('FileOwner', text="FileOwner", anchor=W)
tree.heading('DateCreated', text="DateCreated", anchor=W)
tree.heading('Shared', text="Shared", anchor=W)
tree.heading('FileLocation', text="FileLocation", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50)
tree.column('#2', stretch=NO, minwidth=0, width=140)
tree.column('#3', stretch=NO, minwidth=0, width=75)
tree.column('#4', stretch=NO, minwidth=0, width=75)
tree.column('#5', stretch=NO, minwidth=0, width=50)
tree.column('#6', stretch=NO, minwidth=0, width=150)
tree.pack()

# =======================================LOGO==========================================
logo = PhotoImage(file="logo.png")
lbl_logo = Label(Left, image=logo)
lbl_logo.pack()

# ==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()