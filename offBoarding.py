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
    fen2.title("Questionnaire")
    label1 = LabelFrame(fen2, text="Question 1")
    label1.pack()
    Label(label1, text="What circumstances prompted you to start looking for another job? \n Under what circumstances, if any, would you consider returning to the company?\n").pack()
    text1 = Text(label1, height=2, width=50)
    text1.pack()
    label2 = LabelFrame(fen2, text="Question 2")
    label2.pack()
    Label(label2, text="Were there any company policies you found difficult to understand? \n How can the firm make them clearer?").pack()
    text2 = Text(label2, width=50, height=2)
    text2.pack()
    label3 = LabelFrame(fen2, text="Question 3")
    label3.pack()
    Label(label3, text="Do you feel you had the necessary training to be successful in your role? \n If not, how could it have been better?").pack()
    text3 = Text(label3, width=50, height=2)
    text3.pack()
    label4 = LabelFrame(fen2, text="Question 4")
    label4.pack()
    Label(label4, text="Do you think management adequately recognised employee contributions?\n If not, how do you think recognition could be improved?").pack()
    text4 = Text(label4, width=50, height=2)
    text4.pack()
    label5 = LabelFrame(fen2, text="Question 5")
    label5.pack()
    Label(label5, text="Did you feel you had the tools, resources and working conditions to be successful in your role? \n If not, which areas could be improved and how?").pack()
    text5 = Text(label5, width=50, height=2)
    text5.pack()
    label6 = LabelFrame(fen2, text="Question 6")
    label6.pack()
    Label(label6, text="What can the organisation improve on? \n Do you have any suggestions for improving employee morale?").pack()
    text6 = Text(label6, width=50, height=2)
    text6.pack()
    label7 = LabelFrame(fen2, text="Question 7")
    label7.pack()
    Label(label7, text="Is there anything else you’d like to add?").pack()
    text7 = Text(label7, width=50, height=2)
    text7.pack()
    Button(fen2, text="Valide", width=100, fg="red", command=fen2.quit).pack()
    fen2.mainloop()
    Database()
    cursor.execute(
        "INSERT INTO `Questionnaire` (question1, question2, question3, question4, question5, question6, question7) VALUES(?, ?, ?, ?, ?, ?, ?)",
        (text1.get("1.0", END), text2.get("1.0", END), text3.get("1.0", END), text4.get("1.0", END), text5.get("1.0", END), text6.get("1.0", END), text7.get("1.0", END)))
    conn.commit()
    cursor.close()
    conn.close()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Ufixltd.s3db")
    cursor = conn.cursor()
    cursor.execute( "CREATE TABLE IF NOT EXISTS `Questionnaire` (idQuestionnaire INTEGER PRIMARY KEY  AUTOINCREMENT ,question1	VARCHAR ( 500 ),question2	VARCHAR ( 500 ),question3	VARCHAR ( 500 ),question4	VARCHAR ( 500 ),question5	VARCHAR(500),question6	VARCHAR(500),question7    VARCHAR(500))")


def upload():
    txt_upload.delete("0.0", END)
    filepath = askopenfilename(title="Upload Doc", filetypes=[('pdf files', '.pdf'), ('all files', '.*')])
    name = os.path.basename(filepath)
    txt_upload.insert(END, name)

def callback(event):
    os.system("policies.py")
#==================================VARIABLES==========================================
Q1 = StringVar()
Q2 = StringVar()
Q3 = StringVar()
Q4 = StringVar()
Q5 = StringVar()
Q6 = StringVar()
Q7 = StringVar()

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
