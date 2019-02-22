import os
import webbrowser
from tkinter import *


root = Tk()
root.title("Policy")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
#==================================VARIABLES==========================================
v = IntVar()
v.set(2)
#==================================METHODS============================================
def callback(event):
    ##webbrowser.open_new(r"Policies\Business_Ethics&Conduct_POLICY.pdf")
    text1 = ""
    fichier = open("Policies\Business Ethics & Conduct POLICY.txt", "r")
    for ligne in fichier:
        text1 += ligne
    fichier.close()
    fen2 = Toplevel()
    fen2.title("Business Ethics & Conduct POLICY")
    text = Label(fen2, text=text1)
    text.pack()
    fen2.mainloop()

def callback2(event):
    ##webbrowser.open_new(r"Policies\Confidentiality&Non-Disclosure_POLICY.pdf")
    text1 = ""
    fichier = open("Policies\Confidentiality & Non-Disclosure POLICY.txt", "r")
    for ligne in fichier:
        text1 += ligne
    fichier.close()
    fen2 = Toplevel()
    text = Label(fen2, text=text1)
    text.pack()
    fen2.mainloop()

def callback3(event):
    ##webbrowser.open_new(r"Policies\DISCIPLINE_AND_TERMINATION_POLICY.pdf")
    text1 = ""
    fichier = open("Policies\DISCIPLINE AND TERMINATION POLICY.txt", "r")
    for ligne in fichier:
        text1 += ligne
    fichier.close()
    fen2 = Toplevel()
    text = Label(fen2, text=text1)
    text.pack()
    fen2.mainloop()

def callback4(event):
    ##webbrowser.open_new(r"Policies\Safety_POLICY.pdf")
    text1 = ""
    fichier = open("Policies\Safety POLICY.txt", "r")
    for ligne in fichier:
        text1 += ligne
    fichier.close()
    fen2 = Toplevel()
    text = Label(fen2, text=text1)
    text.pack()
    fen2.mainloop()

def policie(event):
    webbrowser.open_new(r"E:\\usw20182019\CS2S567\Repository\Policies\Policies.pdf")

def valide():
    if v.get() == 1:
        btn_exit.config(state=ACTIVE)
    else:
        btn_exit.config(state=DISABLED)

def exit():
    root.destroy()
def _destroy():
    root.destroy()
    os.system("policies.py")
#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(root, width=900, height=400, bd=8, relief="raise")
Middle.pack()
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
Buttons = Frame(Middle, width=900, height=45, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
Link = Frame(Middle, width=100, height=50)
Link.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Policies")
txt_title.pack()
link1 = Label(Link, width=100, text="Buisiness Ethics & Conduct", fg="blue", cursor="hand2")
link1.bind("<Button-1>", callback)
link1.pack()
link2 = Label(Link, width=100, text="Confidentiality & Non-Disclosure", fg="blue", cursor="hand2")
link2.bind("<Button-1>", callback2)
link2.pack()
link3 = Label(Link, width=100, text="DISCIPLINE AND TERMINATION", fg="blue", cursor="hand2")
link3.bind("<Button-1>", callback3)
link3.pack()
link4 = Label(Link, width=100, text="Safety", fg="blue", cursor="hand2")
link4.bind("<Button-1>", callback4)
link4.pack()
link5 = Label(Link, width=100, text="Policies Pdf", fg="blue", cursor="hand2")
link5.bind("<Button-1>", policie)
link5.pack()

#==================================BUTTONS WIDGET=====================================
btn_agree = Radiobutton(Buttons, width=70, text="I agree", variable=v, value=1, command=valide)
btn_agree.pack(side=LEFT)
btn_disagree = Radiobutton(Buttons, width=70, text="I disagree", variable=v, value=2, command=valide)
btn_disagree.pack()
btn_exit = Button(Bottom, width=10, text="Valide", state=DISABLED, command=exit)
btn_exit.pack(side=RIGHT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Middle, orient=VERTICAL)
text = Text(Middle, height=15, width=900, yscrollcommand=scrollbary.set)
scrollbary.config(command=text.yview)
scrollbary.pack(side=RIGHT, fill=Y)
file = open("Policies\Data_Protection.txt", "r")
for line in file:
    text.insert(END, line)
file.close()
text.config(state=DISABLED)
text.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.protocol("WM_DELETE_WINDOW", _destroy)
    root.mainloop()
