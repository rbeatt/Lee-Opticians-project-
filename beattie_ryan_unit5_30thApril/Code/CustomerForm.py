import sys

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

import CustomerForm_support
import os.path
import sqlite3
import tkinter.messagebox
from datetime import datetime


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = CustomerForm (root)
    CustomerForm_support.init(root, top)
    root.mainloop()

w = None
def create_CustomerForm(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_CustomerForm(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = CustomerForm (w)
    CustomerForm_support.init(w, top, *args, **kwargs)
    return (w, top)


class CustomerForm:
    def quit(self): #Closes the window
        w.destroy()

    def ClearID(self): #Clears the CustomerID field
        self.CustomerEntry.delete(0,'end')

    def ClearDate(self): #Clears the date field
        self.DOBEntry.delete(0,'end')

    def ClearEntries(self): #Clears all entries
        self.CustomerEntry.delete(0,'end')
        self.BranchEntry.delete(0,'end')
        self.NameEntry.delete(0,'end')
        self.SurnameEntry.delete(0,'end')
        self.DOBEntry.delete(0,'end')
        self.TownEntry.delete(0,'end')
        self.PostcodeEntry.delete(0,'end')
        self.EmailEntry.delete(0,'end')
        self.TelephoneEntry.delete(0,'end')
        self.MedicalEntry.delete(0,'end')
    
    def format(self): #Function to perform a format check on the date of birth
        dateofbirth = self.DOBEntry.get()
        try:
            if dateofbirth != datetime.strptime(dateofbirth, "%d/%m/%Y").strftime('%d/%m/%Y'):
                raise ValueError
            return True
        except ValueError:
            tkinter.messagebox.showerror("Error","Please enter the date of birth in the correct format DD/MM/YYYY")
            self.ClearDate()
            return False

    def idpresence(self): #Function to perform a presence check on the CustomerID.
        customerid = self.CustomerEntry.get()
        try:
            if customerid == "":
                raise ValueError
            return True
        except ValueError:
            tkinter.messagebox.showerror("Error","The CustomerID field cannot be left blank. Please enter an CustomerID.")
            self.ClearID()
            return False


    def AddCustomer(self):
        customerid = self.CustomerEntry.get()
        branchid = self.BranchEntry.get()
        name = self.NameEntry.get()
        surname = self.SurnameEntry.get()
        dateofbirth = self.DOBEntry.get()
        town = self.TownEntry.get()
        postcode = self.PostcodeEntry.get()
        email = self.EmailEntry.get()
        telephone = self.TelephoneEntry.get()
        medical = self.MedicalEntry.get()
        
        if self.format() and self.idpresence():
            try:
                with sqlite3.connect("LeeOpt.db") as db:
                    cursor = db.cursor()
                    add_customer = ('''INSERT INTO Customer(CustomerID, BranchID, Name, Surname, DateOfBirth, Town, Postcode, EmailAddress, TelephoneNo, MedicalConditions)
                    VALUES (?,?,?,?,?,?,?,?,?,?)''')
                    cursor.execute(add_customer, [(customerid),(branchid),(name),(surname),(dateofbirth),(town),(postcode),(email),(telephone),(medical)])
                    tkinter.messagebox.showinfo("Notification","Customer added successfully")
                    self.ClearEntries()
            except (sqlite3.IntegrityError): 
                tkinter.messagebox.showerror("Error","This CustomerID is already taken, please try another.")
                self.ClearID()

    def DeleteCustomer(self):
        customerid = self.CustomerEntry.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            delete_customer = ('''DELETE FROM Customer WHERE CustomerID = ?''')
            cursor.execute(delete_customer, [(customerid)])
            tkinter.messagebox.showinfo("Notification","Customer deleted successfully")
            self.ClearEntries()

    def UpdateCustomer(self):
        customerid = self.CustomerEntry.get()
        branchid = self.BranchEntry.get()
        name = self.NameEntry.get()
        surname = self.SurnameEntry.get()
        email = self.EmailEntry.get()
        telephone = self.TelephoneEntry.get()
        town = self.TownEntry.get()
        postcode = self.PostcodeEntry.get()
        medical = self.MedicalEntry.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            update_customer = ('''UPDATE Customer 
            SET 
            BranchID = ?,
            Name = ?,
            Surname = ?,
            EmailAddress = ?,
            TelephoneNo = ?,
            Town = ?,
            Postcode = ?,
            MedicalConditions = ?
            WHERE CustomerID = ?
            ''')
            db.commit()
            
            cursor.execute(update_customer,[(branchid),(name),(surname),(email),(telephone),(town),(postcode),(medical),(customerid)])
            tkinter.messagebox.showinfo("Notification","Customer record updated successfully")
            self.ClearEntries()



    def SearchCustomer(self):
        customerid = self.CustomerEntry.get()
        surname = self.SurnameEntry.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_customer = ('''SELECT * FROM Customer WHERE CustomerID = ? OR Surname =?''')
            cursor.execute(search_customer, [(customerid),(surname)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    tkinter.messagebox.showinfo("Record Found", "\n".join(str(x) for x in results))
                    self.ClearEntries()
            else:
                tkinter.messagebox.showerror("Error", "No record was found with this CustomerID, please try again.")
                self.ClearEntries()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x716+416+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Customer Form")
        top.configure(background="#ffffff")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.CustomerEntry = tk.Entry(top)
        self.CustomerEntry.place(relx=0.2, rely=0.251,height=20, relwidth=0.39)
        self.CustomerEntry.configure(background="white")
        self.CustomerEntry.configure(disabledforeground="#a3a3a3")
        self.CustomerEntry.configure(font="TkFixedFont")
        self.CustomerEntry.configure(foreground="#000000")
        self.CustomerEntry.configure(insertbackground="black")

        self.BranchEntry = tk.Entry(top)
        self.BranchEntry.place(relx=0.2, rely=0.307,height=20, relwidth=0.39)
        self.BranchEntry.configure(background="white")
        self.BranchEntry.configure(disabledforeground="#a3a3a3")
        self.BranchEntry.configure(font="TkFixedFont")
        self.BranchEntry.configure(foreground="#000000")
        self.BranchEntry.configure(insertbackground="black")

        self.NameEntry = tk.Entry(top)
        self.NameEntry.place(relx=0.2, rely=0.363,height=20, relwidth=0.39)
        self.NameEntry.configure(background="white")
        self.NameEntry.configure(disabledforeground="#a3a3a3")
        self.NameEntry.configure(font="TkFixedFont")
        self.NameEntry.configure(foreground="#000000")
        self.NameEntry.configure(insertbackground="black")

        self.SurnameEntry = tk.Entry(top)
        self.SurnameEntry.place(relx=0.2, rely=0.419,height=20, relwidth=0.39)
        self.SurnameEntry.configure(background="white")
        self.SurnameEntry.configure(disabledforeground="#a3a3a3")
        self.SurnameEntry.configure(font="TkFixedFont")
        self.SurnameEntry.configure(foreground="#000000")
        self.SurnameEntry.configure(insertbackground="black")

        self.DOBEntry = tk.Entry(top)
        self.DOBEntry.place(relx=0.2, rely=0.475,height=20, relwidth=0.39)
        self.DOBEntry.configure(background="white")
        self.DOBEntry.configure(disabledforeground="#a3a3a3")
        self.DOBEntry.configure(font="TkFixedFont")
        self.DOBEntry.configure(foreground="#000000")
        self.DOBEntry.configure(insertbackground="black")

        self.TownEntry = tk.Entry(top)
        self.TownEntry.place(relx=0.2, rely=0.531,height=20, relwidth=0.39)
        self.TownEntry.configure(background="white")
        self.TownEntry.configure(disabledforeground="#a3a3a3")
        self.TownEntry.configure(font="TkFixedFont")
        self.TownEntry.configure(foreground="#000000")
        self.TownEntry.configure(insertbackground="black")

        self.PostcodeEntry = tk.Entry(top)
        self.PostcodeEntry.place(relx=0.2, rely=0.587,height=20, relwidth=0.39)
        self.PostcodeEntry.configure(background="white")
        self.PostcodeEntry.configure(disabledforeground="#a3a3a3")
        self.PostcodeEntry.configure(font="TkFixedFont")
        self.PostcodeEntry.configure(foreground="#000000")
        self.PostcodeEntry.configure(insertbackground="black")

        self.EmailEntry = tk.Entry(top)
        self.EmailEntry.place(relx=0.2, rely=0.642,height=20, relwidth=0.39)
        self.EmailEntry.configure(background="white")
        self.EmailEntry.configure(disabledforeground="#a3a3a3")
        self.EmailEntry.configure(font="TkFixedFont")
        self.EmailEntry.configure(foreground="#000000")
        self.EmailEntry.configure(insertbackground="black")

        self.TelephoneEntry = tk.Entry(top)
        self.TelephoneEntry.place(relx=0.2, rely=0.698, height=20, relwidth=0.39)

        self.TelephoneEntry.configure(background="white")
        self.TelephoneEntry.configure(disabledforeground="#a3a3a3")
        self.TelephoneEntry.configure(font="TkFixedFont")
        self.TelephoneEntry.configure(foreground="#000000")
        self.TelephoneEntry.configure(insertbackground="black")

        self.MedicalEntry = tk.Entry(top)
        self.MedicalEntry.place(relx=0.2, rely=0.754,height=70, relwidth=0.39)
        self.MedicalEntry.configure(background="white")
        self.MedicalEntry.configure(disabledforeground="#a3a3a3")
        self.MedicalEntry.configure(font="TkFixedFont")
        self.MedicalEntry.configure(foreground="#000000")
        self.MedicalEntry.configure(insertbackground="black")

        self.CustomerLbl = tk.Label(top)
        self.CustomerLbl.place(relx=0.067, rely=0.251, height=20, width=69)
        self.CustomerLbl.configure(background="#ffffff")
        self.CustomerLbl.configure(disabledforeground="#a3a3a3")
        self.CustomerLbl.configure(foreground="#000000")
        self.CustomerLbl.configure(text='''CustomerID''')

        self.BranchLbl = tk.Label(top)
        self.BranchLbl.place(relx=0.083, rely=0.307, height=20, width=64)
        self.BranchLbl.configure(background="#ffffff")
        self.BranchLbl.configure(disabledforeground="#a3a3a3")
        self.BranchLbl.configure(foreground="#000000")
        self.BranchLbl.configure(text='''BranchID''')

        self.NameLbl = tk.Label(top)
        self.NameLbl.place(relx=0.117, rely=0.363, height=21, width=38)
        self.NameLbl.configure(background="#ffffff")
        self.NameLbl.configure(disabledforeground="#a3a3a3")
        self.NameLbl.configure(foreground="#000000")
        self.NameLbl.configure(text='''Name''')

        self.SurnameLbl = tk.Label(top)
        self.SurnameLbl.place(relx=0.083, rely=0.419, height=21, width=63)
        self.SurnameLbl.configure(background="#ffffff")
        self.SurnameLbl.configure(disabledforeground="#a3a3a3")
        self.SurnameLbl.configure(foreground="#000000")
        self.SurnameLbl.configure(text='''Surname''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.35, rely=0.098, height=61, width=174)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label5.configure(image=_img0)
        self.Label5.configure(text='''Label''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.667, rely=0.223, relheight=0.662
                , relwidth=0.242)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.AddCustomerBtn = tk.Button(self.Frame1)
        self.AddCustomerBtn.place(relx=0.276, rely=0.042, height=24, width=63)
        self.AddCustomerBtn.configure(activebackground="#ececec")
        self.AddCustomerBtn.configure(activeforeground="#000000")
        self.AddCustomerBtn.configure(background="#ffffff")
        self.AddCustomerBtn.configure(disabledforeground="#a3a3a3")
        self.AddCustomerBtn.configure(foreground="#000000")
        self.AddCustomerBtn.configure(highlightbackground="#d9d9d9")
        self.AddCustomerBtn.configure(highlightcolor="black")
        self.AddCustomerBtn.configure(pady="0")
        self.AddCustomerBtn.configure(text='''Add''')
        self.AddCustomerBtn.configure(command=self.AddCustomer)

        self.SearchCustomerBtn = tk.Button(self.Frame1)
        self.SearchCustomerBtn.place(relx=0.276, rely=0.148, height=24, width=66)

        self.SearchCustomerBtn.configure(activebackground="#ececec")
        self.SearchCustomerBtn.configure(activeforeground="#000000")
        self.SearchCustomerBtn.configure(background="#ffffff")
        self.SearchCustomerBtn.configure(disabledforeground="#a3a3a3")
        self.SearchCustomerBtn.configure(foreground="#000000")
        self.SearchCustomerBtn.configure(highlightbackground="#d9d9d9")
        self.SearchCustomerBtn.configure(highlightcolor="black")
        self.SearchCustomerBtn.configure(pady="0")
        self.SearchCustomerBtn.configure(text='''Search''')
        self.SearchCustomerBtn.configure(command=self.SearchCustomer)

        self.DeleteCustomerBtn = tk.Button(self.Frame1)
        self.DeleteCustomerBtn.place(relx=0.276, rely=0.253, height=24, width=64)

        self.DeleteCustomerBtn.configure(activebackground="#ececec")
        self.DeleteCustomerBtn.configure(activeforeground="#000000")
        self.DeleteCustomerBtn.configure(background="#ffffff")
        self.DeleteCustomerBtn.configure(disabledforeground="#a3a3a3")
        self.DeleteCustomerBtn.configure(foreground="#000000")
        self.DeleteCustomerBtn.configure(highlightbackground="#d9d9d9")
        self.DeleteCustomerBtn.configure(highlightcolor="black")
        self.DeleteCustomerBtn.configure(pady="0")
        self.DeleteCustomerBtn.configure(text='''Delete''')
        self.DeleteCustomerBtn.configure(command=self.DeleteCustomer)

        self.UpdateCustomerBtn = tk.Button(self.Frame1)
        self.UpdateCustomerBtn.place(relx=0.276, rely=0.359, height=24, width=67)

        self.UpdateCustomerBtn.configure(activebackground="#ececec")
        self.UpdateCustomerBtn.configure(activeforeground="#000000")
        self.UpdateCustomerBtn.configure(background="#ffffff")
        self.UpdateCustomerBtn.configure(disabledforeground="#a3a3a3")
        self.UpdateCustomerBtn.configure(foreground="#000000")
        self.UpdateCustomerBtn.configure(highlightbackground="#d9d9d9")
        self.UpdateCustomerBtn.configure(highlightcolor="black")
        self.UpdateCustomerBtn.configure(pady="0")
        self.UpdateCustomerBtn.configure(text='''Update''')
        self.UpdateCustomerBtn.configure(command=self.UpdateCustomer)

        self.CustomerCloseBtn = tk.Button(self.Frame1)
        self.CustomerCloseBtn.place(relx=0.207, rely=0.907, height=24, width=91)
        self.CustomerCloseBtn.configure(activebackground="#ececec")
        self.CustomerCloseBtn.configure(activeforeground="#000000")
        self.CustomerCloseBtn.configure(background="#ffffff")
        self.CustomerCloseBtn.configure(disabledforeground="#a3a3a3")
        self.CustomerCloseBtn.configure(foreground="#000000")
        self.CustomerCloseBtn.configure(highlightbackground="#d9d9d9")
        self.CustomerCloseBtn.configure(highlightcolor="black")
        self.CustomerCloseBtn.configure(pady="0")
        self.CustomerCloseBtn.configure(text='''Close Form''')
        self.CustomerCloseBtn.configure(command=self.quit)

        self.DOBLbl = tk.Label(top)
        self.DOBLbl.place(relx=0.067, rely=0.475, height=21, width=72)
        self.DOBLbl.configure(background="#ffffff")
        self.DOBLbl.configure(disabledforeground="#a3a3a3")
        self.DOBLbl.configure(foreground="#000000")
        self.DOBLbl.configure(text='''Date of Birth''')

        self.TownLbl = tk.Label(top)
        self.TownLbl.place(relx=0.117, rely=0.531, height=21, width=45)
        self.TownLbl.configure(background="#ffffff")
        self.TownLbl.configure(disabledforeground="#a3a3a3")
        self.TownLbl.configure(foreground="#000000")
        self.TownLbl.configure(text='''Town''')

        self.PostcodeLbl = tk.Label(top)
        self.PostcodeLbl.place(relx=0.083, rely=0.587, height=21, width=65)
        self.PostcodeLbl.configure(background="#ffffff")
        self.PostcodeLbl.configure(disabledforeground="#a3a3a3")
        self.PostcodeLbl.configure(foreground="#000000")
        self.PostcodeLbl.configure(text='''Postcode''')

        self.EmailLbl = tk.Label(top)
        self.EmailLbl.place(relx=0.117, rely=0.642, height=20, width=44)
        self.EmailLbl.configure(background="#ffffff")
        self.EmailLbl.configure(disabledforeground="#a3a3a3")
        self.EmailLbl.configure(foreground="#000000")
        self.EmailLbl.configure(text='''Email''')

        self.TelephoneLbl = tk.Label(top)
        self.TelephoneLbl.place(relx=0.083, rely=0.698, height=20, width=61)
        self.TelephoneLbl.configure(background="#ffffff")
        self.TelephoneLbl.configure(disabledforeground="#a3a3a3")
        self.TelephoneLbl.configure(foreground="#000000")
        self.TelephoneLbl.configure(text='''Telephone''')

        self.MedicalLbl = tk.Label(top)
        self.MedicalLbl.place(relx=0.0, rely=0.754, height=21, width=109)
        self.MedicalLbl.configure(background="#ffffff")
        self.MedicalLbl.configure(disabledforeground="#a3a3a3")
        self.MedicalLbl.configure(foreground="#000000")
        self.MedicalLbl.configure(text='''Medical Conditions''')

if __name__ == '__main__':
    vp_start_gui()





