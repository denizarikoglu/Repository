from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Personal Information Management")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()


#========================================METHODS==========================================

def Database():
    global conn1, cursor1
    global conn, cursor
    conn1 = sqlite3.connect('ufix.s3db')
    cursor1 = conn1.cursor()
    cursor1.execute("CREATE TABLE IF NOT EXISTS `UFIX_PIM` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, Contact_number TEXT NOT NULL, Email_Address TEXT NOT NULL, Date_of_Birth DATE NOT NULL, Address_line1 TEXT NOT NULL, Address_line2 TEXT NOT NULL, Country TEXT NOT NULL, Postcode TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)")


    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Create():
    if ID.get() == "" or FIRST_NAME.get() == "" or LAST_NAME.get() == "" or CONTACT_NUMBER.get() == "" or EMAIL_ADDRESS.get() == "" or DOB.get() == "" or HOUSE_ADDRESS1.get() == "" or HOUSE_ADDRESS2.get() == "" or COUNTRY.get() == "" or POSTCODE.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor1.execute("INSERT INTO `UFIX_PIM` (emp_id, First_name, Last_name, Contact_number, Email_Address, Date_of_Birth, Address_line1, Address_line2, Country, Postcode, Username, Password) VALUES(?, ?, ?,?, ?, ?,?, ?, ?, ?, ?, ?)", (str(ID.get()), str(FIRST_NAME.get()), str(LAST_NAME.get()), str(CONTACT_NUMBER.get()), str(EMAIL_ADDRESS.get()), str(DOB.get()), str(HOUSE_ADDRESS1.get()), str(HOUSE_ADDRESS2.get()), str(COUNTRY.get()), str(POSTCODE.get()), str(USERNAME.get()), str(PASSWORD.get())))
        conn1.commit()
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
        cursor1.close()
        conn1.close()
        txt_result.config(text="Employee Record is Created!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor1.execute("SELECT * FROM `UFIX_PIM` ORDER BY `emp_id` ASC")
    fetch = cursor1.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    cursor1.close()
    conn1.close()
    txt_result.config(text="Successfully read the records from HR Module Database", fg="green")

def Exit():
    result = tkMessageBox.askquestion('PIM system', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('PIM System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("PIM System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    
def Home():
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
    #========================================VARIABLES========================================

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
    Forms = Frame(Left, width=600, height=450)
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
    global txt_result
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
    global tree
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

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("PIM System/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()

def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('PIM System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("PIM System/View Product")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def Logout():
    result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
  
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `Admin` WHERE `Username` = ? AND `Password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `Admin` WHERE `Username` = ? AND `Password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="PIM", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="PIM System", font=('arial', 45))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
