from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import webbrowser

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


#==================================METHODS============================================
def callback(event):
    webbrowser.open_new(r"Policies\Business_Ethics&Conduct_POLICY.pdf")
def callback2(event):
    webbrowser.open_new(r"Policies\Confidentiality&Non-Disclosure_POLICY.pdf")
def callback3(event):
    webbrowser.open_new(r"Policies\DISCIPLINE_AND_TERMINATION_POLICY.pdf")
def callback4(event):
    webbrowser.open_new(r"Policies\Safety_POLICY.pdf")
def valide():
    if v.get() == 1:
        btn_exit.config(state=ACTIVE)
    else:
        btn_exit.config(state=DISABLED)
def exit():
    root.destroy()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(root, width=900, height=400, bd=8, relief="raise")
Middle.pack()
Bottom = Frame(root, width=900, height=50, bd=8, relief="raise")
Bottom.pack(side=BOTTOM)
Buttons = Frame(Middle, width=900, height=50, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
Link = Frame(Middle, width=100, height=50)
Link.pack(side=BOTTOM)

#==================================VARIABLES==========================================
v = IntVar()
v.set(2)

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

#==================================BUTTONS WIDGET=====================================
btn_agree = Radiobutton(Buttons, width=70, text="I agree", variable=v, value=1, command=valide)
btn_agree.pack(side=LEFT)
btn_disagree = Radiobutton(Buttons, width=70, text="I disagree", variable=v, value=2, command=valide)
btn_disagree.pack()
btn_exit = Button(Bottom, width=10, text="Valide", state=DISABLED, command=exit)
btn_exit.pack(side=RIGHT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Middle, orient=VERTICAL)
text = Text(Middle, height=16, width=900, yscrollcommand=scrollbary.set)
scrollbary.config(command=text.yview)
scrollbary.pack(side=RIGHT, fill=Y)
fichier = open("Policies\Data_Protection.txt","r")
for ligne in fichier:
    text.insert(END,ligne)
fichier.close()
text.config(state=DISABLED)
text.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
