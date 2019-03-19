from tkinter import *
import sqlite3


global prev
prev = 0


def mainMenu():
    closeprev()
    global screen
    screen = Tk()
    screen.geometry("350x400")
    screen.title("Menu")
    Label(screen, text="Staff register", bg="black", fg="white", width=500, height = 2, font=("calibri", 18)).pack()
    Label(screen).pack()
    Label(screen).pack()
    Label(screen).pack()
    Button(screen, text="Sign in", borderwidth=2, relief="solid",  height=3, width="35", bg="white", fg="black", font=("calibri", 12), command=loginForm).pack()
    Label(screen).pack()
    Button(screen, text="Sign out", borderwidth=2, relief="solid", height="3", width="35", bg="white", fg="black", font=("calibri", 12), command=logoutForm).pack()
    Label(screen).pack()
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

def loginForm():
    global prev
    prev=1
    screen.destroy()
    global  screen1
    screen1 = Tk()
    screen1.title("Sign in")
    screen1.geometry("350x400")

    username=StringVar()
    password=StringVar()

    Label(screen1, text="Login", bg="white", fg="black", width=500, height="2", font=("calibri", 18)).pack()
    Label(screen1).pack()
    Label(screen1).pack()
    Label(screen1, text = "Employee ID", bg="black", fg="white", width="300", height=1, font=("calibri", 12)).pack()
    Entry(screen1, textvariable = username, width="300", bg="white", fg="black", font=("calibri", 16)).pack()
    Label(screen1).pack()
    Label(screen1, text="Password", bg="black", fg="white", width=100, height=1,  font=("calibri", 12,)).pack()
    Entry(screen1, textvariable=password,  width=150, bg="white", fg="black",  font=("calibri", 16)).pack()
    Label(screen1).pack()
    Label(screen1).pack()
    Button(screen1, text="log in", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=login).pack()
    Label(screen1).pack()
    Button(screen1, text="cancel", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=mainMenu).pack()

def logoutForm():
    global prev
    prev = 2
    global screen2
    screen.destroy()
    screen2 = Tk()
    screen2.title("Sign out")
    screen2.geometry("350x400")

    username = StringVar()
    password = StringVar()

    Label(screen2, text="Log out", bg="white", fg="black", width=500, height="2", font=("calibri", 18)).pack()
    Label(screen2).pack()
    Label(screen2).pack()
    Label(screen2, text="Employee ID", bg="black", fg="white", width="300", height=1, font=("calibri", 12)).pack()
    Entry(screen2, textvariable=username, width="300", bg="white", fg="black", font=("calibri", 16)).pack()
    Label(screen2).pack()
    Label(screen2, text="Password", bg="black", fg="white", width=100, height=1, font=("calibri", 12,)).pack()
    Entry(screen2, textvariable=password, width=100, bg="white", fg="black", font=("calibri", 16)).pack()
    Label(screen2).pack()
    Label(screen2).pack()
    Button(screen2, text="log out", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=logout).pack()
    Label(screen2).pack()
    Button(screen2, text="cancel", borderwidth=2, relief="solid", height=1, width="35", bg="white", fg="black",
           font=("calibri", 12), command=mainMenu).pack()

def closeprev():
    if prev == 1:
        screen1.destroy()
    elif prev == 2:
        screen2.destroy()
    elif prev == 3:
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
        print (results)

        if results:
            for i in results:
                print ("welcome " + i[2])
            return ("exit")

        else:
            print("Username and password not recognised")
            return ("exit")
        #print("checking credentials")
        #print("allowed")
        #print("logging in/out")


mainMenu()


