# WORK IN PROGRESS
# developer: Matthew Fowler, Joshua Childs
# last updated: 10/12/18 - 9:56


from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

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

def Database():
    global conn, cursor
    conn = sqlite3.connect('UfixLtd.s3db')
    cursor = conn.cursor()
    cursor.execute("CREAT TABE IF NOT EXSITS 'Disciplinary_Action' (emp id INTEGER PRIMARY KEY AUTOINCMENT NOT NULL, Discipline_ID INTEGER, Employee_ID INTEGER, Comment TEXT")
    #connects the displanryaction table

def AddNewRecord():
    if  DISCIPLINARY_ID.get() == "" or EMPLOYEE_ID.get() == "" or COMMENT.get() == "":  #contius for all data to be enterd
        #what are the .get() for? the table feilds or textboxs?
        txt.resulrs.congif(text= "pleasa complete the reierd feld", fg="red")
    else:#creats new record
        Database()
        cursor.execute("INSERT INTO 'Disciplinary_list' (Discipline_ID, Employee_ID, Comment) VALUES{?, ?, ?}", str(S))
        conn.commit()
        DISCIPLINARY_ID.set("")#will this work for combo boxes
        EMPLOYEE_ID.set("")
        COMMENT.set("")
        cursor.close()
        conn.close()
        txt.resulrs.congif(text="New recored created", fg="green")

def exit_program():  # asks the user if they want to exit
    result = tkMessageBox.askquestion('HR Demo Module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def add_widgets(root):

    global employee_ids
    global disciplinary_types
    global selected_emp
    global selected_type
    global disciplinary_descs

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
selected_emp = StringVar(root)  # holds the currently selected employee
employee_ids = {"0000", "0001", "0002"}  # contains fake data
# drop down box
drpEmployee = OptionMenu(Left, selected_emp, *employee_ids)
# drpEmployee.grid(column=1, row=0)
drpEmployee.pack(side=TOP)

selected_type = StringVar(root)
disciplinary_types = {"Item not returned", "Late to work"}
# drop down box
drpDisciplinary = OptionMenu(Left, selected_type, *disciplinary_types)
# drpDisciplinary.grid(column=1, row=0)
drpDisciplinary.pack(side=TOP)

# label
# might work better as a textbox
labDiscribeDiscrtion = Label(Left,width=10,font=('arial', 12),text = "Discrtion")
labDiscribeDiscrtion.pack(side=TOP)

# label
# might work better as a textbox
labActionTaken = Label(Left,width=10,font=('arial', 12),text = "Action taken")
labActionTaken.pack(side=TOP)

# ======================Right Side frame======================
# label
labDiscribeAction = Label(Right, width=600, font=('arial', 24), text = "Discribe dispalnary action")
labDiscribeAction.pack(side=TOP)

# textbox
txtDescription = Text(Right,width=550, height=200 ) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtDescription.pack(side=RIGHT)


# ====================Buttons wigits====================
btn_exit = Button(Bottom, width=10, text="Exit", command=exit_program)#should show up on bottom frame but dosnet
btn_exit.pack(side=RIGHT)

# =====================================================================================
# ==================================INITIALIZATION=====================================
# =====================================================================================
if __name__ == '__main__':
    root.mainloop()
