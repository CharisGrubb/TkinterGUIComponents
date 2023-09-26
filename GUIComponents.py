import tkinter as tk

"""
This class definition is to take existing tkinter objects and fuse them together to imitate an autocomplete field for reusability
"""

class AutoCompleteField():


    def __init__(self, master, suggestedOptions:list, **kwargs):
        self.master = master
        self.textField = tk.Text(master = self.master, wrap = "none", height = 1)
        self.suggestionListBox = tk.Listbox(master = self.master) #This is the menu box popup that shows suggestions based on what was typed
        self.menuOptions = suggestedOptions 

        #start with all options showing, so when the user clicks in the text field it shows all options
        for row in self.menuOptions:
            self.suggestionListBox.insert("end", row)

        #Initialize Fields
        self.selectedOption = None
        self.lb_col = 0
        self.lb_row = 0
        self.sticky = "NWSE"


        #Bind events for seamless functionality
        self.textField.bind("<FocusIn>", self.showPopUpMenu)
        self.textField.bind("<KeyPress>", self.filterOptions)
        self.textField.bind("<FocusOut>",self.hidePopUpMenu)
        self.textField.bind("<Return>",lambda e: "break") #This forces the text field to stay on one line and not do multiline
        self.suggestionListBox.bind("<<ListboxSelection>>", self.selectedOption)


    
    def showPopUpMenu(self,event):
        self.suggestionListBox.grid(column = self.lb_col, row = self.lb_row, sticky = self.sticky)

    #make the suggestion box dissappear
    def hidePopUpMenu(self, event):
        self.suggestionListBox.grid_forget()

    def filterOptions(self, event):

        pass


    #grid layout option
    def grid(self, col=0, row=0, sticky='NWSE'):
        self.textField.grid(column=col, row=row, sticky = sticky)
        self.lb_col = col+1 #used for when suggestions list box is added, to keep it to the right of the text field
        self.lb_row = row
        self.sticky = sticky

    def selectOption(self, selectOption=None):
        pass


