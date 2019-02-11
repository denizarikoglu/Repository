# AUTHOR: Matthew Fowler
# CONTACT: 17025958@students.southwales.ac.uk

# This is a scrip to provide the "add / edit disciplinary action" GUI. This will
# not associate disciplinary actions or notices with specific employees, but will
#

from tkinter import*
import tkinter.ttk as ttk
import sqlite3
import os
# import tkinter.ttk as ttk
# import tkinter.messagebox as tkMessageBox

# from Gui import Databse_Disciplinary_list

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


# from the "GUI.py" script, written by Joshua
def Databse_Disciplinary_list():
    global conn, cursor
    conn = sqlite3.connect('UfixLtd.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Disciplinary_list' (emp id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Discipline_Name TEXT, Reson_for_Action TEXT, Action_Taken TEXT, Severity_Level INTERGER)")
    # connects the list table


# TODO: function must close the current window and show the main disciplinary GUI
def Back_Page():
    print("DEBUG: going to main page, beep boop")
    root.destroy()
    os.system('python Gui.py')


# TODO: function must take all of the inputs of the text boxes and submit to the master database
def Submit():
    print("DEBUG: submitting changes, beep boop")


# TODO: function must show a dialogue allowing the user to select a pre-existing action to load
def SelectAndLoadExisting():
    print("DEBUG: selecting and loading existing action, beep boop")


# ==================================FRAME==============================================

Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
LeftMargin = Frame(root, width=100, height=500, bd=8, relief="raise")
LeftMargin.pack(side=LEFT)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=300, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)

# DONE: button to go back to the main disciplinary GUI
btnGoBack = Button(Bottom, text="Back", command=Back_Page, height=1, width=15)
btnGoBack.pack(side=LEFT)

# DONE: title
lblAddActionTitle = Label(Top, text="Add / Edit Disciplinary Action")
lblAddActionTitle.pack(side=LEFT)

# DONE: "discipline name" textbox (single line)
lblDisciplineName = Label(LeftMargin, text="Name")
txtDisciplineName = Text(Left, height=1, width=30)
lblDisciplineName.pack(side=TOP)
txtDisciplineName.pack(side=TOP)

# DONE: "discipline description" textbox (multi-line)
lblDisciplineDesc = Label(LeftMargin, text="Description", height=5)
txtDisciplineDesc = Text(Left, height=5, width=80)
lblDisciplineDesc.pack(side=TOP)
txtDisciplineDesc.pack(side=TOP)

# DONE: "action to be taken" textbox (multi-line)
lblAction = Label(LeftMargin, text="Action", height=5)
txtAction = Text(Left, height=5, width=80)
lblAction.pack(side=TOP)
txtAction.pack(side=TOP)

# DONE: "severity level" drop down box
possible_severities = [1, 2, 3, 4, 5]
lblSeverity = Label(LeftMargin, text="Severity", height=1)
drpSeverity = ttk.Combobox(Left, values=possible_severities)
lblSeverity.pack(side=TOP)
drpSeverity.pack(side=TOP)

# TODO: add an option to select a pre-existing action and edit it
btnEditExisting = Button(Right, text="Edit Existing Action", command=SelectAndLoadExisting, height=1, width=30)
btnEditExisting.pack(side=TOP)

# DONE: "submit action" button
# lblSubmitDummy = Label(LeftMargin, text="", height=2)
btnSubmitChanges = Button(Right, text="Submit", command=Submit, height=1, width=30)
# lblSubmitDummy.pack(side=BOTTOM)
btnSubmitChanges.pack(side=TOP)


if __name__ == "__main__":
    root.mainloop()
