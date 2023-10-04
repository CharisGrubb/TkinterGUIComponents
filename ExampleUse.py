from GUIComponents import Table, AutoCompleteField

import tkinter as tk

master = tk.Tk() 

example_table_dataset = [[{"text":"This is a test row at 0,0"}]
                         ,[{"text":"This is a test row at 1,0"}]]

example_table = Table(master, example_table_dataset)
example_table.pack()


master.update()
master.mainloop()
