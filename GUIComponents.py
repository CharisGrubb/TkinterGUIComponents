import tkinter as tk
from tkinter import ttk

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


    #Make the suggestion box appear
    def showPopUpMenu(self,event):
        self.suggestionListBox.grid(column = self.lb_col, row = self.lb_row, sticky = self.sticky)

    #make the suggestion box dissappear
    def hidePopUpMenu(self, event):
        self.suggestionListBox.grid_forget()

    #filter the options to display based on what was typed
    def filterOptions(self, event):
        filterText = self.textField.get("1.0","end-1c").strip() #Remove white space
        self.suggestionListBox.delete(0,"end") #remove all and repopulate any that match filter text.

        for row in self.menuOptions:
            if filterText.lower() in str(row).lower(): #Ignore case
                self.suggestionListBox.insert("end",row)

        self.suggestionListBox.update_idletasks()
        self.textField.focus_set() #Set focus back to text field where user was typing.
        


    #grid layout option
    def grid(self, col=0, row=0, sticky='NWSE'):
        self.textField.grid(column=col, row=row, sticky = sticky)
        self.lb_col = col+1 #used for when suggestions list box is added, to keep it to the right of the text field
        self.lb_row = row
        self.sticky = sticky

    def selectOption(self, selectOption=None):
        pass



class Table():
    """"
    This class is to imitate a table object. This uses Labels, Frames, and canvas to imitate a scrolling table/list that supports images and icons. 
    """
    """
    @param: rows:list of list of dictionaries [[{"text": "string display option"
                        , "icon": PILImageObject
                        , "icon Path": "path option that can be send in instead of image object"
                        , "tooltip": "string option for tool tip"}]] -A list of rows containint a list of columns, each cell is a dictionary with it's attributes
    @param: config: dict {"Scrollbar Background": "White"}
    """
    __defaultConfig = {"Scrollbar Background":"White", "Scrollbar darkcolor" : "gray11"
                        ,"Foreground":"Black", "Background":"White"
    }
    def __init__(self, master, rows:list[list[dict]], config:dict=None):
        self.master = master
        self.rows = rows
        if config is not None:
            self.config = config
            for row in self.__defaultConfig.keys():
                if row not in self.config.keys():
                    self.config[row] = self.__defaultConfig[row]
        else:
            self.config = self.__defaultConfig

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Vertical.TScrollbar",gripcount=0
                             , background = self.config['Scrollbar Background']
                             , darkcolor = self.config['Scrollbar darkcolor'])
        self.style.configure("Horizontal.TScrollbar",gripcount=0
                             , background = self.config['Scrollbar Background']
                             , darkcolor = self.config['Scrollbar darkcolor'])

        self.table = tk.Canvas(self.master, confine=True)
        self.frame = tk.Frame(self.table)
        self.table.create_window((0,0),window = self.frame, anchor='nw')

        self.scrollBarVertical = tk.ttk.Scrollbar(self.master, orient = 'vertical', command = self.table.yview, style = 'Vertical.TScrollbar')
        self.scrollBarHorizontal = tk.ttk.Scrollbar(self.master, orient = 'vertical', command = self.table.yview, style = 'Horizontal.TScrollbar')

        self.table.config(yscrollcommand=self.scrollBarVertical.set, xscrollcommand= self.scrollBarHorizontal)
        self.loadTable()
        self.master.bind('<KeyPress>', self.keyPressHandler)

    def setRightClickMenu(self, menu:tk.Menu):
        self.right_click_menu = menu
        for row in self.rows:
            for column in row:#bind each cell to right click
                column['Label Object'].bind('<Button-3>', self.rightClickHandler)

    def loadTable(self):
        
        for row in self.rows:
            for column in row:
                column['Label Object'] = tk.Label(master = self.frame
                                                    , text =  column['text'])
                
                column['Label Object'].bind('<Button-1>', self.clickHandler)
                


    def selectOption(self):
        pass

    def keyPressHandler(self):
        pass

    def clickHandler(self):
        pass
    
    def rightClickHandler(self,event):
        try:
            self.right_click_menu.tk_popup(event.x_root, event.y_root)
        except:
            import traceback
            print(traceback.format_exc())

        finally:
            self.right_click_menu.grab_release()

    def pack(self):
        self.table.pack()
        

    def place(self):
        pass


    def grid(self):
        pass 

    def update(self):
        self.table.update()
        self.frame.update()
        self.scrollBarHorizontal.update()
        self.scrollBarVertical.update()

    def _on_mousewheel(self,event):
        self.table.yview_scroll(int(-1*(event.delta/120)),"units")