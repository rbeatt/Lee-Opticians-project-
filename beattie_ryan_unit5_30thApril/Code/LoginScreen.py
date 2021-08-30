import sys
import sqlite3
import time
import MainMenu2
import MainMenu2_support

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import Image, ImageTk

import LoginScreen_support
import os.path
import tkinter.messagebox

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    LoginScreen_support.init(root, top)
    root.mainloop()

w = None
def create_LoginScreen(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    LoginScreen_support.init(w, top, *args, **kwargs)
    return (w, top)

class Toplevel1:
    def quit(self):
        w.withdraw() #Closes the window
  
    def ClearEntries(self):
        self.Entry1.delete(0,'end') #Deletes all data inside the entry box.
        self.Entry2.delete(0,'end')

    def Access(self):
        staffid = self.Entry1.get() #StaffID entry
        with sqlite3.connect("LeeOpt.db") as db: #Connects to the database file
            cursor = db.cursor()
            find_user = ('SELECT AccessLevel FROM Login WHERE StaffID = ?') #Searches for the record with the corresponding StaffID and returns the access level.
            cursor.execute(find_user, [(staffid)]) #Executes the SELECT statement using the input from the GUI.
            results = cursor.fetchone()

            if results == 1:
                accesslevel = ("1")
                tkinter.messagebox.showinfo("Notification","User Access Level 1") #The user will be prompted with a message displaying their access level.
            elif results == 2:
                accesslevel = ("2")
                tkinter.messagebox.showinfo("Notification","User Access Level 2")
            else:
                accesslevel = ("3")
                tkinter.messagebox.showinfo("Notification","User Access Level 1")

    def UserLogin(self): #Login function for staff members
        while True:
            try:
                staffid = int(self.Entry1.get()) #StaffID entry
                password = self.Entry2.get() #Password entry
                with sqlite3.connect("LeeOpt.db") as db: #Connects to the database file
                    cursor = db.cursor()
                    find_user = ('SELECT * FROM Login WHERE StaffID = ? AND Password = ?') #Uses a SQL SELECT statement to find the record with the same details input by the user.
                    cursor.execute(find_user, [(staffid),(password)]) #Executes the SQL statement
                    results = cursor.fetchall()
                    if results: #If results are found
                        for i in results:
                            self.Access() #Runs the function to display the appropriate access level
                            MainMenu2.create_Toplevel1(root) #Opens the main menu screen
                            self.ClearEntries() #Clears entries to provide additional security
                            self.quit() #Closes the login screen
                    else:
                        tkinter.messagebox.showerror("Error", "The staffID or password is incorrect, please try again.") #An error message is displayed                  
                        time.sleep(1)
                        return("exit")
            except ValueError: #If an invalid data type is entered for StaffID
                tkinter.messagebox.showerror("Validation Error","Please enter the correct data type for StaffID. The field cannot be null and must be an integer.") #An error message is displayed
                self.ClearEntries() #Entries are cleared to allow the user to try again.
                break
        
                    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+378+164")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Login")
        top.configure(background="#ffffff")

#Entry for staffID
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.317, rely=0.4,height=20, relwidth=0.423)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

#Entry for password
        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.317, rely=0.489,height=20, relwidth=0.423)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(show ='*')

#Label for staffID
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.2, rely=0.4, height=21, width=71)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''StaffID''')

#Label for password
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.2, rely=0.489, height=21, width=66)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Password''')

#Button to log in
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.467, rely=0.578, height=24, width=61)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(command=self.UserLogin)

#Lee Opticians logo
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.367, rely=0.2, height=41, width=174)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        photo_location = ("LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img0)
        self.Label3.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()





