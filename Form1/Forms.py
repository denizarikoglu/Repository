import tkinter as tk
top = tk.Tk()
logo = tk.PhotoImage(file="logo.png")

top.title("FORM1")
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
width = 1200
height = 750
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top.geometry('%dx%d+%d+%d' % (width, height, x, y))
top.resizable(0, 0)

image = tk.Label(top, image=logo).pack(padx=15, pady=10, side="left")

username = tk.Label(top, text="Userame").pack(padx=15, pady=20, side="left")
usernameField = tk.Entry(top).pack(padx=15, pady=20, side="left")
password = tk.Label(top, text="password").pack(padx=15, pady=20, side="left")
usernameField = tk.Entry(top).pack(padx=15, pady=20, side="left")



top.mainloop()