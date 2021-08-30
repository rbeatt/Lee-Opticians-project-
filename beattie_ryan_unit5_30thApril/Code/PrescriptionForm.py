#Import modules
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

from PIL import Image, ImageTk #Module to display the Lee Opticians logo on the form.

import PrescriptionForm_support
import os.path
import sqlite3 #SQLite3 module to access the database file.
import tkinter.messagebox #Module to run tkinter message boxes.


def vp_start_gui(): #Function to start
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    PrescriptionForm_support.init(root, top)
    root.mainloop()

w = None
def create_PrescriptionForm(rt, *args, **kwargs): #Function to create the form screen.
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
    PrescriptionForm_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
#Function to close the window when the user is finished using the form.    
    def quit(self): 
        w.destroy()

#Function to clear the entries on the form when a function is performed.
    def ClearEntries(self):
        self.PresIDEntry.delete(0,'end') #Deletes all data inside the entry box.
        self.PresDateEntry.delete(0,'end')
        self.CustomerIDEntry.delete(0,'end')
        self.PresDetailsEntry.delete(0,'end')
        self.StaffIDEntry.delete(0,'end')

#Function to add a record to the prescriptions table.
    def AddPrescription(self):
        presid = self.PresIDEntry.get() #Retrives the data input to the entry box by the user.
        presdate = self.PresDateEntry.get()
        customerid = self.CustomerIDEntry.get()
        presdetails = self.PresDetailsEntry.get()
        staffid = self.StaffIDEntry.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            add_prescription = ('''INSERT INTO Prescriptions(PrescriptionID, PrescriptionDate, CustomerID, PrescriptionDetails, StaffID)
            VALUES (?,?,?,?,?)''') #SQL statement to add a new record.
            cursor.execute(add_prescription, [(presid),(presdate),(customerid),(presdetails),(staffid)]) #Runs the SQL statement using the data input by the user.
            tkinter.messagebox.showinfo("Notification","Prescription created successfully") #Tkinter message box to prompt the user the record has been added successfully.
            self.ClearEntries()

#Function to delete a record from the prescriptions table.
    def DeletePrescription(self):
        presid = self.PresIDEntry.get() #Retrieves the data input to the entry box by the user.
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            delete_prescription = ('''DELETE FROM Prescriptions WHERE PrescriptionID = ?''') #SQL statement to delete an existing record.
            cursor.execute(delete_prescription, [(presid)]) #Runs the SQL statement using the PrescriptionID input by the user.
            tkinter.messagebox.showinfo("Notification","Prescription deleted successfully") #Tkinter message box to prompt the user the record has been deleted successfully.
            self.ClearEntries()

#Function to make changes to a record from the prescriptions table.
    def UpdatePrescription(self):
        presid = self.PresIDEntry.get() #Retrieves the data input to the entry box by the user.
        presdate = self.PresDateEntry.get()
        customerid = self.CustomerIDEntry.get()
        presdetails = self.PresDetailsEntry.get()
        staffid = self.StaffIDEntry.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            update_prescription = ('''UPDATE Prescriptions
            SET 
            PrescriptionDate = ?,
            CustomerID = ?,
            PrescriptionDetails = ?,
            StaffID = ?,
            WHERE PrescriptionID = ?
            ''') #SQL statement to update the existing record with the data input by the user to the entry boxes.
            db.commit() #Saves the changes made to the .db file.

            cursor.execute(update_prescription, [(presdate),(customerid),(presdetails),(staffid),(presid)]) #Runs the SQL statement using the data input by the user.
            tkinter.messagebox.showinfo("Notification","Prescription updated successfully") #Tkinter message box to prompt the user the record has been updated successfully.
            self.ClearEntries()

#Function to search for a record from the prescriptions table.
    def SearchPrescription(self):
        presid = self.PresIDEntry.get() #Retrieves the data input to the entry box by the user.
        customerid = self.CustomerIDEntry.get()

        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_prescription = ('''SELECT * FROM Prescriptions WHERE PrescriptionID = ? OR CustomerID = ?''') #SQL statement to retrive the record with the PrescriptionID or CustomerID input by the user.
            cursor.execute(search_prescription, [(presid),(customerid)]) #Runs the SQL statement using the PrescriptionID or CustomerID input by the user.
            results = cursor.fetchall() #Returns all results with the corresponding PrescriptionID or CustomerID.

            if results:
                for x in results:
                    tkinter.messagebox.showinfo("Record Found", "\n".join(str(x) for x in results)) #If a record is found, the fields will be displayed in a Tkinter message box. 
                    self.ClearEntries()
            else:
                tkinter.messagebox.showerror("Error", "No prescription was found with this PrescriptionID or CustomerID, please try again.") #If a record isn't found, a message box will prompt the user with an error.
                self.ClearEntries()

