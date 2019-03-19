from tkinter import *
import sqlite3


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
        with sqlite3.connect('ufix.s3db') as s3db:
            cursor = s3db.cursor()
        find_user = ("SELECT * FROM UFIX_PIM WHERE username =? AND password = ?")
        cursor.execute(find_user,[(username_input), (password_input)])
        results = cursor.fetchall()
        #print (results)

        if results:
            for i in results:
                print ("welcome " + i[2])
                AdminForm()
            return ("exit")

        else:
            print("Username and password not recognised")
            return ("exit")
        #print("checking credentials")
        #print("allowed")
        #print("logging in/out")


mainMenu()


