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

import AppointmentForm_support
import os.path
import sqlite3
import tkinter.messagebox
from datetime import datetime
import time

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    AppointmentForm_support.init(root, top)
    root.mainloop()

w = None
def create_AppointmentForm(rt, *args, **kwargs):
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
    AppointmentForm_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def quit(self): #Function to close the form window
        w.destroy()

    def ClearEntries(self): #Function to clear the entries of the form
        self.Entry1.delete(0,'end') #AppointmentID
        self.Entry2.delete(0,'end') #CustomerID
        self.Entry3.delete(0,'end') #AppointmentDate
        self.Entry4.delete(0,'end') #AppointmentTime
        self.Entry5.delete(0,'end') #StaffID

    def ClearDate(self):
        self.Entry3.delete(0,'end')

    def ClearTime(self):
        self.Entry4.delete(0,'end')
    
    def ClearID(self):
        self.Entry1.delete(0,'end')

    def dateformat(self): #Function to perform a format check on the date of birth
        date = self.Entry3.get() #Date entry
        try:
            if date != datetime.strptime(date, "%d/%m/%Y").strftime('%d/%m/%Y'): #If the date input by the user doesn't match the specified format, a value error is raised.
                raise ValueError
            return True
        except ValueError:
            tkinter.messagebox.showerror("Error","Please enter the appointment date in the correct format DD/MM/YYYY") #Error message if the input does not match the pre-defined format.
            self.ClearDate() #Clears the date entry.
            return False

    def timeformat(self): #Function to perform a format check on the time.
        apptime = self.Entry4.get() #Time entry
        try:
            if apptime != datetime.strptime(apptime, "%H:%M").strftime('%H:%M'): #If the time input by the user doesn't match the specified format, a value error is raised.
                raise ValueError
            return True
        except ValueError:
            tkinter.messagebox.showerror("Error","Please enter the appointment time in the correct 24hr format HH:MM") #Error message if the input does not match the pre-defined format.
            self.ClearTime() #Clears the time entry.
            return False

    def idpresence(self): #Function to perform a presence check on the AppointmentID.
        appointmentid = self.Entry1.get() #AppointmentID entry
        try:
            if appointmentid == "": #If the field is blank, a value error is raised.
                raise ValueError
            return True
        except ValueError:
            tkinter.messagebox.showerror("Error","The AppointmentID field cannot be left blank. Please enter an AppointmentID.") #Error message if the ID field is left blank.
            self.ClearID() #Clears the ID entry
            return False

    def AddAppointment(self):
        appointmentid = self.Entry1.get()
        customerid = self.Entry2.get()
        date = self.Entry3.get()
        apptime = self.Entry4.get()
        staffid = self.Entry5.get()

        if self.dateformat() and self.timeformat() and self.idpresence():
            try:
                with sqlite3.connect("LeeOpt.db") as db:
                    cursor = db.cursor()
                    add_appointment = ('''INSERT INTO Appointments(AppointmentID, CustomerID, AppointmentDate, AppointmentTime, StaffID)
                    VALUES (?,?,?,?,?)''')
                    cursor.execute(add_appointment, [(appointmentid),(customerid),(date),(apptime),(staffid)])
                    tkinter.messagebox.showinfo("Notification","Appointment added successfully")
                    self.ClearEntries()
            except (sqlite3.IntegrityError):
                tkinter.messagebox.showerror("Error","This AppointmentID is already taken, please try another.")
                self.ClearID()


    def DeleteAppointment(self):
        appointmentid = self.Entry1.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            delete_appointment = ('''DELETE FROM Appointments WHERE AppointmentID = ?''')
            cursor.execute(delete_appointment, [(appointmentid)])
            tkinter.messagebox.showinfo("Notification","Appointment deleted successfully")
            self.ClearEntries()

    def UpdateAppointment(self):
        appointmentid = self.Entry1.get()
        date = self.Entry3.get()
        apptime = self.Entry4.get()
        staffid = self.Entry5.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            update_appointment = ('''UPDATE Appointments 
            SET 
            AppointmentDate = ?,
            AppointmentTime = ?,
            StaffID = ?
            WHERE AppointmentID = ?
            ''')
            db.commit()
            
            cursor.execute(update_appointment,[(date),(apptime),(staffid),(appointmentid)])
            tkinter.messagebox.showinfo("Notification","Appointment record updated successfully")
            self.ClearEntries()

    def SearchAppointments(self):
        appointmentid = self.Entry1.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_appointments = ('''SELECT * FROM Appointments WHERE AppointmentID = ?''')
            cursor.execute(search_appointments, [(appointmentid)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    tkinter.messagebox.showinfo("Record Found", "\n".join(str(x) for x in results))
                    self.ClearEntries()
            else:
                tkinter.messagebox.showerror("Error", "No record was found with this AppointmentID, please try again.")
                self.ClearEntries()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x696+425+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Appointment Form")
        top.configure(background="#ffffff")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.167, rely=0.244,height=20, relwidth=0.49)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.167, rely=0.302,height=20, relwidth=0.49)
        self.Entry2.configure(background="white")
        self.Entry2.configure(cursor="fleur")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.167, rely=0.359,height=20, relwidth=0.49)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.167, rely=0.417,height=20, relwidth=0.49)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.167, rely=0.474,height=20, relwidth=0.49)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.717, rely=0.23, relheight=0.408, relwidth=0.208)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.AddBtn = tk.Button(self.Frame1)
        self.AddBtn.place(relx=0.24, rely=0.07, height=24, width=57)
        self.AddBtn.configure(activebackground="#ececec")
        self.AddBtn.configure(activeforeground="#000000")
        self.AddBtn.configure(background="#ffffff")
        self.AddBtn.configure(disabledforeground="#a3a3a3")
        self.AddBtn.configure(foreground="#000000")
        self.AddBtn.configure(highlightbackground="#d9d9d9")
        self.AddBtn.configure(highlightcolor="black")
        self.AddBtn.configure(pady="0")
        self.AddBtn.configure(text='''Add''')
        self.AddBtn.configure(command=self.AddAppointment)

        self.SearchBtn = tk.Button(self.Frame1)
        self.SearchBtn.place(relx=0.24, rely=0.246, height=24, width=57)
        self.SearchBtn.configure(activebackground="#ececec")
        self.SearchBtn.configure(activeforeground="#000000")
        self.SearchBtn.configure(background="#ffffff")
        self.SearchBtn.configure(disabledforeground="#a3a3a3")
        self.SearchBtn.configure(foreground="#000000")
        self.SearchBtn.configure(highlightbackground="#d9d9d9")
        self.SearchBtn.configure(highlightcolor="black")
        self.SearchBtn.configure(pady="0")
        self.SearchBtn.configure(text='''Search''')
        self.SearchBtn.configure(command=self.SearchAppointments)

        self.DeleteBtn = tk.Button(self.Frame1)
        self.DeleteBtn.place(relx=0.24, rely=0.423, height=24, width=57)
        self.DeleteBtn.configure(activebackground="#ececec")
        self.DeleteBtn.configure(activeforeground="#000000")
        self.DeleteBtn.configure(background="#ffffff")
        self.DeleteBtn.configure(disabledforeground="#a3a3a3")
        self.DeleteBtn.configure(foreground="#000000")
        self.DeleteBtn.configure(highlightbackground="#d9d9d9")
        self.DeleteBtn.configure(highlightcolor="black")
        self.DeleteBtn.configure(pady="0")
        self.DeleteBtn.configure(text='''Delete''')
        self.DeleteBtn.configure(command=self.DeleteAppointment)

        self.UpdateBtn = tk.Button(self.Frame1)
        self.UpdateBtn.place(relx=0.24, rely=0.599, height=24, width=57)
        self.UpdateBtn.configure(activebackground="#ececec")
        self.UpdateBtn.configure(activeforeground="#000000")
        self.UpdateBtn.configure(background="#ffffff")
        self.UpdateBtn.configure(disabledforeground="#a3a3a3")
        self.UpdateBtn.configure(foreground="#000000")
        self.UpdateBtn.configure(highlightbackground="#d9d9d9")
        self.UpdateBtn.configure(highlightcolor="black")
        self.UpdateBtn.configure(pady="0")
        self.UpdateBtn.configure(text='''Update''')
        self.UpdateBtn.configure(command=self.UpdateAppointment)

        self.CloseBtn = tk.Button(self.Frame1)
        self.CloseBtn.place(relx=0.16, rely=0.845, height=24, width=77)
        self.CloseBtn.configure(activebackground="#ececec")
        self.CloseBtn.configure(activeforeground="#000000")
        self.CloseBtn.configure(background="#ffffff")
        self.CloseBtn.configure(cursor="fleur")
        self.CloseBtn.configure(disabledforeground="#a3a3a3")
        self.CloseBtn.configure(foreground="#000000")
        self.CloseBtn.configure(highlightbackground="#d9d9d9")
        self.CloseBtn.configure(highlightcolor="black")
        self.CloseBtn.configure(pady="0")
        self.CloseBtn.configure(text='''Close Form''')
        self.CloseBtn.configure(command=self.quit)

        self.AppointmentLbl = tk.Label(top)
        self.AppointmentLbl.place(relx=0.017, rely=0.244, height=21, width=88)
        self.AppointmentLbl.configure(background="#ffffff")
        self.AppointmentLbl.configure(disabledforeground="#a3a3a3")
        self.AppointmentLbl.configure(foreground="#000000")
        self.AppointmentLbl.configure(text='''AppointmentID''')

        self.CustomerLbl = tk.Label(top)
        self.CustomerLbl.place(relx=0.05, rely=0.302, height=21, width=64)
        self.CustomerLbl.configure(background="#ffffff")
        self.CustomerLbl.configure(cursor="fleur")
        self.CustomerLbl.configure(disabledforeground="#a3a3a3")
        self.CustomerLbl.configure(foreground="#000000")
        self.CustomerLbl.configure(text='''CustomerID''')

        self.DateLbl = tk.Label(top)
        self.DateLbl.place(relx=0.1, rely=0.359, height=21, width=31)
        self.DateLbl.configure(background="#ffffff")
        self.DateLbl.configure(cursor="fleur")
        self.DateLbl.configure(disabledforeground="#a3a3a3")
        self.DateLbl.configure(foreground="#000000")
        self.DateLbl.configure(text='''Date''')

        self.TimeLbl = tk.Label(top)
        self.TimeLbl.place(relx=0.1, rely=0.417, height=21, width=32)
        self.TimeLbl.configure(background="#ffffff")
        self.TimeLbl.configure(disabledforeground="#a3a3a3")
        self.TimeLbl.configure(foreground="#000000")
        self.TimeLbl.configure(text='''Time''')

        self.StaffLbl = tk.Label(top)
        self.StaffLbl.place(relx=0.083, rely=0.474, height=21, width=41)
        self.StaffLbl.configure(background="#ffffff")
        self.StaffLbl.configure(disabledforeground="#a3a3a3")
        self.StaffLbl.configure(foreground="#000000")
        self.StaffLbl.configure(text='''StaffID''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.35, rely=0.101, height=41, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()





