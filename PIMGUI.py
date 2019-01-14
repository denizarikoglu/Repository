from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Personal Information Management")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 750
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `UFIX_PIM` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, Contact_number TEXT NOT NULL, Email_Address TEXT NOT NULL, Date_of_Birth DATE NOT NULL, Address_line1 TEXT NOT NULL, Address_line2 TEXT NOT NULL, Country TEXT NOT NULL, Postcode TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)")
    
def Create():
    if ID.get() == "" or FIRST_NAME.get() == "" or LAST_NAME.get() == "" or CONTACT_NUMBER.get() == "" or EMAIL_ADDRESS.get() == "" or DOB.get() == "" or HOUSE_ADDRESS1.get() == "" or HOUSE_ADDRESS2.get() == "" or COUNTRY.get() == "" or POSTCODE.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `UFIX_PIM` (emp_id, First_name, Last_name, Contact_number, Email_Address, Date_of_Birth, Address_line1, Address_line2, Country, Postcode, Username, Password) VALUES(?, ?, ?,?, ?, ?,?, ?, ?, ?, ?, ?)", (str(ID.get()), str(FIRST_NAME.get()), str(LAST_NAME.get()), str(CONTACT_NUMBER.get()), str(EMAIL_ADDRESS.get()), str(DOB.get()), str(HOUSE_ADDRESS1.get()), str(HOUSE_ADDRESS2.get()), str(COUNTRY.get()), str(POSTCODE.get()), str(USERNAME.get()), str(PASSWORD.get())))
        conn.commit()
        ID.delete(0, END)
        First_Name.delete(0, END)
        Last_Name.delete(0, END)
        Contact_Number.delete(0, END)
        Email_Address.delete(0, END)
        DoB.delete(0, END)
        House_Address1.delete(0, END)
        House_Address2.delete(0, END)
        Country.delete(0, END)
        Postcode.delete(0, END)
        Username.delete(0, END)
        Password.delete(0, END)
        cursor.close()
        conn.close()
        txt_result.config(text="Employee Record is Created!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `UFIX_PIM` ORDER BY `emp_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the records from HR Module Database", fg="green")
    
def Exit():
    result = tkMessageBox.askquestion('PIM module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABLES==========================================

ID = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
CONTACT_NUMBER = StringVar()
EMAIL_ADDRESS = StringVar()
DOB = StringVar()
HOUSE_ADDRESS1 = StringVar()
HOUSE_ADDRESS2 = StringVar()
COUNTRY = StringVar()
POSTCODE = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

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
txt_title = Label(Top, width=900, font=('arial', 24), text = "Personal Information Management")
txt_title.pack()
txt_ID = Label(Forms, text="Employee ID:", font=('arial', 9), bd=5)
txt_ID.grid(row=0, stick="e")
txt_firstName = Label(Forms, text="First Name:", font=('arial', 9), bd=5)
txt_firstName.grid(row=1, stick="e")
txt_lastName = Label(Forms, text="Last Name:", font=('arial', 9), bd=5)
txt_lastName.grid(row=2, stick="e")
txt_contactNumber = Label(Forms, text = "Contact Number:", font=('arial', 9), bd=5)
txt_contactNumber.grid (row=3,stick = "e")
txt_emailAddress = Label(Forms,text="Email Address:", font=('arial', 9), bd=5)
txt_emailAddress.grid(row=4, stick="e")
txt_DoB = Label(Forms, text="Date of Birth:", font=('arial', 9), bd=5)
txt_DoB.grid(row=5,stick="e")
txt_blank1 = Label(Forms)
txt_blank1.grid(row=6)
txt_address = Label(Forms,text="Home Address:", font=('arial', 9), bd=5)
txt_address.grid(row = 7,stick ="e")
txt_blank2 = Label (Forms)
txt_blank2.grid(row=8)
txt_country = Label(Forms,text="Country:", font=('arial', 9), bd=5)
txt_country.grid(row=9,stick="e")
txt_postCode=Label(Forms,text="Post Code:", font=('arial', 9), bd=5)
txt_postCode.grid(row=10,stick="e")
txt_blank3 = Label(Forms)
txt_blank3.grid(row=11)
txt_username=Label(Forms,text="Username:", font=('arial', 9), bd=5)
txt_username.grid(row=12,stick="e")
txt_password=Label(Forms,text="Password:", font=('arial', 9), bd=5)
txt_password.grid(row=13,stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)
for i in range(1,13):
    root.grid_rowconfigure(i, minsize=10)

#==================================ENTRY WIDGET=======================================
ID = Entry(Forms, textvariable=ID, width=30)
ID.grid(row=0, column=1)
First_Name = Entry(Forms, textvariable=FIRST_NAME, width=30)
First_Name.grid(row=1, column=1)
Last_Name = Entry(Forms, textvariable=LAST_NAME, width=30)
Last_Name.grid(row=2, column=1)
Contact_Number = Entry(Forms, textvariable=CONTACT_NUMBER, width=30)
Contact_Number.grid(row=3, column=1)
Email_Address = Entry(Forms, textvariable=EMAIL_ADDRESS, width =30 )
Email_Address.grid(row=4, column=1)
DoB = Entry(Forms, textvariable=DOB, width=30)
DoB.grid(row=5, column=1)
House_Address1 = Entry(Forms, textvariable=HOUSE_ADDRESS1, width=30)
House_Address1.grid(row=7, column=1)
House_Address2 = Entry(Forms, textvariable=HOUSE_ADDRESS2, width=30)
House_Address2.grid(row=8, column=1)
Country = Entry(Forms, textvariable=COUNTRY, width=30)
Country.grid(row=9, column=1)
Postcode = Entry(Forms, textvariable=POSTCODE, width=30)
Postcode.grid(row=10, column=1)
Username = Entry(Forms, textvariable=USERNAME, width=30)
Username.grid(row=12, column=1)
Password = Entry(Forms, textvariable=PASSWORD, width=30)
Password.grid(row=13, column=1)



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
tree = ttk.Treeview(Right, columns=("emp_id", "First_name", "Last_name", "Contact_number", "Email_Address", "Date_of_Birth", "Address_line1", "Address_line2", "Country", "Postcode", "Username"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('emp_id', text="emp_id", anchor=W)
tree.heading('First_name', text="First_name", anchor=W)
tree.heading('Last_name', text="Last_name", anchor=W)
tree.heading('Contact_number', text="Contact_number", anchor=W)
tree.heading('Email_Address', text="Email_Address", anchor=W)
tree.heading('Date_of_Birth', text="Date_of_Birth", anchor=W)
tree.heading('Address_line1', text="Address_line1", anchor=W)
tree.heading('Address_line2', text="Address_line2", anchor=W)
tree.heading('Country', text="Country", anchor=W)
tree.heading('Postcode', text="Postcode", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=120)
tree.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
