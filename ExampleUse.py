from GUIComponents import Table, AutoCompleteField

import tkinter as tk

master = tk.Tk() 

example_table_dataset = [[{"text":"This is a test row at 0,0"},{"text":"Cell at 0,1"}]
                         ,[{"text":"This is a test row at 1,0"},{"text":"Cell at 1,1"}]]

example_table = Table(master, example_table_dataset)
example_table.grid()


master.update()
master.mainloop()
