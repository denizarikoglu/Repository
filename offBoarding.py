from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import webbrowser
import os


root = Tk()
root.title("OFF Boarding Page")
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
    conn = sqlite3.connect('Ufixltd.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Questionnaire` (idQuestionnaire INTEGER PRIMARY KEY  AUTOINCREMENT ,firstAnswer	VARCHAR ( 50 ),SecondAnswer	VARCHAR ( 50 ),thridAnswer	VARCHAR ( 50 ),lastAnswer	VARCHAR ( 50 ),comment	VARCHAR(500))")

def Questionnaire():
    print(3)

def Exit():
    result = tkMessageBox.askquestion('Welcome page', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def callback(event):
    ##webbrowser.open_new(r"Policies\Policies.pdf")
    os.system("policies.py")

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(root, width=900, height=400, bd=8, relief="raise")
Middle.pack()
MiddleTop = Frame(Middle, width=300, height=200, bd=8, relief="raise")
MiddleTop.pack(side=TOP)
MiddleBottom = Frame(Middle, width=600, height=200, bd=8, relief="raise")
MiddleBottom.pack(side=BOTTOM)
Bottom = Frame(root, width=300, height=50, bd=4, relief="raise")
Bottom.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "OFF Boarding Page")
txt_title.pack()
link = Label(Bottom, width=900, text="Policies", fg="blue", cursor="hand2")
link.bind("<Button-1>", callback)
link.pack()

#==================================BUTTONS WIDGET=====================================
btn_questionnaire = Button(MiddleTop, width=10, text="Questionnaire", command=Questionnaire)
btn_questionnaire.pack(side=LEFT)
btn_exit = Button(Bottom, width=10, text="Exit", command=Exit)
btn_exit.pack(side=RIGHT)

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
