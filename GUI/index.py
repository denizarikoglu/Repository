from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import os

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

NumeracyMentalq1 = StringVar()
NumeracyMentalq2 = StringVar()
NumeracyMentalq3 = StringVar()
NumeracyMentalq4 = StringVar()
NumeracyMentalq5 = StringVar()
NumeracyMentalq6 = StringVar()
NumeracyMentalq7 = StringVar()
NumeracyMentalq8 = StringVar()
NumeracyMentalq9 = StringVar()
NumeracyMentalq10 = StringVar()
NumeracyMentalq11 = StringVar()
NumeracyMentalq12 = StringVar()
NumeracyMentalq13 = StringVar()
NumeracyMentalq14 = StringVar()
NumeracyMentalq15 = StringVar()

NumeracyWrittenq1 = StringVar()
NumeracyWrittenq2 = StringVar()
NumeracyWrittenq3 = StringVar()
NumeracyWrittenq4 = StringVar()
NumeracyWrittenq5 = StringVar()
NumeracyWrittenq6 = StringVar()
NumeracyWrittenq7 = StringVar()
NumeracyWrittenq8 = StringVar()
NumeracyWrittenq9 = StringVar()
NumeracyWrittenq10 = StringVar()
NumeracyWrittenq11 = StringVar()
NumeracyWrittenq12 = StringVar()

LiteracySpelling1 = StringVar()
LiteracySpelling2 = StringVar()
LiteracySpelling3 = StringVar()
LiteracySpelling4 = StringVar()
LiteracySpelling5 = StringVar()
LiteracySpelling6 = StringVar()
LiteracySpelling7 = StringVar()
LiteracySpelling8 = StringVar()
LiteracySpelling9 = StringVar()
LiteracySpelling10 = StringVar()
LiteracySpelling11 = StringVar()
LiteracySpelling12 = StringVar()

LiteracyGrammarPartA1 = StringVar()
LiteracyGrammarPartA2 = StringVar()
LiteracyGrammarPartA3 = StringVar()
LiteracyGrammarPartA4 = StringVar()
LiteracyGrammarPartA5 = StringVar()

LiteracyGrammarPartB1 = StringVar()
LiteracyGrammarPartB2 = StringVar()

LiteracyGrammarPartC1 = StringVar()
LiteracyGrammarPartC2 = StringVar()
LiteracyGrammarPartC3 = StringVar()

LiteracyComprehensionA = StringVar()
LiteracyComprehensionB = StringVar()
LiteracyComprehensionC = StringVar()
LiteracyComprehensionD = StringVar()

JobTitleAdd = StringVar()
ContractStartDateAdd = StringVar()
ContractEndDateAdd = StringVar()
StartingSalaryAdd = StringVar()
BriefDescriptionAdd = StringVar()

JobIDAssign= StringVar()

LiteracyPunctuationText = StringVar()

USERNAMEemplogin = StringVar()
PASSWORDemplogin = StringVar()

PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()
SEARCHJOBS = StringVar()

