## WORK IN PROGRESS
## developer: Matthew Fowler
## last updated: 15/11/18 - 16:12


import tkinter as tk


def addwidgets(root):

    global employee_ids
    global disciplinary_types
    global selected_emp
    global selected_type
    global disciplinary_descs

    # Title label
    lblTitle = tk.Label(root, text="Set Disciplinary Action")
    #lblTitle.grid(column=0, row=0)
    lblTitle.pack()

    # Person names drop-down box
    drpEmployee = tk.OptionMenu(root, selected_emp, *employee_ids)
    #drpEmployee.grid(column=1, row=0)
    drpEmployee.pack()

    # Disciplinary type drop-down box
    selected_emp = tk.StringVar(root) #holds the currently selected employee
    drpDisciplinary = tk.OptionMenu(root, selected_type, *disciplinary_types)
    #drpDisciplinary.grid(column=1, row=0)
    drpDisciplinary.pack()

    # Description non-editable textbox
    scrollDescription = tk.Scrollbar(root)
    scrollDescription.pack( side = tk.RIGHT, fill = tk.Y )
    txtDescription = tk.Entry(root, text="", yscrollcommand = scrollDescription.set)
    txtDescription.pack()
    scrollDescription.config(command = txtDescription.yview)

    # Action taken non-editable text box


## Root window settup:
root = tk.Tk()
root.title("UFIX LTD: Disciplinary Actions")

## Global values settup:
employee_ids = {"0000", "0001", "0002"} #contains fake data
disciplinary_types = {"Item not returned", "Late to work"}
disciplinary_descs = {"Item not returned": "Employee rented an item, but did not return within the required time-frame.",
                      "Late to work": "Employee has arrived late for work on three or more occasions."}

selected_emp = tk.StringVar(root) #holds the currently selected employee
selected_type = tk.StringVar(root)#holds the currently selected disciplinary type

## Add widgets and show the form
addwidgets(root)
tk.mainloop()
