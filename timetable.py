import json
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import hashlib
import os


root = Tk()
root.title("GUI")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 300
height = 300
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("Ufixltd.s3db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `TimeTable` (day VARCHAR ( 20 ) PRIMARY KEY,idTeam	INTEGER,hourStart	NUMERIC,hourFinish   NUMERIC)")

def TimeTable():
    Database()
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        id = data["user"]
    cursor.execute(
        "SELECT * FROM `TimeTable` where idTeam = (SELECT idTeam FROM Employee where idEmployee ='" + id + "' )")
    fetch = cursor.fetchall()
    for data in fetch:
        start = data[2] - 5
        temp = data[3] - 5
        if data[0] == "Monday":
            colonne = 2
        if data[0] == "Thuesday":
            colonne = 3
        if data[0] == "Wenesday":
            colonne = 4
        if data[0] == "Thursday":
            colonne = 5
        if data[0] == "Friday":
            colonne = 6
        for line in range(start, temp):
            Label(root, bg="red", borderwidth=1, width=5).grid(row=line, column=colonne)
    cursor.close()
    conn.close()

#==================================FRAME==============================================

#==================================LABEL WIDGET=======================================


#==================================ENTRY WIDGET=======================================


#==================================BUTTONS WIDGET=====================================
Label(root, text='Monday', borderwidth=1).grid(row=1, column=2)
Label(root, text='Thuesday', borderwidth=1).grid(row=1, column=3)
Label(root, text='Wenesday', borderwidth=1).grid(row=1, column=4)
Label(root, text='Thursday', borderwidth=1).grid(row=1, column=5)
Label(root, text='Friday', borderwidth=1).grid(row=1, column=6)
Label(root, text='7:00', borderwidth=1).grid(row=2, column=1)
Label(root, text='8:00', borderwidth=1).grid(row=3, column=1)
Label(root, text='9:00', borderwidth=1).grid(row=4, column=1)
Label(root, text='10:00', borderwidth=1).grid(row=5, column=1)
Label(root, text='11:00', borderwidth=1).grid(row=6, column=1)
Label(root, text='12:00', borderwidth=1).grid(row=7, column=1)
Label(root, text='13:00', borderwidth=1).grid(row=8, column=1)
Label(root, text='14:00', borderwidth=1).grid(row=9, column=1)
Label(root, text='15:00', borderwidth=1).grid(row=10, column=1)
Label(root, text='16:00', borderwidth=1).grid(row=11, column=1)
Label(root, text='17:00', borderwidth=1).grid(row=12, column=1)
Label(root, text='18:00', borderwidth=1).grid(row=13, column=1)
Label(root, text='19:00', borderwidth=1).grid(row=14, column=1)
Label(root, text='20:00', borderwidth=1).grid(row=15, column=1)

#==================================LIST WIDGET========================================

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    TimeTable()
    root.mainloop()

