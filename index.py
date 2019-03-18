from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Recruitment")

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
FirstNameemp = StringVar()
LastNameemp = StringVar()
ContactNumberemp = StringVar()
EmailAddressemp = StringVar()
USERNAMEemp = StringVar()
PASSWORDemp = StringVar()
DOBemp = StringVar()
AddressLine1emp = StringVar()
AddressLine2emp = StringVar()
Countryemp = StringVar()
PostCodeemp = StringVar()


PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()

#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `employees` (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, DOB TEXT, 'Phone Number' TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `UFIX_PIM` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, Contact_number TEXT NOT NULL, Email_Address TEXT NOT NULL, Date_of_Birth DATE NOT NULL, Address_line1 TEXT NOT NULL, Address_line2 TEXT NOT NULL, Country TEXT NOT NULL, Postcode TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowExistingEmpForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Recruitment/Account Login")
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
    lbl_text = Label(TopLoginForm, text="Login", font=('arial', 18), width=600)
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

def ShowNewEmpForm():
    global registerform
    registerform = Toplevel()
    registerform.title("Recruitment/Account Registration")
    width = 800
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    registerform.resizable(0,0)
    registerform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    RegisterForm()

def RegisterForm():
    global lbl_result
    TopRegisterForm = Frame(registerform, width=6000, height=100, bd=1, relief=SOLID)
    #scrollbar = Scrollbar(registerform)
    #scrollbar.pack( side = RIGHT, fill = Y )
    TopRegisterForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopRegisterForm, text="Registration New Employee", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftRegisterForm = Frame(registerform, width=600)
    LeftRegisterForm.pack(side=LEFT, pady=50)
    MidRegisterForm = Frame(registerform, width=600)
    MidRegisterForm.pack(side=TOP, pady=50)

    lbl_FirstName= Label(LeftRegisterForm, text="FirstName:", font=('arial', 15), bd=18)
    lbl_FirstName.grid(row=0)
    lbl_LastName= Label(LeftRegisterForm, text="LastName:", font=('arial', 15), bd=18)
    lbl_LastName.grid(row=1)
    lbl_Contactnumber= Label(LeftRegisterForm, text="Contact Number:", font=('arial', 15), bd=18)
    lbl_Contactnumber.grid(row=2)
    lbl_EmailAddress= Label(LeftRegisterForm, text="Email Address:", font=('arial', 15), bd=18)
    lbl_EmailAddress.grid(row=3)
    lbl_DateofBirth= Label(LeftRegisterForm, text="Date Of Birth:", font=('arial', 15), bd=18)
    lbl_DateofBirth.grid(row=4)
    lbl_AddressLine1= Label(LeftRegisterForm, text="Address Line 1:", font=('arial', 15), bd=18)
    lbl_AddressLine1.grid(row=5)
    lbl_AddressLine2= Label(LeftRegisterForm, text="Address Line 2:", font=('arial', 15), bd=18)
    lbl_AddressLine2.grid(row=6)
    lbl_Country= Label(LeftRegisterForm, text="Country:", font=('arial', 15), bd=18)
    lbl_Country.grid(row=7)
    lbl_PostCode= Label(MidRegisterForm, text="PostCode:", font=('arial', 15), bd=18)
    lbl_PostCode.grid(row=8)
    lbl_username = Label(MidRegisterForm, text="Username:", font=('arial', 15), bd=18)
    lbl_username.grid(row=9)
    lbl_password = Label(MidRegisterForm, text="Password:", font=('arial', 15), bd=18)
    lbl_password.grid(row=10)
    lbl_result = Label(MidRegisterForm, text="", font=('arial', 18))
    lbl_result.grid(row=13, columnspan=2)

    FirstName = Entry(LeftRegisterForm, textvariable=FirstNameemp, font=('arial', 15), width=15)
    FirstName.grid(row=0, column=1)
    LastName = Entry(LeftRegisterForm, textvariable=LastNameemp, font=('arial', 15), width=15)
    LastName.grid(row=1, column=1)
    Contactnumber = Entry(LeftRegisterForm, textvariable=ContactNumberemp, font=('arial', 15), width=15)
    Contactnumber.grid(row=2, column=1)
    EmailAddress = Entry(LeftRegisterForm, textvariable=EmailAddressemp, font=('arial', 15), width=15)
    EmailAddress.grid(row=3, column=1)
    DateofBirth = Entry(LeftRegisterForm, textvariable=DOBemp, font=('arial', 15), width=15)
    DateofBirth.grid(row=4, column=1)
    AddressLine1 = Entry(LeftRegisterForm, textvariable=AddressLine1emp, font=('arial', 15), width=15)
    AddressLine1.grid(row=5, column=1)
    AddressLine2 = Entry(LeftRegisterForm, textvariable=AddressLine2emp, font=('arial', 15), width=15)
    AddressLine2.grid(row=6, column=1)
    Country = Entry(LeftRegisterForm, textvariable=Countryemp, font=('arial', 15), width=15)
    Country.grid(row=7, column=1)
    PostCode = Entry(MidRegisterForm, textvariable=PostCodeemp, font=('arial', 15), width=15)
    PostCode.grid(row=8, column=1)
    username = Entry(MidRegisterForm, textvariable=USERNAMEemp, font=('arial', 15), width=15)
    username.grid(row=9, column=1)
    password = Entry(MidRegisterForm, textvariable=PASSWORDemp, font=('arial', 15), width=15, show="*")
    password.grid(row=10, column=1)

    btn_Register = Button(MidRegisterForm, text="Register", font=('arial', 18), width=30, command=Register)
    btn_Register.grid(row=11, columnspan=2, pady=20)
    btn_Policy = Button(MidRegisterForm, text="Policies", font=('arial', 18), width=30, command=PolicyView)
    btn_Policy.grid(row=12, columnspan=2, pady=20)
    btn_Register.bind('<Return>', Login)
    
