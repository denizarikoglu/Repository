from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import os

root = Tk()
root.title("Dispinary : Add new action")  # name for the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 800
height = 700
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


def exit_program():  # asks the user if they want to exit

    result = tkMessageBox.askquestion('HR Demo Module', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
Middel = Frame(root, width=800, height=650, bd=8, relief="raise")
Middel.pack(side=TOP)



btn_exit = Button(Bottom, width=15, text="Exit", command=exit_program)#should show up on bottom frame but dosnet
btn_exit.pack(side=BOTTOM)

txtpoilcy = Text(Middel,width=550, height=200, ) ##adds a textbox on the right frame. dose not seam to care aboyt hight
txtpoilcy.pack(side=TOP)

poilcy_file = open("poilcy.txt","r")
txtpoilcy.insert('1.0', poilcy_file.read())
poilcy_file.close()
txtpoilcy.config(state=DISABLED)

root.mainloop()