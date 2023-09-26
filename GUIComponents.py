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


        self.selectedOption = None 
        #Bind events for seamless functionality
        self.textField.bind("<FocusIn>", self.showPopUpMenu)
        self.textField.bind("<KeyPress>", self.filterOptions)
        self.textField.bind("<FocusOut>",self.hidePopUpMenu)
        self.textField.bind("<Return>",lambda e: "break") #This forces the text field to stay on one line and not do multiline
        self.suggestionListBox.bind("<<ListboxSelection>>", self.selectedOption)


    
    def showPopUpMenu(self,event):
        pass

    def hidePopUpMenu(self, event):
        pass

    def filterOptions(self, event):

        pass

    
    def grid(selfm col=0, row=0, sticky='NWSE'):
        pass

    def selectOption(self, selectOption=None):
        pass

    
