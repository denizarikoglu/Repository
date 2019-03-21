from tkinter import *
from tkinter import messagebox
import sqlite3
sqlite_file = 'ufix.s3db'
with sqlite3.connect(sqlite_file) as s3db:
    c = s3db.cursor()


def calculate_total_pay():
    fetched_user = get_emps_by_ID()
    hours_worked = fetched_user[0][4]
    string_pay_rate = fetched_user[0][5]
    actual_pay_rate = ""
    for i in string_pay_rate:
        if i == '/':
            actual_pay_rate = actual_pay_rate
            break
        actual_pay_rate += i
    total_pay = int(actual_pay_rate) * hours_worked
    return total_pay

def calculate_gross_pay():
    total_pay = calculate_total_pay()
    fetched_user = get_emps_by_ID()
    string_tax_bracket = fetched_user[0][6]
    actual_tax_bracket = ""
    for i in string_tax_bracket:
        if i == '%':
            actual_tax_bracket = actual_tax_bracket
            break
        actual_tax_bracket += i
    perc_to_decimal = float(actual_tax_bracket) / 100
    num_to_sub = total_pay * perc_to_decimal
    gross_pay = total_pay - num_to_sub
    return gross_pay

def insert_emp(emp):
    with s3db:
        c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})



def update_pay(total_pay, gross_pay):
    ID = int(inputted_ID.get())
    with s3db:
        c.execute("""UPDATE Payroll SET Total_Pay = :total_pay, Gross_Pay = :gross_pay
                    WHERE ID = :ID""",
                  {'ID': ID, 'total_pay': total_pay, 'gross_pay': gross_pay})
    print("Total pay added to the database!\nGross pay added to the database!")

def remove_emp(ID):
    with s3db:
        c.execute("DELETE from Payroll WHERE ID = :ID", {'ID': ID})

global prev
prev = 0


def mainMenu():
    closeprev()
    global screen
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Menu")
    Label(screen, text="Staff register", bg="black", fg="white", width=500, height = 2, font=("calibri", 18)).pack()
    Label(screen).pack()
    Label(screen).pack()
    Button(screen, text="Admin", borderwidth=2, relief="solid", height="1", width="35", bg="white", fg="black",
           font=("calibri", 12), command=AdminLoginForm).pack()
    screen.mainloop()

def AdminForm():
    closeprev()
    global prev
    prev = 3
    global screen3
    screen3 = Tk()
    screen3.geometry("1000x600")
    screen3.title("Admin")
    global inputted_ID
    inputted_ID = StringVar()
    id_label = Label(screen3, text="ID")
    id_label.pack()
    id_entry = Entry(screen3, textvariable=inputted_ID, width=40)
    id_entry.pack()
    #the find button
    find_btn = Button(screen3, text="Find", width=16, command=find_results)
    find_btn.place(x=250, y=60)
    #the calculate pay button
    calculate_btn = Button(screen3, text="Calculate pay", command=calculate_results)
    calculate_btn.place(x=450, y=60)
    #the quit button
    quit_btn = Button(screen3, text="Exit", width=16, command=quit)
    quit_btn.place(x=600, y=60)

    screen3.mainloop()

def calculate_results():
    total_pay = calculate_total_pay()
    gross_pay = calculate_gross_pay()
    fetched_user = get_emps_by_ID()
    id = fetched_user[0][0]
    Name = fetched_user[0][1] + " " + fetched_user[0][2] + "                 "
    hours_worked = fetched_user[0][4]
    pay_rate = fetched_user[0][5]
    tax_bracket = fetched_user[0][6]
    # the results header
    result_label = Label(screen3, text="Results:-", font=("calibri", 24))
    result_label.place(x=50, y=200)
    # the id results
    id_result_label = Label(screen3, text="ID:", font=("calibri", 18))
    id_result_label.place(x=50, y=250)
    the_id_lbl = Label(screen3, text=str(id))
    the_id_lbl.place(x=100, y=260)
    # the name results
    Name_result_label = Label(screen3, text="Name:", font=("calibri", 18))
    Name_result_label.place(x=50, y=300)
    the_Name_lbl = Label(screen3, text=Name)
    the_Name_lbl.place(x=150, y=310)
    # the hours worked results
    hours_result_label = Label(screen3, text="Hours worked:", font=("calibri", 18))
    hours_result_label.place(x=50, y=350)
    the_hours_lbl = Label(screen3, text=hours_worked)
    the_hours_lbl.place(x=240, y=360)
    # the pay rate results
    payRate_result_label = Label(screen3, text="Pay rate:", font=("calibri", 18))
    payRate_result_label.place(x=50, y=400)
    the_payRate_lbl = Label(screen3, text=pay_rate)
    the_payRate_lbl.place(x=170, y=410)
    # the tax bracket results
    taxBracket_result_label = Label(screen3, text="Tax bracket:", font=("calibri", 18))
    taxBracket_result_label.place(x=50, y=450)
    the_taxBracket_lbl = Label(screen3, text=tax_bracket)
    the_taxBracket_lbl.place(x=210, y=460)
    # the total pay results
    totalPay_result_label = Label(screen3, text="Total pay:", font=("calibri", 18))
    totalPay_result_label.place(x=50, y=500)
    if total_pay == '' or total_pay == None:
        the_totalPay_lbl = Label(screen3, text="               ")
    else:
        the_totalPay_lbl = Label(screen3, text="     " + str(total_pay) + "     ")
    the_totalPay_lbl.place(x=180, y=510)
    # the gross pay results
    grossPay_result_label = Label(screen3, text="Gross pay:", font=("calibri", 18))
    grossPay_result_label.place(x=50, y=550)
    if gross_pay == '' or gross_pay == None:
        the_grossPay_lbl = Label(screen3, text="               ")
    else:
        the_grossPay_lbl = Label(screen3, text="     " + str(gross_pay) + "     ")
    the_grossPay_lbl.place(x=180, y=560)
    #add the calculated pay to database
    update_pay(total_pay, gross_pay)


