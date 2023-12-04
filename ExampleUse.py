from GUIComponents import Table, AutoCompleteField
from tkinter.messagebox import showinfo
import tkinter as tk



def sayHello():
    showinfo('Howdy Partner','Hello World')




master = tk.Tk() 

#Menu
menu = tk.Menu(master, tearoff=False)
menu.add_command(label = "Say Hello", command = sayHello)

#Table
example_table_dataset = [[{"text":"This is a test row at 0,0"},{"text":"Cell at 0,1"}]
                         ,[{"text":"This is a test row at 1,0"},{"text":"Cell at 1,1"}]
                         ,[{"text":"This is a test row at 2,0"},{"text":"Cell at 2,1"}]
                         ,[{"text":"This is a test row at 3,0"},{"text":"Cell at 3,1"}]]

example_table = Table(master, example_table_dataset)
example_table.setRightClickMenu(menu)
example_table.grid()

#Auto Complete Field
autoCompleteOptions = ['Florida','Georgia','Indiana','Ohio','New York','California','Alaska','Illinois']

ac_field = AutoCompleteField(master, autoCompleteOptions)

ac_field.grid(col=2,row=0, sticky = 'NW')


master.update()
master.mainloop()