def Home():
    global Home
    Home = Tk()
    Home.title("Recruitment/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Recruitment", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#99ff99")

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Recruitment/Add new")
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
        result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to delete this record?', icon="warning")
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
    viewform.title("Recruitment/View Product")
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
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to logout?', icon="warning")
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
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
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

def Register(event=None):
    global admin_id
    Database()
    if USERNAMEemp.get == "" or PASSWORDemp.get() == "" or DOBemp.get() == "" or FirstNameemp.get()==""or LastNameemp.get()=="" or ContactNumberemp.get()=="" or EmailAddressemp.get()=="" or AddressLine1emp.get()=="" or AddressLine2emp.get()=="" or Countryemp.get()=="" or PostCodeemp=="":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'UFIX_PIM'(Username,Password,Date_of_Birth,First_name,last_name,Contact_number,Email_Address,Address_line1,Address_line2,Country,Postcode) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(str(USERNAMEemp.get()),str(PASSWORDemp.get()),str(DOBemp.get()),str(FirstNameemp.get()),str(LastNameemp.get()),str(ContactNumberemp.get()),str(EmailAddressemp.get()),str(AddressLine1emp.get()),str(AddressLine2emp.get()),str(Countryemp.get()),str(PostCodeemp.get())))
        conn.commit()
    cursor.close()
    conn.close()

def PolicyView(event=None):
    tkMessageBox.showinfo('Policies', 'It is our policy to make sure the use of our\n software and that the recruiting process is relatively easy and simple to use.\nAs part of a recruitment team there are many rules to follow within the law\nsuch as the newly updated GDPR laws. This is one of the most important laws\nto follow as a lot of personal data will be collected about each applicant. This\ndata must be stored securely where it can’t be exposed to anyone other than\nthe appropriate users.\nAs Brainvire is a big company and several different teams we all have different\npolicies within each group. Our policy will go through everything we expect\nfrom our employees and from everyone that will be using the software\nprovided by us.\n“Brainvire Ltd” is committed to:\n- Viewing all entries for positions as equals and only taking in the best of\nthe best.\n- Providing potential new employees with fair numeracy and literacy tests\nto help the process of elimination.\n- Promoting continual quality of improvement and the philosophy of\ngetting things “right the first time”.')

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()
    RegisterForm.destroy()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Existing Employee", command=ShowExistingEmpForm)
filemenu.add_command(label="New Employee", command=ShowNewEmpForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Recruitment", font=('arial', 45))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
