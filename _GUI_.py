from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
#import io.StringIO
import tkinter as tk

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
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page_Home(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is the HOME page, navigate from here")
       label.pack(side="top", fill="both", expand=True)

class Page_Departments(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This will bring up DEPARTMENT navigation page")
        label.pack(side="top", fill="both", expand=True)

class Page_Support(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This will bring up SUPPORT page")
       label.pack(side="top", fill="both", expand=True)

class Page_Services(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This will bring up SERVICES page")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page_Home(self)
        p2 = Page_Departments(self)
        p3 = Page_Support(self)
        p4 = Page_Services(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # p1 = home
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p2 = departments
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3 = support
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p4 = services
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        ############Buttons############
        # Home Page
        # exit button
        btn_exit = Button(root, width=10, text='EXIT', command=root.quit)
        btn_exit.place(x=20, y=450)
        # support button
        button_1 = Button(root, text="Support", command=p3.lift)
        button_1.place(x=20, y=50)
        # services button
        button_2 = Button(root, text="Services", command=p4.lift)
        button_2.place(x=20, y=150)
        # department button
        button_3 = Button(root, text="Department", command=p2.lift)
        button_3.place(x=20, y=250)
        # legal doc button
        button_4 = Button(root, text="Legal Documentation", command=LegalInfo)
        button_4.place(x=20, y=350)

        # Department Page - for integration

        # Support Page - for integration

        # Services Page - for integration

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("UFIX LTD.")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("480x500")
    root.mainloop()