#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `UFIX_PIM` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, Contact_number TEXT NOT NULL, Email_Address TEXT NOT NULL, Date_of_Birth DATE NOT NULL, Address_line1 TEXT NOT NULL, Address_line2 TEXT NOT NULL, Country TEXT NOT NULL, Postcode TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `NumeracyTestMental` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT, `Question 3` TEXT, `Question 4` TEXT, `Question 5` TEXT, `Question 6` TEXT, `Question 7` TEXT, `Question 8` TEXT, `Question 9` TEXT, `Question 10` TEXT, `Question 11` TEXT, `Question 12` TEXT, `Question 13` TEXT, `Question 14` TEXT, `Question 15` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `NumeracyTestWritten` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT, `Question 3` TEXT, `Question 4` TEXT, `Question 5` TEXT, `Question 6` TEXT, `Question 7` TEXT, `Question 8` TEXT, `Question 9` TEXT, `Question 10` TEXT, `Question 11` TEXT, `Question 12` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracySpelling` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT, `Question 3` TEXT, `Question 4` TEXT, `Question 5` TEXT, `Question 6` TEXT, `Question 7` TEXT, `Question 8` TEXT, `Question 9` TEXT, `Question 10` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracyGrammarPartA` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT, `Question 3` TEXT, `Question 4` TEXT, `Question 5` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracyGrammarPartB` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracyGrammarPartC` ( `emp_id` TEXT,`Question 1` TEXT, `Question 2` TEXT, `Question 3` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracyComprehension` ( `emp_id` TEXT,`Part A` TEXT, `Part B` TEXT, `Part C` TEXT, `Part D` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `Available_Jobs` (job_id INTEGER PRIMARY KEY AUTOINCREMENT, `Job Title` TEXT, `Contract Start Date` TEXT, `Contract End Date` TEXT, `Starting Salary` TEXT, `Brief Description` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `EmployeeJobsAssigned` ( `emp_id` TEXT, `job_id` TEXT )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `LiteracyPunctuation` ( `emp_id` TEXT, `Text` TEXT )")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def ShowExistingempForm():
    global loginempform
    loginempform = Toplevel()
    loginempform.title("Recruitment/Account Employee Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginempform.resizable(0, 0)
    loginempform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginempForm()

def LoginempForm():
    global lbl_result
    TopLoginempForm = Frame(loginempform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginempForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginempForm, text="Employee Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginempForm = Frame(loginempform, width=600)
    MidLoginempForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginempForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginempForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginempForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginempForm, textvariable=USERNAMEemplogin, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginempForm, textvariable=PASSWORDemplogin, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_loginemp = Button(MidLoginempForm, text="Login", font=('arial', 18), width=30, command=Loginemp)
    btn_loginemp.grid(row=2, columnspan=2, pady=20)
    btn_loginemp.bind('<Return>', Login)

def ShowExistingAdminForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Recruitment/Account Admin Login")
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
    lbl_text = Label(TopLoginForm, text="Admin Login", font=('arial', 18), width=600)
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
    Home.title("Recruitment/Home Admin")
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
    filemenu.add_command(label="Exit", command=Exit)
    #filemenu2.add_command(label="Add new", command=ShowAddNew)
    #filemenu2.add_command(label="View", command=ShowView)
    filemenu2.add_command(label="Add Jobs", command=ShowAddAvailableJobs)
    filemenu2.add_command(label="View Jobs", command=ShowViewJobsAdmin)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Jobs", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#99ff99")

def HomeEmp():
    global HomeEmp
    HomeEmp = Tk()
    HomeEmp.title("Recruitment/Home Employee")
    width = 1024
    height = 720
    screen_width = HomeEmp.winfo_screenwidth()
    screen_height = HomeEmp.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    HomeEmp.geometry("%dx%d+%d+%d" % (width, height, x, y))
    HomeEmp.resizable(0, 0)
    Title = Frame(HomeEmp, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Recruitment", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(HomeEmp)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=LogoutEmp)#CONTINUE HERE
    filemenu.add_command(label="Exit", command=Exit)
    filemenu2.add_command(label="Numeracy", command=NumeracyIntro)
    filemenu2.add_command(label="Literacy", command=LiteracyIntro)
    filemenu3.add_command(label="Numeracy Mental", command=NumeracyTestMental)
    filemenu3.add_command(label="Numeracy Written", command=NumeracyTestWritten)#written numeracy test
    filemenu4.add_command(label="Spelling", command=LiteracySpellingTest)
    filemenu4.add_command(label="Punctuation", command=LiteracyPunctuationTest)
    filemenu4.add_command(label="Grammar Part A", command=LiteracyGrammarPartATest)
    filemenu4.add_command(label="Grammar Part B", command=LiteracyGrammarPartBTest)
    filemenu4.add_command(label="Grammar Part C", command=LiteracyGrammarPartCTest)
    filemenu4.add_command(label="Comprehension", command=LiteracyComprehensionTest)
    filemenu5.add_command(label="View Jobs", command=ShowViewJobs)
    filemenu5.add_command(label="Apply", command=ShowAssignJob)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Intro", menu=filemenu2)
    menubar.add_cascade(label="Numeracy Test", menu=filemenu3)
    menubar.add_cascade(label="Literacy Test", menu=filemenu4)
    menubar.add_cascade(label="Jobs", menu=filemenu5)
    HomeEmp.config(menu=menubar)
    HomeEmp.config(bg="#99ff99")

def NumeracyIntro():
    osCommandString = "notepad.exe NumeracyIntro.txt"
    os.system(osCommandString)

def LiteracyIntro():
    osCommandString = "notepad.exe LiteracyIntro.txt"
    os.system(osCommandString)

def ShowAssignJob():
    global assignjobform
    assignjobform = Toplevel()
    assignjobform.title("Recruitment/Apply for a job")
    width = 600
    height = 500
    screen_width = HomeEmp.winfo_screenwidth()
    screen_height = HomeEmp.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    assignjobform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    assignjobform.resizable(0, 0)
    AddAssignJob()

def AddAssignJob():
    global lbl_result
    TopAddAssignJob = Frame(assignjobform, width=600, height=100, bd=1, relief=SOLID)
    TopAddAssignJob.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddAssignJob, text="Apply for a job", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddAssignJob = Frame(assignjobform, width=600)
    MidAddAssignJob.pack(side=TOP, pady=50)
    lbl_1 = Label(MidAddAssignJob, text="Job ID:", font=('arial', 25), bd=10)
    lbl_1.grid(row=0, sticky=W)
    JobID = Entry(MidAddAssignJob, textvariable=JobIDAssign, font=('arial', 25), width=15)
    JobID.grid(row=0, column=1)
    lbl_result = Label(MidAddAssignJob, text="", font=('arial', 18))
    lbl_result.grid(row=1, columnspan=2)#add 3 from previous row count

    btn_AddAssignJob = Button(MidAddAssignJob, text="Apply", font=('arial', 18), width=30, bg="#009ACD", command=AddAssignJobNew)
    btn_AddAssignJob.grid(row=5, columnspan=2, pady=20)

def AddAssignJobNew():
    Database()
    cursor.execute("INSERT INTO `EmployeeJobsAssigned` ('emp_id','job_id') VALUES(?, ?)", (emp_id ,str(JobIDAssign.get())))
    conn.commit()
    lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def ShowAddAvailableJobs():
    global addavailablejobsform
    addavailablejobsform = Toplevel()
    addavailablejobsform.title("Recruitment/Add New Available Job")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addavailablejobsform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addavailablejobsform.resizable(0, 0)
    AddAvailableJobs()

def AddAvailableJobs():
    TopAddNew = Frame(addavailablejobsform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Available Job", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddAvailableJobs = Frame(addavailablejobsform, width=600)
    MidAddAvailableJobs.pack(side=TOP, pady=50)
    lbl_1 = Label(MidAddAvailableJobs, text="Job Title:", font=('arial', 25), bd=10)
    lbl_1.grid(row=0, sticky=W)
    lbl_2 = Label(MidAddAvailableJobs, text="Contract Start Date:", font=('arial', 25), bd=10)
    lbl_2.grid(row=1, sticky=W)
    lbl_3 = Label(MidAddAvailableJobs, text="Contract End Date:", font=('arial', 25), bd=10)
    lbl_3.grid(row=2, sticky=W)
    lbl_4 = Label(MidAddAvailableJobs, text="Starting Salary:", font=('arial', 25), bd=10)
    lbl_4.grid(row=3, sticky=W)
    lbl_5 = Label(MidAddAvailableJobs, text="Brief Description:", font=('arial', 25), bd=10)
    lbl_5.grid(row=4, sticky=W)
    JobTitle = Entry(MidAddAvailableJobs, textvariable=JobTitleAdd, font=('arial', 25), width=15)
    JobTitle.grid(row=0, column=1)
    ContractStartDate = Entry(MidAddAvailableJobs, textvariable=ContractStartDateAdd, font=('arial', 25), width=15)
    ContractStartDate.grid(row=1, column=1)
    ContractEndDate = Entry(MidAddAvailableJobs, textvariable=ContractEndDateAdd, font=('arial', 25), width=15)
    ContractEndDate.grid(row=2, column=1)
    StartingSalary = Entry(MidAddAvailableJobs, textvariable=StartingSalaryAdd, font=('arial', 25), width=15)
    StartingSalary.grid(row=3, column=1)
    BriefDescription = Entry(MidAddAvailableJobs, textvariable=BriefDescriptionAdd, font=('arial', 25), width=15)
    BriefDescription.grid(row=4, column=1)

    btn_addAddAvailableJobs = Button(MidAddAvailableJobs, text="Add", font=('arial', 18), width=30, bg="#009ACD", command=AddNewAvailableJobs)
    btn_addAddAvailableJobs.grid(row=5, columnspan=2, pady=20)

def AddNewAvailableJobs():
    Database()
    cursor.execute("INSERT INTO `Available_Jobs` ('Job Title','Contract Start Date','Contract End Date','Starting Salary','Brief Description') VALUES(?, ?, ?,?,?)", (str(JobTitleAdd.get()), str(ContractStartDateAdd.get()), str(ContractEndDateAdd.get()),str(StartingSalaryAdd.get()),str(BriefDescriptionAdd.get())))
    conn.commit()
    JobTitleAdd.set("")
    ContractStartDateAdd.set("")
    ContractEndDateAdd.set("")
    StartingSalaryAdd.set("")
    BriefDescriptionAdd.set("")
    cursor.close()
    conn.close()

def LiteracyComprehensionTest():
    global literacyComprehensionform
    literacyComprehensionform = Toplevel()
    literacyComprehensionform.title("Recruitment/Literacy Comprehension Test")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacyComprehensionform.resizable(0,0)
    literacyComprehensionform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracyComprehensionForm()

def LiteracyComprehensionForm():
    global lbl_result
    TopLiteracyComprehensionForm = Frame(literacyComprehensionform, width=600, height=100, bd=1, relief=SOLID)
    TopLiteracyComprehensionForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracyComprehensionForm, text="Literacy Grammar Part C Test", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracyComprehensionForm = Frame(literacyComprehensionform, width=600)
    LeftLiteracyComprehensionForm.pack(side=TOP, pady=50)
    MidLiteracyComprehensionForm = Frame(literacyComprehensionform, width=600)
    MidLiteracyComprehensionForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracyComprehensionForm, text="Part A:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftLiteracyComprehensionForm, text="Part B:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftLiteracyComprehensionForm, text="Part C:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_4= Label(LeftLiteracyComprehensionForm, text="Part D:", font=('arial', 15), bd=18)
    lbl_4.grid(row=3)
    lbl_result = Label(LeftLiteracyComprehensionForm, text="", font=('arial', 18))
    lbl_result.grid(row=6, columnspan=2)#add 3 from previous row count

    LiteracyComprehensionAq = Entry(LeftLiteracyComprehensionForm, textvariable=LiteracyComprehensionA, font=('arial', 15), width=15)
    LiteracyComprehensionAq.grid(row=0, column=1)
    LiteracyComprehensionBq = Entry(LeftLiteracyComprehensionForm, textvariable=LiteracyComprehensionB, font=('arial', 15), width=15)
    LiteracyComprehensionBq.grid(row=1, column=1)
    LiteracyComprehensionCq = Entry(LeftLiteracyComprehensionForm, textvariable=LiteracyComprehensionC, font=('arial', 15), width=15)
    LiteracyComprehensionCq.grid(row=2, column=1)
    LiteracyComprehensionDq = Entry(LeftLiteracyComprehensionForm, textvariable=LiteracyComprehensionD, font=('arial', 15), width=15)
    LiteracyComprehensionDq.grid(row=3, column=1)

    btn_LiteracyComprehension = Button(LeftLiteracyComprehensionForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracyComprehension)
    btn_LiteracyComprehension.grid(row=4, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracyComprehension.bind('<Return>', Login)

def LiteracyPunctuationTest():
    global literacyPunctuationform
    literacyPunctuationform = Toplevel()
    literacyPunctuationform.title("Recruitment/Literacy Punctuation")
    width = 800
    height = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacyPunctuationform.resizable(0,0)
    literacyPunctuationform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracyPunctuationForm()

def LiteracyPunctuationForm():
    global lbl_result
    TopLiteracyPunctuationForm = Frame(literacyPunctuationform, width=6000, height=100, bd=1, relief=SOLID)
    TopLiteracyPunctuationForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracyPunctuationForm, text="Literacy Punctuation", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracyPunctuationForm = Frame(literacyPunctuationform, width=600)
    LeftLiteracyPunctuationForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracyPunctuationForm, text="This is an extract from Brookdale School’s newsletter.\nDo you have some spare time?\nAre you willing to give the school a helping hand\nWe are looking for volunteers from the community to join us in enhancing the\nopportunities and experiences of Brookdale Schools children. There are\nvarious ways in which you could help as a paired reader; as a sports coach or\nreferee; as a chaperone on outings by sharing a specialist knowledge you\nhave.\nThe paired reading scheme has been running at brookdale for two years,\nduring which time over one hundred children have benefited from the help\ngiven to them by volunteers. The scheme operates every morning from 9.00\nto 9.30 a.m. helpers elect to come as many mornings as they feel able and full\nguidance and training are given. Pupils responses have been almost wholly\npositive one twelve-year-old recently said “I thought I’d never be able to read,\nbut thanks to Mrs Davis, whos been helping me for eight months Ive just read\n‘The Magician’s Nephew’ and The silver Chair’ all on my own.”\n\nBelow is the correct version, with the answers highlighted in green:\nThis is an extract from Brookdale School’s newsletter.\nDo you have some spare time?\nAre you willing to give the school a helping hand?\nWe are looking for volunteers from the community to join us in enhancing the\nopportunities and experiences of Brookdale School’s children. There are\nvarious ways in which you could help: as a paired reader; as a sports coach or\nreferee; as a chaperone on outings; by sharing a specialist knowledge you\nhave.\nThe paired reading scheme has been running at Brookdale for two years,\nduring which time over one hundred children have benefitted from the help\ngiven to them by volunteers. The scheme operates every morning from 9.00\nto 9.30 a.m. Helpers elect to come as many mornings as they feel able and full\nguidance and training are given. Pupils’ responses have been almost wholly\npositive. One twelve-year-old recently said, “I thought I’d never be able to read,\nbut thanks to Mrs Davis, who’s been helping me for eight months, I’ve just read\n‘The Magician’s Nephew’ and ‘The Silver Chair’ all on my own.”", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_result = Label(LeftLiteracyPunctuationForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)#add 3 from previous row count

    LiteracyGrammarPartC1q = Entry(LeftLiteracyPunctuationForm, textvariable=LiteracyPunctuationText, font=('arial', 15), width=15)
    LiteracyGrammarPartC1q.grid(row=0, column=1)

    btn_LiteracyPunctuation = Button(LeftLiteracyPunctuationForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracyPunctuationForm)
    btn_LiteracyPunctuation.grid(row=1, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracyPunctuation.bind('<Return>', Login)

def LiteracyGrammarPartCTest():
    global literacygrammarPartCtestform
    literacygrammarPartCtestform = Toplevel()
    literacygrammarPartCtestform.title("Recruitment/Literacy GrammarPart C Test")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacygrammarPartCtestform.resizable(0,0)
    literacygrammarPartCtestform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracyGrammarPartCTestForm()

def LiteracyGrammarPartCTestForm():
    global lbl_result
    TopLiteracyGrammarPartCTestForm = Frame(literacygrammarPartCtestform, width=6000, height=100, bd=1, relief=SOLID)
    TopLiteracyGrammarPartCTestForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracyGrammarPartCTestForm, text="Literacy Grammar Part C Test", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracyGrammarPartCTestForm = Frame(literacygrammarPartCtestform, width=600)
    LeftLiteracyGrammarPartCTestForm.pack(side=TOP, pady=50)
    MidLiteracyGrammarPartCTestForm = Frame(literacygrammarPartCtestform, width=600)
    MidLiteracyGrammarPartCTestForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracyGrammarPartCTestForm, text="1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftLiteracyGrammarPartCTestForm, text="2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftLiteracyGrammarPartCTestForm, text="3:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_result = Label(LeftLiteracyGrammarPartCTestForm, text="", font=('arial', 18))
    lbl_result.grid(row=5, columnspan=2)#add 3 from previous row count

    LiteracyGrammarPartC1q = Entry(LeftLiteracyGrammarPartCTestForm, textvariable=LiteracyGrammarPartC1, font=('arial', 15), width=15)
    LiteracyGrammarPartC1q.grid(row=0, column=1)
    LiteracyGrammarPartC2q = Entry(LeftLiteracyGrammarPartCTestForm, textvariable=LiteracyGrammarPartC2, font=('arial', 15), width=15)
    LiteracyGrammarPartC2q.grid(row=1, column=1)
    LiteracyGrammarPartC3q = Entry(LeftLiteracyGrammarPartCTestForm, textvariable=LiteracyGrammarPartC3, font=('arial', 15), width=15)
    LiteracyGrammarPartC3q.grid(row=2, column=1)

    btn_LiteracyGrammarPartCTest = Button(LeftLiteracyGrammarPartCTestForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracyGrammarPartC)
    btn_LiteracyGrammarPartCTest.grid(row=3, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracyGrammarPartCTest.bind('<Return>', Login)

def LiteracyGrammarPartBTest():
    global literacygrammarPartBtestform
    literacygrammarPartBtestform = Toplevel()
    literacygrammarPartBtestform.title("Recruitment/Literacy GrammarPart B Test")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacygrammarPartBtestform.resizable(0,0)
    literacygrammarPartBtestform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracyGrammarPartBTestForm()

def LiteracyGrammarPartBTestForm():
    global lbl_result
    TopLiteracyGrammarPartBTestForm = Frame(literacygrammarPartBtestform, width=6000, height=100, bd=1, relief=SOLID)
    TopLiteracyGrammarPartBTestForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracyGrammarPartBTestForm, text="Literacy Grammar Part B Test", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracyGrammarPartBTestForm = Frame(literacygrammarPartBtestform, width=600)
    LeftLiteracyGrammarPartBTestForm.pack(side=TOP, pady=50)
    MidLiteracyGrammarPartBTestForm = Frame(literacygrammarPartBtestform, width=600)
    MidLiteracyGrammarPartBTestForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracyGrammarPartBTestForm, text="1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftLiteracyGrammarPartBTestForm, text="2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_result = Label(LeftLiteracyGrammarPartBTestForm, text="", font=('arial', 18))
    lbl_result.grid(row=4, columnspan=2)#add 3 from previous row count

    LiteracyGrammarPartB1q = Entry(LeftLiteracyGrammarPartBTestForm, textvariable=LiteracyGrammarPartB1, font=('arial', 15), width=15)
    LiteracyGrammarPartB1q.grid(row=0, column=1)
    LiteracyGrammarPartB2q = Entry(LeftLiteracyGrammarPartBTestForm, textvariable=LiteracyGrammarPartB2, font=('arial', 15), width=15)
    LiteracyGrammarPartB2q.grid(row=1, column=1)

    btn_LiteracyGrammarPartBTest = Button(LeftLiteracyGrammarPartBTestForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracyGrammarPartB)
    btn_LiteracyGrammarPartBTest.grid(row=2, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracyGrammarPartBTest.bind('<Return>', Login)

def LiteracyGrammarPartATest():
    global literacygrammarPartAtestform
    literacygrammarPartAtestform = Toplevel()
    literacygrammarPartAtestform.title("Recruitment/Literacy GrammarPart A Test")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacygrammarPartAtestform.resizable(0,0)
    literacygrammarPartAtestform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracyGrammarPartATestForm()

def LiteracyGrammarPartATestForm():
    global lbl_result
    TopLiteracyGrammarPartATestForm = Frame(literacygrammarPartAtestform, width=6000, height=100, bd=1, relief=SOLID)
    TopLiteracyGrammarPartATestForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracyGrammarPartATestForm, text="Literacy Grammar Part A Test", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracyGrammarPartATestForm = Frame(literacygrammarPartAtestform, width=600)
    LeftLiteracyGrammarPartATestForm.pack(side=TOP, pady=50)
    MidLiteracyGrammarPartATestForm = Frame(literacygrammarPartAtestform, width=600)
    MidLiteracyGrammarPartATestForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracyGrammarPartATestForm, text="Question 1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftLiteracyGrammarPartATestForm, text="Question 2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftLiteracyGrammarPartATestForm, text="Question 3:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_4= Label(LeftLiteracyGrammarPartATestForm, text="Question 4:", font=('arial', 15), bd=18)
    lbl_4.grid(row=3)
    lbl_5= Label(LeftLiteracyGrammarPartATestForm, text="Question 5:", font=('arial', 15), bd=18)
    lbl_5.grid(row=4)
    lbl_result = Label(LeftLiteracyGrammarPartATestForm, text="", font=('arial', 18))
    lbl_result.grid(row=7, columnspan=2)#add 3 from previous row count

    LiteracyGrammarPartA1q = Entry(LeftLiteracyGrammarPartATestForm, textvariable=LiteracyGrammarPartA1, font=('arial', 15), width=15)
    LiteracyGrammarPartA1q.grid(row=0, column=1)
    LiteracyGrammarPartA2q = Entry(LeftLiteracyGrammarPartATestForm, textvariable=LiteracyGrammarPartA2, font=('arial', 15), width=15)
    LiteracyGrammarPartA2q.grid(row=1, column=1)
    LiteracyGrammarPartA3q = Entry(LeftLiteracyGrammarPartATestForm, textvariable=LiteracyGrammarPartA3, font=('arial', 15), width=15)
    LiteracyGrammarPartA3q.grid(row=2, column=1)
    LiteracyGrammarPartA4q = Entry(LeftLiteracyGrammarPartATestForm, textvariable=LiteracyGrammarPartA4, font=('arial', 15), width=15)
    LiteracyGrammarPartA4q.grid(row=3, column=1)
    LiteracyGrammarPartA5q = Entry(LeftLiteracyGrammarPartATestForm, textvariable=LiteracyGrammarPartA5, font=('arial', 15), width=15)
    LiteracyGrammarPartA5q.grid(row=4, column=1)

    btn_LiteracyGrammarPartATest = Button(LeftLiteracyGrammarPartATestForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracyGrammarPartA)
    btn_LiteracyGrammarPartATest.grid(row=5, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracyGrammarPartATest.bind('<Return>', Login)

def LiteracySpellingTest():
    global literacyspellingtestform
    literacyspellingtestform = Toplevel()
    literacyspellingtestform.title("Recruitment/Literacy Spelling Test")
    width = 800
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    literacyspellingtestform.resizable(0,0)
    literacyspellingtestform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LiteracySpellingTestForm()

def LiteracySpellingTestForm():
    global lbl_result
    TopLiteracySpellingTestForm = Frame(literacyspellingtestform, width=6000, height=100, bd=1, relief=SOLID)
    TopLiteracySpellingTestForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLiteracySpellingTestForm, text="Literacy Spelling Test", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftLiteracySpellingTestForm = Frame(literacyspellingtestform, width=600)
    LeftLiteracySpellingTestForm.pack(side=LEFT, pady=50)
    MidLiteracySpellingTestForm = Frame(literacyspellingtestform, width=600)
    MidLiteracySpellingTestForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe LiteracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftLiteracySpellingTestForm, text="Question 1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftLiteracySpellingTestForm, text="Question 2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftLiteracySpellingTestForm, text="Question 3:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_4= Label(LeftLiteracySpellingTestForm, text="Question 4:", font=('arial', 15), bd=18)
    lbl_4.grid(row=3)
    lbl_5= Label(LeftLiteracySpellingTestForm, text="Question 5:", font=('arial', 15), bd=18)
    lbl_5.grid(row=4)
    lbl_6= Label(LeftLiteracySpellingTestForm, text="Question 6:", font=('arial', 15), bd=18)
    lbl_6.grid(row=5)
    lbl_7= Label(LeftLiteracySpellingTestForm, text="Question 7:", font=('arial', 15), bd=18)
    lbl_7.grid(row=6)
    lbl_8= Label(LeftLiteracySpellingTestForm, text="Question 8:", font=('arial', 15), bd=18)
    lbl_8.grid(row=7)
    lbl_9= Label(MidLiteracySpellingTestForm, text="Question 9:", font=('arial', 15), bd=18)
    lbl_9.grid(row=8)
    lbl_10 = Label(MidLiteracySpellingTestForm, text="Question 10:", font=('arial', 15), bd=18)
    lbl_10.grid(row=9)
    lbl_result = Label(MidLiteracySpellingTestForm, text="", font=('arial', 18))
    lbl_result.grid(row=12, columnspan=2)#add 3 from previous row count

    LiteracySpelling1q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling1, font=('arial', 15), width=15)
    LiteracySpelling1q.grid(row=0, column=1)
    LiteracySpelling2q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling2, font=('arial', 15), width=15)
    LiteracySpelling2q.grid(row=1, column=1)
    LiteracySpelling3q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling3, font=('arial', 15), width=15)
    LiteracySpelling3q.grid(row=2, column=1)
    LiteracySpelling4q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling4, font=('arial', 15), width=15)
    LiteracySpelling4q.grid(row=3, column=1)
    LiteracySpelling5q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling5, font=('arial', 15), width=15)
    LiteracySpelling5q.grid(row=4, column=1)
    LiteracySpelling6q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling6, font=('arial', 15), width=15)
    LiteracySpelling6q.grid(row=5, column=1)
    LiteracySpelling7q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling7, font=('arial', 15), width=15)
    LiteracySpelling7q.grid(row=6, column=1)
    LiteracySpelling8q = Entry(LeftLiteracySpellingTestForm, textvariable=LiteracySpelling8, font=('arial', 15), width=15)
    LiteracySpelling8q.grid(row=7, column=1)
    LiteracySpelling9q = Entry(MidLiteracySpellingTestForm, textvariable=LiteracySpelling9, font=('arial', 15), width=15)
    LiteracySpelling9q.grid(row=8, column=1)
    LiteracySpelling10q = Entry(MidLiteracySpellingTestForm, textvariable=LiteracySpelling10, font=('arial', 15), width=15)
    LiteracySpelling10q.grid(row=9, column=1)

    btn_LiteracySpellingTest = Button(MidLiteracySpellingTestForm, text="Complete", font=('arial', 18), width=30, command=CompleteLiteracySpelling)
    btn_LiteracySpellingTest.grid(row=10, columnspan=2, pady=20)#add one to row from previous row count
    btn_LiteracySpellingTest.bind('<Return>', Login)

def NumeracyTestWritten():
    global numeracytestwrittenform
    numeracytestwrittenform = Toplevel()
    numeracytestwrittenform.title("Recruitment/Numeracy Test Written")
    width = 800
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    numeracytestwrittenform.resizable(0,0)
    numeracytestwrittenform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    NumeracyTestWrittenForm()

def NumeracyTestWrittenForm():
    global lbl_result
    TopNumeracyTestWrittenForm = Frame(numeracytestwrittenform, width=6000, height=100, bd=1, relief=SOLID)
    TopNumeracyTestWrittenForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopNumeracyTestWrittenForm, text="Numeracy Test Written Form", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftNumeracyTestWrittenForm = Frame(numeracytestwrittenform, width=600)
    LeftNumeracyTestWrittenForm.pack(side=LEFT, pady=50)
    MidNumeracyTestWrittenForm = Frame(numeracytestwrittenform, width=600)
    MidNumeracyTestWrittenForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe NumeracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftNumeracyTestWrittenForm, text="Question 1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftNumeracyTestWrittenForm, text="Question 2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftNumeracyTestWrittenForm, text="Question 3:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_4= Label(LeftNumeracyTestWrittenForm, text="Question 4:", font=('arial', 15), bd=18)
    lbl_4.grid(row=3)
    lbl_5= Label(LeftNumeracyTestWrittenForm, text="Question 5:", font=('arial', 15), bd=18)
    lbl_5.grid(row=4)
    lbl_6= Label(LeftNumeracyTestWrittenForm, text="Question 6:", font=('arial', 15), bd=18)
    lbl_6.grid(row=5)
    lbl_7= Label(LeftNumeracyTestWrittenForm, text="Question 7:", font=('arial', 15), bd=18)
    lbl_7.grid(row=6)
    lbl_8= Label(LeftNumeracyTestWrittenForm, text="Question 8:", font=('arial', 15), bd=18)
    lbl_8.grid(row=7)
    lbl_9= Label(MidNumeracyTestWrittenForm, text="Question 9:", font=('arial', 15), bd=18)
    lbl_9.grid(row=8)
    lbl_10 = Label(MidNumeracyTestWrittenForm, text="Question 10:", font=('arial', 15), bd=18)
    lbl_10.grid(row=9)
    lbl_11 = Label(MidNumeracyTestWrittenForm, text="Question 11:", font=('arial', 15), bd=18)
    lbl_11.grid(row=10)
    lbl_12 = Label(MidNumeracyTestWrittenForm, text="Question 12:", font=('arial', 15), bd=18)
    lbl_12.grid(row=11)
    lbl_result = Label(MidNumeracyTestWrittenForm, text="", font=('arial', 18))
    lbl_result.grid(row=15, columnspan=2)#add 3 from previous row count

    NumeracyWritten1 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq1, font=('arial', 15), width=15)
    NumeracyWritten1.grid(row=0, column=1)
    NumeracyWritten2 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq2, font=('arial', 15), width=15)
    NumeracyWritten2.grid(row=1, column=1)
    NumeracyWritten3 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq3, font=('arial', 15), width=15)
    NumeracyWritten3.grid(row=2, column=1)
    NumeracyWritten4 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq4, font=('arial', 15), width=15)
    NumeracyWritten4.grid(row=3, column=1)
    NumeracyWritten5 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq5, font=('arial', 15), width=15)
    NumeracyWritten5.grid(row=4, column=1)
    NumeracyWritten6 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq6, font=('arial', 15), width=15)
    NumeracyWritten6.grid(row=5, column=1)
    NumeracyWritten7 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq7, font=('arial', 15), width=15)
    NumeracyWritten7.grid(row=6, column=1)
    NumeracyWritten8 = Entry(LeftNumeracyTestWrittenForm, textvariable=NumeracyWrittenq8, font=('arial', 15), width=15)
    NumeracyWritten8.grid(row=7, column=1)
    NumeracyWritten9 = Entry(MidNumeracyTestWrittenForm, textvariable=NumeracyWrittenq9, font=('arial', 15), width=15)
    NumeracyWritten9.grid(row=8, column=1)
    NumeracyWritten10 = Entry(MidNumeracyTestWrittenForm, textvariable=NumeracyWrittenq10, font=('arial', 15), width=15)
    NumeracyWritten10.grid(row=9, column=1)
    NumeracyWritten11 = Entry(MidNumeracyTestWrittenForm, textvariable=NumeracyWrittenq11, font=('arial', 15), width=15)
    NumeracyWritten11.grid(row=10, column=1)
    NumeracyWritten12 = Entry(MidNumeracyTestWrittenForm, textvariable=NumeracyWrittenq12, font=('arial', 15), width=15)
    NumeracyWritten12.grid(row=11, column=1)

    btn_NumeracyWrittenTest = Button(MidNumeracyTestWrittenForm, text="Complete", font=('arial', 18), width=30, command=CompleteNumeracyWrittentest)
    btn_NumeracyWrittenTest.grid(row=12, columnspan=2, pady=20)#add one to row from previous row count
    btn_NumeracyWrittenTest.bind('<Return>', Login)

