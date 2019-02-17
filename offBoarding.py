from tkinter import *
import sqlite3
import tkinter.messagebox as tkMessageBox
import os
from tkinter.filedialog import *

root = Tk()
root.title("OFF Boarding Page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 600
height = 300
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
    fen2 = Tk()
    text1 = LabelFrame(fen2, text="Question 1")
    text1.pack()
    Label(text1, text="what you ?").pack()
    fen2.mainloop()

def upload():
    txt_upload.delete("0.0", END)
    filepath = askopenfilename(title="Upload Doc", filetypes=[('pdf files', '.pdf'), ('all files', '.*')])
    name = os.path.basename(filepath)
    txt_upload.insert(END, name)

def callback(event):
    try:
        os.system("Page\policies.py")
    except ValueError:
        os.system("policies.py")

#==================================FRAME==============================================
Top = Frame(root, width=600, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(root, width=600, height=200, bd=8)
Middle.pack()
MiddleTop = Frame(Middle, width=600, height=50, bd=8, relief="raise")
MiddleTop.pack(side=TOP)
MiddleBottom = Frame(Middle, width=600, height=150, bd=8, relief="raise")
MiddleBottom.pack(side=BOTTOM)
Bottom = Frame(root, width=600, height=50, bd=4, relief="raise")
Bottom.pack(side=BOTTOM)
#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text="OFF Boarding Page")
txt_title.pack()
txt_termi = Label(MiddleBottom, width=600, text="Upload and sign your termination contract")
txt_termi.pack()
txt_quest = Label(MiddleTop, width=600, text="Start the satifaction questionnaire")
txt_quest.pack()
link = Label(Bottom, width=900, text="Policies", fg="blue", cursor="hand2")
link.bind("<Button-1>", callback)
link.pack()
txt_upload = Text(MiddleBottom, width=50, height=1)
txt_upload.pack()
#==================================BUTTONS WIDGET=====================================
btn_questionnaire = Button(MiddleTop, width=10, text="Questionnaire", command=Questionnaire)
btn_questionnaire.pack(side=RIGHT)
btn_upload = Button(MiddleBottom, width=10, text="upload", command=upload)
btn_upload.pack(side=RIGHT)
#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
