from tkinter import *

window = Tk()
window.title("Welcome to Ufix")
window.geometry('550x500')
label = Label(window, text="Welcome to Ufix", font=("Arial Bold", 50))
label.pack()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 900
height = 1000
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)


#==================================METHODS============================================


#==================================FRAME==============================================
Top = Frame(window, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Middle = Frame(window, width=900, height=300, bd=8, relief="groove")
Middle.pack()
Left = Frame(Middle, width=300, height=400, bd=8, relief="groove")
#Left.pack(side=LEFT)
Right = Frame(Middle, width=600, height=400, bd=8, relief="raise")
#Right.pack(side=RIGHT)
Bottom = Frame(window, width=900, height=50, bd=4, relief="groove")
Bottom.pack(side=BOTTOM)
#Forms = Frame(Left, width=300, height=400)
#Forms.pack(side=TOP)
#Buttons = Frame(Left, width=300, height=50, bd=8, relief="raise")
#Buttons.pack(side=BOTTOM)

#ufix introduction
introUfix_text=Label(Middle,font=("arial",14),fg="#505359",height=10,width=60,bg="#98adce", text="The Presentation Company s training workshops are always well-paced,\n informative and a fantastic use of our time.\n Their customized approach and use of before and after examples helped transform our marketing team into more knowledgeable and effective PowerPoint presenters.")
introUfix_text.pack()

# bouton de sortie
boutonClose=Button(Bottom, text="Close",width=100,fg="red", cursor="hand2", command=window.quit)
boutonClose.pack()
window.mainloop()