def NumeracyTestMental():
    global numeracytestform
    numeracytestform = Toplevel()
    numeracytestform.title("Recruitment/Numeracy Mental Test")
    width = 800
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    numeracytestform.resizable(0,0)
    numeracytestform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    NumeracyTestMentalForm()

def NumeracyTestMentalForm():
    global lbl_result
    TopNumeracyTestForm = Frame(numeracytestform, width=6000, height=100, bd=1, relief=SOLID)
    TopNumeracyTestForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopNumeracyTestForm, text="Numeracy Test Mental Form", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    LeftNumeracyTestForm = Frame(numeracytestform, width=600)
    LeftNumeracyTestForm.pack(side=LEFT, pady=50)
    MidNumeracyTestForm = Frame(numeracytestform, width=600)
    MidNumeracyTestForm.pack(side=TOP, pady=50)

    osCommandString = "notepad.exe NumeracyTest.txt"
    os.system(osCommandString)

    lbl_1= Label(LeftNumeracyTestForm, text="Question 1:", font=('arial', 15), bd=18)
    lbl_1.grid(row=0)
    lbl_2= Label(LeftNumeracyTestForm, text="Question 2:", font=('arial', 15), bd=18)
    lbl_2.grid(row=1)
    lbl_3= Label(LeftNumeracyTestForm, text="Question 3:", font=('arial', 15), bd=18)
    lbl_3.grid(row=2)
    lbl_4= Label(LeftNumeracyTestForm, text="Question 4:", font=('arial', 15), bd=18)
    lbl_4.grid(row=3)
    lbl_5= Label(LeftNumeracyTestForm, text="Question 5:", font=('arial', 15), bd=18)
    lbl_5.grid(row=4)
    lbl_6= Label(LeftNumeracyTestForm, text="Question 6:", font=('arial', 15), bd=18)
    lbl_6.grid(row=5)
    lbl_7= Label(LeftNumeracyTestForm, text="Question 7:", font=('arial', 15), bd=18)
    lbl_7.grid(row=6)
    lbl_8= Label(LeftNumeracyTestForm, text="Question 8:", font=('arial', 15), bd=18)
    lbl_8.grid(row=7)
    lbl_9= Label(MidNumeracyTestForm, text="Question 9:", font=('arial', 15), bd=18)
    lbl_9.grid(row=8)
    lbl_10 = Label(MidNumeracyTestForm, text="Question 10:", font=('arial', 15), bd=18)
    lbl_10.grid(row=9)
    lbl_11 = Label(MidNumeracyTestForm, text="Question 11:", font=('arial', 15), bd=18)
    lbl_11.grid(row=10)
    lbl_12 = Label(MidNumeracyTestForm, text="Question 12:", font=('arial', 15), bd=18)
    lbl_12.grid(row=11)
    lbl_13 = Label(MidNumeracyTestForm, text="Question 13:", font=('arial', 15), bd=18)
    lbl_13.grid(row=12)
    lbl_14 = Label(MidNumeracyTestForm, text="Question 14:", font=('arial', 15), bd=18)
    lbl_14.grid(row=13)
    lbl_15 = Label(MidNumeracyTestForm, text="Question 15:", font=('arial', 15), bd=18)
    lbl_15.grid(row=14)
    lbl_result = Label(MidNumeracyTestForm, text="", font=('arial', 18))
    lbl_result.grid(row=17, columnspan=2)#add 3 from previous row count

    NumeracyMental1 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq1, font=('arial', 15), width=15)
    NumeracyMental1.grid(row=0, column=1)
    NumeracyMental2 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq2, font=('arial', 15), width=15)
    NumeracyMental2.grid(row=1, column=1)
    NumeracyMental3 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq3, font=('arial', 15), width=15)
    NumeracyMental3.grid(row=2, column=1)
    NumeracyMental4 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq4, font=('arial', 15), width=15)
    NumeracyMental4.grid(row=3, column=1)
    NumeracyMental5 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq5, font=('arial', 15), width=15)
    NumeracyMental5.grid(row=4, column=1)
    NumeracyMental6 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq6, font=('arial', 15), width=15)
    NumeracyMental6.grid(row=5, column=1)
    NumeracyMental7 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq7, font=('arial', 15), width=15)
    NumeracyMental7.grid(row=6, column=1)
    NumeracyMental8 = Entry(LeftNumeracyTestForm, textvariable=NumeracyMentalq8, font=('arial', 15), width=15)
    NumeracyMental8.grid(row=7, column=1)
    NumeracyMental9 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq9, font=('arial', 15), width=15)
    NumeracyMental9.grid(row=8, column=1)
    NumeracyMental10 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq10, font=('arial', 15), width=15)
    NumeracyMental10.grid(row=9, column=1)
    NumeracyMental11 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq11, font=('arial', 15), width=15)
    NumeracyMental11.grid(row=10, column=1)
    NumeracyMental12 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq12, font=('arial', 15), width=15)
    NumeracyMental12.grid(row=11, column=1)
    NumeracyMental13 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq13, font=('arial', 15), width=15)
    NumeracyMental13.grid(row=12, column=1)
    NumeracyMental14 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq14, font=('arial', 15), width=15)
    NumeracyMental14.grid(row=13, column=1)
    NumeracyMental15 = Entry(MidNumeracyTestForm, textvariable=NumeracyMentalq15, font=('arial', 15), width=15)
    NumeracyMental15.grid(row=14, column=1)

    btn_NumeracyTest = Button(MidNumeracyTestForm, text="Complete", font=('arial', 18), width=30, command=CompleteNumeracytest)
    btn_NumeracyTest.grid(row=15, columnspan=2, pady=20)#add one to row from previous row count
    btn_NumeracyTest.bind('<Return>', Login)