def find_results():
    fetched_user = get_emps_by_ID()
    id = fetched_user[0][0]
    Name = fetched_user[0][1] + " " + fetched_user[0][2] + "               "
    hours_worked = fetched_user[0][4]
    pay_rate = fetched_user[0][5]
    tax_bracket = fetched_user[0][6]
    total_pay = fetched_user[0][7]
    gross_pay = fetched_user[0][8]
    #the results header
    global result_label
    result_label = Label(screen3, text="Results:-", font=("calibri", 24))
    result_label.place(x=50, y=200)
    #the id results
    id_result_label = Label(screen3, text="ID:", font=("calibri", 18))
    id_result_label.place(x=50, y=250)
    the_id_lbl = Label(screen3, text=str(id))
    the_id_lbl.place(x=100, y=260)
    #the name results
    Name_result_label = Label(screen3, text="Name:", font=("calibri", 18))
    Name_result_label.place(x=50, y=300)
    the_Name_lbl = Label(screen3, text=Name)
    the_Name_lbl.place(x=150, y=310)
    #the hours worked results
    hours_result_label = Label(screen3, text="Hours worked:", font=("calibri", 18))
    hours_result_label.place(x=50, y=350)
    the_hours_lbl = Label(screen3, text=hours_worked)
    the_hours_lbl.place(x=240, y=360)
    #the pay rate results
    payRate_result_label = Label(screen3, text="Pay rate:", font=("calibri", 18))
    payRate_result_label.place(x=50, y=400)
    the_payRate_lbl = Label(screen3, text=pay_rate)
    the_payRate_lbl.place(x=170, y=410)
    #the tax bracket results
    taxBracket_result_label = Label(screen3, text="Tax bracket:", font=("calibri", 18))
    taxBracket_result_label.place(x=50, y=450)
    the_taxBracket_lbl = Label(screen3, text=tax_bracket)
    the_taxBracket_lbl.place(x=210, y=460)
    # the total pay results
    totalPay_result_label = Label(screen3, text="Total pay:", font=("calibri", 18))
    totalPay_result_label.place(x=50, y=500)
    if total_pay == '' or total_pay == None:
        the_totalPay_lbl = Label(screen3, text="                  ")
    else:
        the_totalPay_lbl = Label(screen3, text=str(total_pay) + "      ")
    the_totalPay_lbl.place(x=200, y=510)
    # the gross pay results
    grossPay_result_label = Label(screen3, text="Gross pay:", font=("calibri", 18))
    grossPay_result_label.place(x=50, y=550)
    if gross_pay == '' or gross_pay == None:
        the_grossPay_lbl = Label(screen3, text="                   ")
    else:
        the_grossPay_lbl = Label(screen3, text=str(gross_pay) + "      ")
    the_grossPay_lbl.place(x=200, y=560)




def get_emps_by_ID():
    ID = int(inputted_ID.get())
    c.execute("SELECT * FROM Payroll WHERE ID = :ID", {'ID': ID})
    fetched_user = c.fetchall()
    if len(fetched_user) == 0:
        messagebox.showinfo("Not Found!", "No Employee Found!!")
        return
    else:
        return fetched_user

def AdminLoginForm():
    global prev
    prev = 4
    screen.destroy()
    global screen4
    screen4 = Tk()
    screen4.title("Admin Sign in")
    screen4.geometry("1000x600")

    global username
    global  password

    username=StringVar()
    password=StringVar()

    Label(screen4, text="Admin", bg="white", fg="black", width=500, height="2", font=("calibri", 18)).pack()
    Label(screen4).pack()
    Label(screen4).pack()
    Label(screen4, text = "Username", fg="black", width=35, height=1, font=("calibri", 12)).pack()
    Entry(screen4, textvariable=username, width=26, bg="white", fg="black", font=("calibri", 16)).pack()
    Label(screen4).pack()
    Label(screen4, text="Password", fg="black", width=35, height=1,  font=("calibri", 12,)).pack()
    Entry(screen4, textvariable=password,  width=26, bg="white", fg="black",  font=("calibri", 16)).pack()
    Label(screen4).pack()
    Label(screen4).pack()
    Button(screen4, text="log in", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=login).pack()
    Label(screen4).pack()
    Button(screen4, text="cancel", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=mainMenu).pack()


def closeprev():
    if prev == 3:
        screen3.destroy()
    elif prev == 4:
        screen4.destroy()

def login():
    checkcredentials()

def logout():
    checkcredentials()

def checkcredentials():
    while True:
        username_input = username.get()
        password_input = password.get()
        with s3db:
            cursor = s3db.cursor()
        find_user = ("SELECT * FROM UFIX_PIM WHERE username =? AND password = ?")
        cursor.execute(find_user,[(username_input), (password_input)])
        results = cursor.fetchall()
        #print (results)

        if results:
            for i in results:
                print("welcome " + i[2])
                AdminForm()
            return ("exit")

        else:
            print("Username and password not recognised")
            return ("exit")
        #print("checking credentials")
        #print("allowed")
        #print("logging in/out")

mainMenu()

s3db.close()
