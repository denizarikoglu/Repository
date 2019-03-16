# WORK IN PROGRESS
# developer: Matthew Fowler, Joshua Childs
# last updated: 10/12/18 - 9:56


from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import os
import unittest

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

def Database_Disciplinary_Action():
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Disciplinary_Action' (emp id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Discipline_ID INTEGER, Employee_ID INTEGER, Comment TEXT)")
    #connects the displanryaction table

def Databse_Disciplinary_list():
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Disciplinary_list")  # will get just the dispinary names from the list
    #cursor.execute("SELECT DISTINCT Discipline_Name, Reson_for_Action FROM Disciplinary_list") #will get just the dispinary names from the list
    #cursor.execute("CREATE TABLE IF NOT EXISTS 'Disciplinary_list' (emp id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Discipline_Name TEXT, Reson_for_Action TEXT, Action_Taken TEXT, Severity_Level INTERGER)")
    #conncts the list table

def Database_Users(): #gets all users from the database
    global conn, cursor
    conn = sqlite3.connect('ufix.s3db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UFIX_PIM")

def AddNewRecord():
    user_ID=[]#used to hold all the user ids
    Database_Users()
    results = cursor.fetchall()
    for row in results:
        user_ID.append(row[0])
       #print (row[0])
    cursor.close()  # closes database conection
    conn.close()
    if  comboDisciplinary.get() == "" or TxtEmployeeId.get("1.0", "end-1c") =="" or txtDescription.get("1.0", "end-1c") == "":  #contius for all data to be enterd
        #need to check the verable for the option boxes
        tkMessageBox.showinfo("", "please complete the record field")
        #txt.resulrs.congif(text= "pleasa complete the reierd feld", fg="red")
    elif(int(TxtEmployeeId.get("1.0", "end-1c")) in (user_ID)) :#checks weher thr user id exists
        Database_Disciplinary_Action()
        cursor.execute("INSERT INTO 'Disciplinary_Action' (Discipline_ID, Employee_ID, Comment) VALUES(?, ?, ?)", (str(comboDisciplinary.current()+1), str(TxtEmployeeId.get("1.0", "end-1c")), str(txtDescription.get("1.0", "end-1c"))))
        conn.commit()
        comboDisciplinary.set("")#emptys the inputboxes
        TxtEmployeeId.insert(END,"")
        txtDescription.insert(END,"")
        cursor.close()
        conn.close()
        tkMessageBox.showinfo("","New recored created")
       # txt.resulrs.congif(text="New recored created", fg="green")
    else:
        tkMessageBox.showinfo("", "user dose not exist")
def exit_program():  # asks the user if they want to exit

    result = tkMessageBox.askquestion('HR Demo Module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def update_lables(event):
    print (disciplinary_discrtion[(comboDisciplinary.current())])
    Displinary_Discrtion_text.set(disciplinary_discrtion[(comboDisciplinary.current())])
    Displinary_Action_Taken.set(displinary_action[(comboDisciplinary.current())])

def add_widgets(root):

    global employee_ids
    global disciplinary_types
    global TxtEmployeeId#selected_emp
    global selected_type
    global disciplinary_descs


# show the "add new disciplinary action" screen to the user. Should dissable the main frame.
def show_add_action_screen():
    root.destroy()
    os.system('python AddActionGUI.py')

def show_policy():
    os.system('poilcy.py')
# ==================================FRAME==============================================


Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)


# textframeRight = Frame(Right, width=550, hight=200, relief="raise")#creats a fream for the textbox
# textframeRight.pack(side=TOP)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
# Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")  # creats frame for Buttons?
# Buttons.pack(side=BOTTOM)


# ======================Top Side frame======================
labTitleBar = Label(Top,width=900,font=('arial', 20),text = "Add new action")
labTitleBar.pack(side=TOP)
# ======================Left Side frame======================
# order that thing are done here is how they will show up

labEmpleyID = Label(Left,font=('arial', 12),text="Employee ID")
labEmpleyID.pack(side=TOP)

TxtEmployeeId = Text(Left, height=1, width=10)#Textbox for user to enter users IDs
TxtEmployeeId.pack(side=TOP)
selected_type = StringVar(root)


labDisciplinary = Label(Left,font=('arial', 12),text="Disciplinary Types")
labDisciplinary.pack(side=TOP)

disciplinary_types = []# drop down box verables
disciplinary_discrtion =[]#holds text about dipiary types
displinary_action=[]
Databse_Disciplinary_list()#trying to read data from list
results = cursor.fetchall()
Disciplinary_list = results#used to keep data read from database
cursor.close()#closes database conection
conn.close()
for row in Disciplinary_list:
    disciplinary_types.append(row[1])#gets just the names for displinary type
    disciplinary_discrtion.append(row[2])
    displinary_action.append(row[3])
comboDisciplinary = ttk.Combobox(Left, values=disciplinary_types )#TODO get to trgger comand when changed
comboDisciplinary.bind("<<ComboboxSelected>>",update_lables)#creats a callback to run whenvere combo box is updataed
comboDisciplinary.pack(side=TOP)


# label
Displinary_Discrtion_text = StringVar()
labDiscribeDiscrtion = Label(Left,font=('arial', 12),textvariable=Displinary_Discrtion_text)
labDiscribeDiscrtion.pack(side=TOP)
Displinary_Discrtion_text.set('Dispnary artion')

# label
Displinary_Action_Taken = StringVar()
labActionTaken = Label(Left,font=('arial', 12),textvariable=Displinary_Action_Taken)
labActionTaken.pack(side=TOP)
Displinary_Action_Taken.set("Action taken")

btn_CreatNewEntry = Button(Left, width=15, text="Create new entry", command=AddNewRecord)#creats new entry in table
btn_CreatNewEntry.pack(side=BOTTOM)


# ======================Right Side frame======================
# label
labDiscribeAction = Label(Right, width=600, font=('arial', 24), text = "Discribe dispalnary action")
labDiscribeAction.pack(side=TOP)

# textbox
txtDescription = Text(Right,width=550, height=200 ) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtDescription.pack(side=RIGHT)


# ====================Bottom frame widgits====================
btn_exit = Button(Bottom, width=15, text="Exit", command=exit_program)#should show up on bottom frame but dosnet
btn_exit.pack(side=RIGHT)
btn_add_action = Button(Bottom, width=15, text="Add New Action", command=show_add_action_screen)
btn_add_action.pack(side=LEFT)

btn_show_policy = Button(Bottom, width=15, text="Show policy", command=show_policy)
btn_show_policy.pack(side=LEFT)

# ==================================DISCIPLINARY LIST FRAME==============================================



# =====================================================================================
# ==================================INITIALIZATION=====================================
# =====================================================================================

#if __name__ == '__main__':


root.mainloop()