def ShowViewJobsAdmin():
    global viewformjobs
    viewformjobs = Toplevel()
    viewformjobs.title("Recruitment/View Product")
    width = 800
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewformjobs.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewformjobs.resizable(0, 0)
    ViewFormJobs()

def ShowViewJobs():
    global viewformjobs
    viewformjobs = Toplevel()
    viewformjobs.title("Recruitment/View Product")
    width = 800
    height = 400
    screen_width = HomeEmp.winfo_screenwidth()
    screen_height = HomeEmp.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewformjobs.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewformjobs.resizable(0, 0)
    ViewFormJobs()

def ViewFormJobs():
    global treejobs
    TopViewFormJobs = Frame(viewformjobs, width=800, bd=1, relief=SOLID)
    TopViewFormJobs.pack(side=TOP, fill=X)
    LeftViewFormJobs = Frame(viewformjobs, width=600)
    LeftViewFormJobs.pack(side=LEFT, fill=Y)
    MidViewFormJobs = Frame(viewformjobs, width=600)
    MidViewFormJobs.pack(side=RIGHT)
    lbl_textjobs = Label(TopViewFormJobs, text="View Available Jobs", font=('arial', 18), width=600)
    lbl_textjobs.pack(fill=X)
    lbl_txtsearchjobs = Label(LeftViewFormJobs, text="Search", font=('arial', 15))
    lbl_txtsearchjobs.pack(side=TOP, anchor=W)
    searchjobs = Entry(LeftViewFormJobs, textvariable=SEARCHJOBS, font=('arial', 15), width=10)
    searchjobs.pack(side=TOP,  padx=10, fill=X)
    btn_searchjobs = Button(LeftViewFormJobs, text="Search", command=SearchJobs)
    btn_searchjobs.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewFormJobs, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewFormJobs, orient=VERTICAL)
    treejobs = ttk.Treeview(MidViewFormJobs, columns=("ID", "Job Title", "Contract Start Date", "Contract End Date", "Starting Salary", "Brief Description"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=treejobs.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=treejobs.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    treejobs.heading('ID', text="ID",anchor=W)
    treejobs.heading('Job Title', text="Job Title",anchor=W)
    treejobs.heading('Contract Start Date', text="Contract Start Date",anchor=W)
    treejobs.heading('Contract End Date', text="Contract End Date",anchor=W)
    treejobs.heading('Starting Salary', text="Starting Salary",anchor=W)
    treejobs.heading('Brief Description', text="Brief Description",anchor=W)
    treejobs.column('#0', stretch=NO, minwidth=0, width=0)
    treejobs.column('#1', stretch=NO, minwidth=0, width=20)
    treejobs.column('#2', stretch=NO, minwidth=0, width=100)
    treejobs.column('#3', stretch=NO, minwidth=0, width=120)
    treejobs.column('#4', stretch=NO, minwidth=0, width=120)
    treejobs.column('#5', stretch=NO, minwidth=0, width=120)
    treejobs.column('#5', stretch=NO, minwidth=0, width=120)
    treejobs.pack()

    if admin_id != "":
        btn_deletejobs = Button(LeftViewFormJobs, text="Delete", command=DeleteJobs)
        btn_deletejobs.pack(side=TOP, padx=10, pady=10, fill=X)
    DisplayDataJobs()

def DeleteJobs():
    if not treejobs.selection() and admin_id != "":
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = treejobs.focus()
            contents =(treejobs.item(curItem))
            selecteditem = contents['values']
            treejobs.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `Available_Jobs` WHERE `job_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def DisplayDataJobs():
    Database()
    cursor.execute("SELECT * FROM `Available_Jobs`")
    fetch = cursor.fetchall()
    for data in fetch:
        treejobs.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SearchJobs():
    if SEARCHJOBS.get() != "":
        treejobs.delete(*treejobs.get_children())
        Database()
        cursor.execute("SELECT * FROM `Available_Jobs` WHERE `Job Title` LIKE ?", ('%'+str(SEARCHJOBS.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            treejobs.insert('', 'end', values=(data))
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

def Logout():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()

def LogoutEmp():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        employee_id = ""
        root.deiconify()
        HomeEmp.destroy()

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

def Loginemp(event=None):
    global emp_id
    Database()
    if USERNAMEemplogin.get == "" or PASSWORDemplogin.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `UFIX_PIM` WHERE `Username` = ? AND `Password` = ?", (USERNAMEemplogin.get(), PASSWORDemplogin.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `UFIX_PIM` WHERE `Username` = ? AND `Password` = ?", (USERNAMEemplogin.get(), PASSWORDemplogin.get()))
            data = cursor.fetchone()
            emp_id = data[0]
            USERNAMEemplogin.set("")
            PASSWORDemplogin.set("")
            lbl_result.config(text="")
            ShowHomeEmp()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAMEemplogin.set("")
            PASSWORDemplogin.set("")
    cursor.close()
    conn.close()

def Register(event=None):
    Database()
    if USERNAMEemp.get == "" or PASSWORDemp.get() == "" or DOBemp.get() == "" or FirstNameemp.get()==""or LastNameemp.get()=="" or ContactNumberemp.get()=="" or EmailAddressemp.get()=="" or AddressLine1emp.get()=="" or AddressLine2emp.get()=="" or Countryemp.get()=="" or PostCodeemp=="":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'UFIX_PIM'(Username,Password,Date_of_Birth,First_name,last_name,Contact_number,Email_Address,Address_line1,Address_line2,Country,Postcode) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(str(USERNAMEemp.get()),str(PASSWORDemp.get()),str(DOBemp.get()),str(FirstNameemp.get()),str(LastNameemp.get()),str(ContactNumberemp.get()),str(EmailAddressemp.get()),str(AddressLine1emp.get()),str(AddressLine2emp.get()),str(Countryemp.get()),str(PostCodeemp.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteNumeracytest(event=None):
    Database()
    if NumeracyMentalq1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'NumeracyTestMental'('emp_id','Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10', 'Question 11', 'Question 12', 'Question 13', 'Question 14', 'Question 15') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(emp_id,str(NumeracyMentalq1.get()),str(NumeracyMentalq2.get()),str(NumeracyMentalq3.get()),str(NumeracyMentalq4.get()),str(NumeracyMentalq5.get()),str(NumeracyMentalq6.get()),str(NumeracyMentalq7.get()),str(NumeracyMentalq8.get()),str(NumeracyMentalq9.get()),str(NumeracyMentalq10.get()),str(NumeracyMentalq11.get()),str(NumeracyMentalq12.get()),str(NumeracyMentalq13.get()),str(NumeracyMentalq14.get()),str(NumeracyMentalq15.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteNumeracyWrittentest(event=None):
    Database()
    if NumeracyWrittenq1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'NumeracyTestWritten'('emp_id','Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10', 'Question 11', 'Question 12') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(emp_id,str(NumeracyWrittenq1.get()),str(NumeracyWrittenq2.get()),str(NumeracyWrittenq3.get()),str(NumeracyWrittenq4.get()),str(NumeracyWrittenq5.get()),str(NumeracyWrittenq6.get()),str(NumeracyWrittenq7.get()),str(NumeracyWrittenq8.get()),str(NumeracyWrittenq9.get()),str(NumeracyWrittenq10.get()),str(NumeracyWrittenq11.get()),str(NumeracyWrittenq12.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteLiteracySpelling(event=None):
    Database()
    if LiteracySpelling1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracySpelling'('emp_id','Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10') VALUES(?,?,?,?,?,?,?,?,?,?,?)",(emp_id,str(LiteracySpelling1.get()),str(LiteracySpelling2.get()),str(LiteracySpelling3.get()),str(LiteracySpelling4.get()),str(LiteracySpelling5.get()),str(LiteracySpelling6.get()),str(LiteracySpelling7.get()),str(LiteracySpelling8.get()),str(LiteracySpelling9.get()),str(LiteracySpelling10.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteLiteracyGrammarPartA(event=None):
    Database()
    if LiteracyGrammarPartA1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracyGrammarPartA'('emp_id','Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5') VALUES(?,?,?,?,?,?)",(emp_id,str(LiteracyGrammarPartA1.get()),str(LiteracyGrammarPartA2.get()),str(LiteracyGrammarPartA3.get()),str(LiteracyGrammarPartA4.get()),str(LiteracyGrammarPartA5.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteLiteracyGrammarPartB(event=None):
    Database()
    if LiteracyGrammarPartB1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracyGrammarPartB'('emp_id','Question 1', 'Question 2') VALUES(?,?,?)",(emp_id,str(LiteracyGrammarPartB1.get()),str(LiteracyGrammarPartB2.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteLiteracyGrammarPartC(event=None):
    Database()
    if LiteracyGrammarPartC1.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracyGrammarPartC'('emp_id','Question 1', 'Question 2', 'Question 3') VALUES(?,?,?,?)",(emp_id,str(LiteracyGrammarPartC1.get()),str(LiteracyGrammarPartC2.get()),str(LiteracyGrammarPartC3.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def CompleteLiteracyPunctuationForm(event=None):
    Database()
    if LiteracyPunctuationText.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracyPunctuation'('emp_id','Text') VALUES(?,?)",(emp_id,str(LiteracyPunctuationText.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()


def CompleteLiteracyComprehension(event=None):
    Database()
    if LiteracyComprehensionA.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO 'LiteracyComprehension'('emp_id','Part A', 'Part B', 'Part C', 'Part D') VALUES(?,?,?,?,?)",(emp_id,str(LiteracyComprehensionA.get()),str(LiteracyComprehensionB.get()),str(LiteracyComprehensionC.get()),str(LiteracyComprehensionD.get())))
        conn.commit()
        lbl_result.config(text="Successful!", fg="green")
    cursor.close()
    conn.close()

def PolicyView(event=None):
    tkMessageBox.showinfo('Policies', 'Our policy to make sure the use of our\n software and that the recruiting process is relatively easy and simple to use.\nAs part of a recruitment team there are many rules to follow within the law\nsuch as the newly updated GDPR laws. This is one of the most important laws\nto follow as a lot of personal data will be collected about each applicant. This\ndata must be stored securely where it can’t be exposed to anyone other than\nthe appropriate users.\nAs Brainvire is a big company and several different teams we all have different\npolicies within each group. Our policy will go through everything we expect\nfrom our employees and from everyone that will be using the software\nprovided by us.\n“Brainvire Ltd” is committed to:\n- Viewing all entries for positions as equals and only taking in the best of\nthe best.\n- Providing potential new employees with fair numeracy and literacy tests\nto help the process of elimination.\n- Promoting continual quality of improvement and the philosophy of\ngetting things “right the first time”.')

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

def ShowHomeEmp():
    root.withdraw()
    HomeEmp()
    loginempform.destroy()

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar, tearoff=0)
filemenu3 = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin Login", command=ShowExistingAdminForm)
filemenu.add_command(label="Employee Login", command=ShowExistingempForm)
filemenu2.add_command(label="New Employee", command=ShowNewEmpForm)
filemenu3.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Login", menu=filemenu)
menubar.add_cascade(label="Register", menu=filemenu2)
menubar.add_cascade(label="Exit", menu=filemenu3)
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
