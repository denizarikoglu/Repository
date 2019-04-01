from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
#import io.StringIO


root = Tk()
root.title("Login Page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 300
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

############Methods############

def Exit():
    result = tkMessageBox.askquestion('Login Module', 'Are you sure you want to exit?', icon = "warning")
    if result == 'yes':
        root.destroy()
        exit()

def LegalInfo():
    tkMessageBox.showinfo('Legal Notice', 'These messages are for LEGAL PURPOSES. Please adhere to them. For more details copy the URL into a web browser')
    tkMessageBox.showinfo('Legal Notice', 'https://www.gov.uk/data-protection - Data protection is vital for any business with data held about its customers')
    tkMessageBox.showinfo('Legal Notice', 'https://www.copyrightservice.co.uk/copyright/uk_law_summary - Use of assets that are not yours for personal gain is illegal')
    tkMessageBox.showinfo('Legal Notice', 'https://en.wikipedia.org/wiki/Influence_peddling - Accepting bribes or assurences to get them access to restriced material or boost their cause is illegal')
    tkMessageBox.showinfo('Legal Notice', 'Reminder - Coding practises and ethical standards are to be met at all times')

############Frame############

#Top = Frame(root, width = 900, height = 50, bd = 8, relief = "raise")
#Top.pack(side = TOP)

Left = Frame(root, width = 300, height = 500, bd = 8, relief = "raise")
Left.pack(side = LEFT)

#Right = Frame(root, width = 600, height = 500, bd = 8, relief = "raise")
#Right.pack(side = RIGHT)

Forms = Frame(Left, width = 300, height = 500)
Forms.pack(side = TOP)

#Buttons = Frame(Left, width = 100, height = 100, bd = 8, relief = "raise")
#Buttons.pack(side = BOTTOM)

############Buttons############
#exit button
btn_exit = Button(root, width = 10, text = 'EXIT', command = root.quit)
btn_exit.place(x = 20, y = 450)
#support button
button_1 = Button(root, text = "Support")
button_1.place(x = 20, y = 50)
#services button
button_2 = Button(root, text = "Services")
button_2.place(x = 20, y = 150)
#department button
button_3 = Button(root, text = "Department")
button_3.place(x = 20, y = 250)
#legal doc button
button_4 = Button(root, text = "Legal Documentation", command = LegalInfo)
button_4.place(x = 20, y = 350)

if __name__ == '__main__':
    root.mainloop()
