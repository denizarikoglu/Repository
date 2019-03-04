import json
import sqlite3
import webbrowser
from tkinter import *
import os

window = Tk()
window.title("Welcome to Ufix")
window.geometry('550x500')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 900
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)


#==================================METHODS============================================
def callback(event):
    os.system("policies.py")
def Database():
    global conn, cursor
    conn = sqlite3.connect("Ufixltd.s3db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Employee` (idEmployee INTEGER PRIMARY KEY  AUTOINCREMENT ,firstNameEmployee	VARCHAR ( 50 ),lastNameEmployee	VARCHAR ( 50 ),emailEmployee	VARCHAR ( 50 ),phoneEmployee	VARCHAR ( 20 ),idTeam	VARCHAR(50),log	VARCHAR(50),pass    VARCHAR(50),connect     INTEGER)")
def leave():
    os.system("offBoarding.py")
def timetable():
    os.system("timetable.py")
def Admin():
    os.system("connect.py")
def map():
    fen2 = Toplevel()
    fen2.title("Map")
    img = PhotoImage(file="Images/map.png")
    Image = Label(fen2, image=img)
    Image.pack()
    fen2.mainloop()
def callback(event):
    os.system("policies.py")
def Team():
    Database()
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        id = data["user"]
        cursor.execute("SELECT teamName FROM `Team` where idTeam = (SELECT idTeam FROM Employee where idEmployee ='" + id + "' )")
    fetch = cursor.fetchone()
    if fetch[0] == "Admin":
        buttonAdmin = Button(labelService, text="Admin", width=20, cursor="hand2", command=Admin)
        buttonAdmin.pack()

#==================================FRAME==============================================
Top = Frame(window, width=900, height=150)
Top.pack(side=TOP)
Middle = Frame(window, width=900, height=400, bd=8)
Middle.pack()
Left = Frame(Middle, width=100, height=400, bd=8)
Left.pack(side=LEFT)
Right = Frame(Middle, width=800, height=400, bd=8)
Right.pack(side=RIGHT)
RightTop = Frame(Right, width=800, height=150)
RightTop.pack(side=TOP)
RightMiddle = Frame(Right, width=800, height=150)
RightMiddle.pack()
RightBottom = Frame(Right, width=800, height=100)
RightBottom.pack(side=BOTTOM)
RightBottomL = Frame(RightBottom, width=200, height=100)
RightBottomL.pack(side=RIGHT)
RightBottomR = Frame(RightBottom, width=200, height=100)
RightBottomR.pack(side=LEFT)
Bottom = Frame(window, width=900, height=50, bd=4)
Bottom.pack(side=BOTTOM)

#==================================LIST WIDGET========================================
img = PhotoImage(file="Images/UfixLogo.png")

#==================================LABEL WIDGET========================================
labelImage = Label(Top, image=img)
labelImage.pack()
label = LabelFrame(RightTop, text="Welcome To Ufix", font=("Arial Bold", 20))
label.pack(fill="both", expand="yes")

#ufix introduction
introUfix_text = Label(label, font=("arial", 10), bg="#A9A9A9", height=5, width=80, text="The Presentation Company's training workshops are always well-paced,\n informative and a fantastic use of our time.\n Their customized approach and use of before and after examples helped\n transform our marketing team into more knowledgeable and effective\n PowerPoint presenters.")
introUfix_text.pack()

labelService = LabelFrame(RightMiddle, text="ACCESS TO SERVICES", font=("Arial Bold", 15))
labelService.pack(fill="both", expand="yes")
labelNew = LabelFrame(RightBottomR, text="News", font=("Arial Bold", 10))
labelNew.pack(fill="both", expand="yes")
labelEvent = LabelFrame(RightBottomL, text="Events", font=("Arial Bold", 10))
labelEvent.pack(fill="both", expand="yes")


link = Label(Bottom, width=900, text="Policies", fg="blue", cursor="hand2")
link.bind("<Button-1>", callback)
link.pack()
linkNew = Label(labelNew, text="News", fg="blue", cursor="hand2")
linkNew.pack()
linkEvent = Label(labelEvent, text="Event", fg="blue", cursor="hand2")
linkEvent.pack()

#==================================BUTTONS WIDGET=====================================
buttonPD = Button(Left, text="Personal details", width=20, cursor="hand2")
buttonPD.pack()
buttonTT = Button(Left, text="Timetable", width=20, cursor="hand2", command=timetable)
buttonTT.pack()
buttonWT = Button(Left, text="Work Team", width=20, cursor="hand2")
buttonWT.pack()
buttonMap = Button(Left, text="Map", width=20, cursor="hand2", command=map)
buttonMap.pack()
buttonDev = Button(Left, text="Devices", width=20, cursor="hand2")
buttonDev.pack()


buttonP = Button(labelService, text="PayRoll", width=20, cursor="hand2")
buttonP.pack()
buttonOFF = Button(labelService, text="OFF Boarding", width=20, cursor="hand2", command=leave)
buttonOFF.pack()
buttonL = Button(labelService, text="Leave System", width=20, cursor="hand2")
buttonL.pack()


#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    Team()
    mainloop()


