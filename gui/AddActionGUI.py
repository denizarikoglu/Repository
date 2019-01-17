from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

#from Gui import Databse_Disciplinary_list

root = Tk()
root.title("Dispinary : Add new action")  # name for the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def Databse_Disciplinary_list():
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Disciplinary_list' (emp id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Discipline_Name TEXT, Reson_for_Action TEXT, Action_Taken TEXT, Severity_Level INTERGER)")
    #conncts the list table

# ==================================FRAME==============================================

Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)

root.mainloop()
