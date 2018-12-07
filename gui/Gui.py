## WORK IN PROGRESS
## developer: Matthew Fowler
## last updated: 15/11/18 - 16:12


from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Dispinary : Add new action")##name for the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def Exit():##asks the user if they want to exit
    result = tkMessageBox.askquestion('HR Demo Module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def addwidgets(root):

    global employee_ids
    global disciplinary_types
    global selected_emp
    global selected_type
    global disciplinary_descs

    # ==================================FRAME==============================================


Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
##Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")  # creats frame for Buttons?
##Buttons.pack(side=BOTTOM)
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")#dosent show up?
Bottom.pack(side=BOTTOM)

##======================Top Side frame======================
labTitleBar = Label(Top,width=10,font=('arial', 20),text = "Add new action")
labTitleBar.pack(side=TOP)
##======================Left Side frame======================
#order that thing are done here is how they will show up
selected_emp = StringVar(root) #holds the currently selected employee
employee_ids = {"0000", "0001", "0002"} #contains fake data
#drop down box
drpEmployee = OptionMenu(Left, selected_emp, *employee_ids)
#drpEmployee.grid(column=1, row=0)
drpEmployee.pack(side=TOP)

selected_type = StringVar(root)
disciplinary_types = {"Item not returned", "Late to work"}
#drop down box
drpDisciplinary = OptionMenu(Left, selected_type, *disciplinary_types)
#drpDisciplinary.grid(column=1, row=0)
drpDisciplinary.pack(side=TOP)

#label
#might work better as a textbox
labDiscribeDiscrtion = Label(Left,width=10,font=('arial', 12),text = "Discrtion")
labDiscribeDiscrtion.pack(side=TOP)

#label
#might work better as a textbox
labActionTaken = Label(Left,width=10,font=('arial', 12),text = "Action taken")
labActionTaken.pack(side=TOP)

##======================Right Side frame======================
#label
labDiscribeAction = Label(Right, width=600, font=('arial', 24), text = "Discribe dispalnary action")
labDiscribeAction.pack(side=TOP)

#textbox
txtDescription = Text(Right, height=200, width=550) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtDescription.pack(side=RIGHT)




##====================Buttons wigits====================
btn_exit = Button(Bottom, width=10, text="Exit", command=Exit)#should show up on bottom frame but dosnet
btn_exit.pack(side=LEFT)







#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()