#Function to create a prescription, of which the user can view and print, using a .txt file.
    def PrintOrder(self):
        presid = self.PresIDEntry.get() #Retrieves the data input to the entry box by the user.

        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_prescription = ('''SELECT * FROM Prescriptions WHERE PrescriptionID = ?''') #SQL statement to retrieve the record with the PrescriptionID input by the user.
            cursor.execute(search_prescription, [(presid)]) #Runs the SQL statement using the PrescriptionID input by the user.
            results = cursor.fetchall() #Returns all results with the corresponding PrescriptionID. 

        if results:
            for x in results:
                write = open("prescription.txt","w") #Opens the .txt file to write to. Each time this function is run, the .txt file will be overwritten. 
                write.write("""
//=============================================================================//
//                           CUSTOMER PRESCRIPTION                             //
//=============================================================================//
//=============================================================================//
// PRESCRIPTIONID, PRESCRIPTIONDATE, CUSTOMERID, PRESCRIPTIONDETAILS, STAFFID  //
//=============================================================================//
""") #A template with the field headings is written to the .txt file.

            for x in results:
                write.write(str(x)) #Writes the fields of the matching record to the .txt file.
                write.close() #The .txt file is closed.
                tkinter.messagebox.showinfo("Notification","Prescription generated successfully, please open the .txt file to view and print.") #A message box prompting the user a prescription has been created successfully.
                self.ClearEntries()
        else:
            tkinter.messagebox.showerror("Error", "No prescription was found with this PrescriptionID or CustomerID, please try again.") #A message box prompting the user with an error.
            self.ClearEntries()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x696+381+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Prescription Form")
        top.configure(background="#ffffff")
#Logo displayed at the top of the form
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.35, rely=0.144, height=41, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg") #Lee Opticians logo file destination
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')
#Frame where buttons to operate the form are included.
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.733, rely=0.273, relheight=0.496
                , relwidth=0.208)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

#Add button
        self.AddButton = tk.Button(self.Frame1)
        self.AddButton.place(relx=0.24, rely=0.058, height=24, width=67)
        self.AddButton.configure(activebackground="#ececec")
        self.AddButton.configure(activeforeground="#000000")
        self.AddButton.configure(background="#ffffff")
        self.AddButton.configure(disabledforeground="#a3a3a3")
        self.AddButton.configure(foreground="#000000")
        self.AddButton.configure(highlightbackground="#d9d9d9")
        self.AddButton.configure(highlightcolor="black")
        self.AddButton.configure(pady="0")
        self.AddButton.configure(text='''Add''')
        self.AddButton.configure(command = self.AddPrescription) #Runs the add function when clicked by the user.

#Search button
        self.SearchButton = tk.Button(self.Frame1)
        self.SearchButton.place(relx=0.24, rely=0.203, height=24, width=67)
        self.SearchButton.configure(activebackground="#ececec")
        self.SearchButton.configure(activeforeground="#000000")
        self.SearchButton.configure(background="#ffffff")
        self.SearchButton.configure(disabledforeground="#a3a3a3")
        self.SearchButton.configure(foreground="#000000")
        self.SearchButton.configure(highlightbackground="#d9d9d9")
        self.SearchButton.configure(highlightcolor="black")
        self.SearchButton.configure(pady="0")
        self.SearchButton.configure(text='''Search''')
        self.SearchButton.configure(command = self.SearchPrescription) #Runs the search function when clicked by the user.

#Update button
        self.UpdateButton = tk.Button(self.Frame1)
        self.UpdateButton.place(relx=0.24, rely=0.493, height=24, width=67)
        self.UpdateButton.configure(activebackground="#ececec")
        self.UpdateButton.configure(activeforeground="#000000")
        self.UpdateButton.configure(background="#ffffff")
        self.UpdateButton.configure(disabledforeground="#a3a3a3")
        self.UpdateButton.configure(foreground="#000000")
        self.UpdateButton.configure(highlightbackground="#d9d9d9")
        self.UpdateButton.configure(highlightcolor="black")
        self.UpdateButton.configure(pady="0")
        self.UpdateButton.configure(text='''Update''')
        self.UpdateButton.configure(command = self.UpdatePrescription) #Runs the update function when clicked by the user,

#Print button
        self.PrintButton = tk.Button(self.Frame1)
        self.PrintButton.place(relx=0.08, rely=0.638, height=24, width=102)
        self.PrintButton.configure(activebackground="#ececec")
        self.PrintButton.configure(activeforeground="#000000")
        self.PrintButton.configure(background="#ffffff")
        self.PrintButton.configure(disabledforeground="#a3a3a3")
        self.PrintButton.configure(foreground="#000000")
        self.PrintButton.configure(highlightbackground="#d9d9d9")
        self.PrintButton.configure(highlightcolor="black")
        self.PrintButton.configure(pady="0")
        self.PrintButton.configure(text='''Print Prescription''')
        self.PrintButton.configure(command = self.PrintOrder) #Runs the print function when clicked by the user.

