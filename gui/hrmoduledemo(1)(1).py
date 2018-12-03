from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("HR : Demo Module")
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
    conn = sqlite3.connect('ufixhr.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `UFIX` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, salary TEXT, taxcode TEXT, nationalinsurance TEXT)")
    
def Create():
    if  SALARY.get() == "" or TAXCODE.get() == "" or NATIONALINSURANCE.get() == "" :
        txt_result.config(text= "Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `UFIX` (salary, taxcode, nationalinsurance) VALUES(?, ?, ?)", (str(SALARY.get()), str(TAXCODE.get()), str(NATIONALINSURANCE.get())))
        conn.commit()
        SALARY.set("")
        TAXCODE.set("")
        NATIONALINSURANCE.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Employee Record is Created!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `UFIX` ORDER BY `salary` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the records from HR Module Database", fg="green")
    
def Exit():
    result = tkMessageBox.askquestion('HR Demo Module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABLES==========================================

SALARY = StringVar()
TAXCODE = StringVar()
NATIONALINSURANCE = StringVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "HR: Simple Demo")
txt_title.pack()
txt_salary = Label(Forms, text="Salary:", font=('arial', 16), bd=15)
txt_salary.grid(row=0, stick="e")
txt_taxcode = Label(Forms, text="Tax Code:", font=('arial', 16), bd=15)
txt_taxcode.grid(row=1, stick="e")
txt_nationalinsurance = Label(Forms, text="National Insurance:", font=('arial', 16), bd=15)
txt_nationalinsurance.grid(row=2, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
salary = Entry(Forms, textvariable=SALARY, width=30)
salary.grid(row=0, column=1)
taxcode = Entry(Forms, textvariable=TAXCODE, width=30)
taxcode.grid(row=1, column=1)
nationalinsurance = Entry(Forms, textvariable=NATIONALINSURANCE, width=30)
nationalinsurance.grid(row=2, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("Salary", "TaxCode", "National Insurance","Test"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Salary', text="Salary", anchor=W)
tree.heading('TaxCode', text="Tax Code", anchor=W)
tree.heading('National Insurance', text="National Insurance", anchor=W)
tree.heading('Test', text="test", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=160)
tree.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
