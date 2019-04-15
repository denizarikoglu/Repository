
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Python: Leave Management System")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#ce1a1a")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
EMPLOYEE_NAME = StringVar()
END_DATE = StringVar()
START_DATE = StringVar()
LEAVE_REASON = StringVar()
SEARCH = StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
        " username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
        "employee_name TEXT, start_date TEXT, end_date TEXT, leave_reason TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Leave Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Leave Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Leave Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
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
    global Home
    Home = Tk()
    Home.title("Leave Management System/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Leave Management System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    filemenu3.add_command(label = "View", command=ViewPolicy)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Holidays", menu=filemenu2)
    menubar.add_cascade(label="Documents", menu=filemenu3)
    Home.config(menu=menubar)
    Home.config(bg="#ce1a1a")

def ViewPolicy():
    global policyform
    policyform = Toplevel()
    policyform.title("Documents/ Policy Document")
    width = 700
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    policyform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    policyform.resizable(0, 0)
    PolicyForm()

def PolicyForm():
    TopAddNew = Frame(policyform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Policy Document for Leave Systems", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(policyform, width=600)
    MidAddNew.pack(side=TOP, pady=5)
    lbl_document = Label(MidAddNew, text= "UFIX and Brainvire LTD. have put this policy document in place to make sure that you know, as well\n"
                                          "as we do, what your rights are. It is a stern belief of ours that the system that has been put in place\n"
                                          "should be intuitive, good-looking and secure. The security is our main priority. YOUR security is our main priority. \n\n"
                                          "We here as Brainvire LTD know how scary things can be in the internet and intranet and that’s we \n"
                                          "follow strict guidelines, laws and rules about employee and customer security. As an example, we \n"
                                          "follow the brand new GDPR laws to the letter. Making sure that we acquire the consent of subjects \n"
                                          "for data processing and anonymizing and data you allow us to collect to protect your privacy. Also, in \n"
                                          "case the worst does happen, and a data breach occurs, no matter how small, we will notify you so \nyou can do what you feel is right. \n\n"
                                          "Right alongside the GDPR laws is the Data Protection Act 2018. This is an updated version of the\n "
                                          "older more outdated Data Protection Act of 1998. This means that all your information that you\n "
                                          "volunteer to us is used in a very specific manner and is forbidden to be used in any way that you are\n  "
                                          "not aware of. This also means that we are not allowed to keep your information for any longer than \n"
                                          "is necessary. If you quit or leave our company, within weeks your information will be wiped from out\n "
                                          "memory. Before that however, your information will be handled in a way that ensures appropriate \n"
                                          "security, including protection against unlawful or unauthorised processing, access, loss, destruction or damage. \n"
                                          "These things are very important to UFIX and Brainvire as because we recruit so many people, and \n"
                                          "work with so many more, we must know how to handle the personal data of not only our employees \n"
                                          "but anyone who volunteers their sensitive personal data to us. Any breach in security by someone in \n"
                                          "house could have major affects for UFIX and Brainvire LTD. If they are found to not follow these \n"
                                          "guidelines, they may be required to pay a fine of up to €10 Million or 2% of their annual turnover \n(Whichever results in a higher figure).\n\n\n"
                                          "Business Ethics and Conduct\n\n"
                                          "We have a few rules that we need everyone to follow at Brainvire LTD, these are covered briefly \n"
                                          "below. There is a more detailed description in a pdf that will be sent out over the next few days.\n\n"
                                          "•	Be respectful, patient and courteous                 •    Be Inclusive \n"
                                          "•	Choose your words carefully                               •    Repeated Harassment will not be tolerated\n"
                                          "•	Be considerate                                                       •    Our differences can be our strengths \n"
                       ,font=('arial', 8), bd=10)
    lbl_document.grid(row=0, sticky=W)




def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Simple Inventory System/Add new")
    width = 700
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Leave Request", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_employeename = Label(MidAddNew, text="Employee Name:", font=('arial', 25), bd=10)
    lbl_employeename.grid(row=0, sticky=W)
    lbl_strtdate = Label(MidAddNew, text="Start Date", font=('arial', 25), bd=10)
    lbl_strtdate.grid(row=1, sticky=W)
    lbl_end = Label(MidAddNew, text="End Date:", font=('arial', 25), bd=10)
    lbl_end.grid(row=2, sticky=W)
    lbl_leave = Label(MidAddNew, text="Leave Reason:", font=('arial', 25), bd=10)
    lbl_leave.grid(row=3, sticky=W)
    employeename = Entry(MidAddNew, textvariable=EMPLOYEE_NAME, font=('arial', 25), width=15)
    employeename.grid(row=0, column=1)
    startdate = Entry(MidAddNew, textvariable=START_DATE, font=('arial', 25), width=15)
    startdate.grid(row=1, column=1)
    enddate = Entry(MidAddNew, textvariable=END_DATE, font=('arial', 25), width=15)
    enddate.grid(row=2, column=1)
    leavereason = Entry(MidAddNew, textvariable=LEAVE_REASON, font=('arial', 25), width=15)
    leavereason.grid(row=3, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=4, columnspan=2, pady=20)


def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (employee_name, start_date, end_date, leave_reason) VALUES(?, ?, ?, ?)",
                   (str(EMPLOYEE_NAME.get()), str(START_DATE.get()), str(END_DATE.get()), str(LEAVE_REASON.get())))
    conn.commit()
    EMPLOYEE_NAME.set("")
    START_DATE.set("")
    END_DATE.set("")
    LEAVE_REASON.set("")
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
    lbl_text = Label(TopViewForm, text="View Leave Requests", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("EmployeeID", "Employee Name", "Start Date", "End Date", "Leave Reason"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('EmployeeID', text="EmployeeID", anchor=W)
    tree.heading('Employee Name', text="Employee Name", anchor=W)
    tree.heading('Start Date', text="Start Date", anchor=W)
    tree.heading('End Date', text="End Date", anchor=W)
    tree.heading('Leave Reason', text="Leave Reason", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
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
        cursor.execute("SELECT * FROM `product` WHERE `employee_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
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
        result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `employee_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Leave Management System/View Product")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
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
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
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


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Leave Management System", font=('arial', 45))
lbl_display.pack()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()