#Close button
        self.CloseButton = tk.Button(self.Frame1)
        self.CloseButton.place(relx=0.16, rely=0.87, height=24, width=87)
        self.CloseButton.configure(activebackground="#ececec")
        self.CloseButton.configure(activeforeground="#000000")
        self.CloseButton.configure(background="#ffffff")
        self.CloseButton.configure(disabledforeground="#a3a3a3")
        self.CloseButton.configure(foreground="#000000")
        self.CloseButton.configure(highlightbackground="#d9d9d9")
        self.CloseButton.configure(highlightcolor="black")
        self.CloseButton.configure(pady="0")
        self.CloseButton.configure(text='''Close Form''')
        self.CloseButton.configure(command = self.quit) #Runs the close function when clicked by the user.

#PrescriptionID label
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.05, rely=0.302, height=21, width=80)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''PrescriptionID''')

#PrescriptionID entry
        self.PresIDEntry = tk.Entry(top)
        self.PresIDEntry.place(relx=0.2, rely=0.302,height=20, relwidth=0.473)
        self.PresIDEntry.configure(background="white")
        self.PresIDEntry.configure(disabledforeground="#a3a3a3")
        self.PresIDEntry.configure(font="TkFixedFont")
        self.PresIDEntry.configure(foreground="#000000")
        self.PresIDEntry.configure(insertbackground="black")

#Prescription date
        self.PresDateEntry = tk.Entry(top)
        self.PresDateEntry.place(relx=0.2, rely=0.359, height=20, relwidth=0.473)
        self.PresDateEntry.configure(background="white")
        self.PresDateEntry.configure(disabledforeground="#a3a3a3")
        self.PresDateEntry.configure(font="TkFixedFont")
        self.PresDateEntry.configure(foreground="#000000")
        self.PresDateEntry.configure(insertbackground="black")

#CustomerID entry
        self.CustomerIDEntry = tk.Entry(top)
        self.CustomerIDEntry.place(relx=0.2, rely=0.417, height=20
                , relwidth=0.473)
        self.CustomerIDEntry.configure(background="white")
        self.CustomerIDEntry.configure(disabledforeground="#a3a3a3")
        self.CustomerIDEntry.configure(font="TkFixedFont")
        self.CustomerIDEntry.configure(foreground="#000000")
        self.CustomerIDEntry.configure(insertbackground="black")

#Prescription date entry
        self.PresDetailsEntry = tk.Entry(top)
        self.PresDetailsEntry.place(relx=0.2, rely=0.474, height=90
                , relwidth=0.473)
        self.PresDetailsEntry.configure(background="white")
        self.PresDetailsEntry.configure(disabledforeground="#a3a3a3")
        self.PresDetailsEntry.configure(font="TkFixedFont")
        self.PresDetailsEntry.configure(foreground="#000000")
        self.PresDetailsEntry.configure(insertbackground="black")

#StaffID entry
        self.StaffIDEntry = tk.Entry(top)
        self.StaffIDEntry.place(relx=0.2, rely=0.632,height=20, relwidth=0.473)
        self.StaffIDEntry.configure(background="white")
        self.StaffIDEntry.configure(disabledforeground="#a3a3a3")
        self.StaffIDEntry.configure(font="TkFixedFont")
        self.StaffIDEntry.configure(foreground="#000000")
        self.StaffIDEntry.configure(insertbackground="black")

#PrescriptionDate entry
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.017, rely=0.359, height=21, width=103)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''PrescriptionDate''')

#CustomerID label
        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.05, rely=0.417, height=21, width=79)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''CustomerID''')

#PrescriptionDetails label
        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.0, rely=0.474, height=21, width=104)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''PrescriptionDetails''')

#StaffID label
        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.083, rely=0.632, height=21, width=61)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''StaffID''')

#Delete button
        self.DeleteButton = tk.Button(top)
        self.DeleteButton.place(relx=0.783, rely=0.445, height=24, width=67)
        self.DeleteButton.configure(activebackground="#ececec")
        self.DeleteButton.configure(activeforeground="#000000")
        self.DeleteButton.configure(background="#ffffff")
        self.DeleteButton.configure(disabledforeground="#a3a3a3")
        self.DeleteButton.configure(foreground="#000000")
        self.DeleteButton.configure(highlightbackground="#d9d9d9")
        self.DeleteButton.configure(highlightcolor="black")
        self.DeleteButton.configure(pady="0")
        self.DeleteButton.configure(text='''Delete''')
        self.DeleteButton.configure(command = self.DeletePrescription) #Runs the delete function when clicked by the user.

if __name__ == '__main__':
    vp_start_gui() #Runs the function to open the window.





