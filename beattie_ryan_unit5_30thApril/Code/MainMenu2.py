import sys
import CustomerForm #Import customer form.
import CustomerForm_support #Import support file for the customer form.
import AppointmentForm #Import appointment form.
import AppointmentForm_support #Import support file for appointment form.
import BranchSearch #Import branch search.
import BranchSearch_support #Import support file for branch search.
import tkinter.messagebox #Module to run tkinter message boxes.
import OrderForm #Import order form.
import OrderForm_support #Import support file for order form.
import PrescriptionForm #Import prescription form.
import PrescriptionForm_support #Import support file for prescription form.
import StaffForm
import StaffForm_support


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

import MainMenu2_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    MainMenu2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
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
    MainMenu2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
#Function to close the main menu when the user is finished using the system.
    def quit(self):
        w.destroy()
#Function to open the customer form.
    def CustomerTab(self):
        CustomerForm.create_CustomerForm(root)
#Function to open the appointment form.
    def AppointmentTab(self):
        AppointmentForm.create_AppointmentForm(root)
#Function to open the branch search form.
    def BranchesTab(self):
        BranchSearch.create_BranchSearch(root)
#Function to open the order form.
    def OrderTab(self):
        OrderForm.create_OrderForm(root)
#Function to open the prescription form.
    def PrescriptionTab(self):
        PrescriptionForm.create_PrescriptionForm(root)
#Function to open the staff form
    def StaffTab(self):
        StaffForm.create_Toplevel1(root)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+395+137")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Main Menu")
        top.configure(background="#ffffff")

        self.ButtonCustomer = tk.Button(top)
        self.ButtonCustomer.place(relx=0.1, rely=0.222, height=44, width=87)
        self.ButtonCustomer.configure(activebackground="#ececec")
        self.ButtonCustomer.configure(activeforeground="#000000")
        self.ButtonCustomer.configure(background="#ffffff")
        self.ButtonCustomer.configure(disabledforeground="#a3a3a3")
        self.ButtonCustomer.configure(foreground="#000000")
        self.ButtonCustomer.configure(highlightbackground="#d9d9d9")
        self.ButtonCustomer.configure(highlightcolor="black")
        self.ButtonCustomer.configure(pady="0")
        self.ButtonCustomer.configure(relief="groove")
        self.ButtonCustomer.configure(text='''Customers''')
        self.ButtonCustomer.configure(command=self.CustomerTab)

        self.ButtonAppointments = tk.Button(top)
        self.ButtonAppointments.place(relx=0.1, rely=0.378, height=44, width=87)
        self.ButtonAppointments.configure(activebackground="#ececec")
        self.ButtonAppointments.configure(activeforeground="#000000")
        self.ButtonAppointments.configure(background="#ffffff")
        self.ButtonAppointments.configure(disabledforeground="#a3a3a3")
        self.ButtonAppointments.configure(foreground="#000000")
        self.ButtonAppointments.configure(highlightbackground="#d9d9d9")
        self.ButtonAppointments.configure(highlightcolor="black")
        self.ButtonAppointments.configure(pady="0")
        self.ButtonAppointments.configure(relief="groove")
        self.ButtonAppointments.configure(text='''Appointments''')
        self.ButtonAppointments.configure(command=self.AppointmentTab)

        self.ButtonOrders = tk.Button(top)
        self.ButtonOrders.place(relx=0.1, rely=0.533, height=44, width=87)
        self.ButtonOrders.configure(activebackground="#ececec")
        self.ButtonOrders.configure(activeforeground="#000000")
        self.ButtonOrders.configure(background="#ffffff")
        self.ButtonOrders.configure(disabledforeground="#a3a3a3")
        self.ButtonOrders.configure(foreground="#000000")
        self.ButtonOrders.configure(highlightbackground="#d9d9d9")
        self.ButtonOrders.configure(highlightcolor="black")
        self.ButtonOrders.configure(pady="0")
        self.ButtonOrders.configure(relief="groove")
        self.ButtonOrders.configure(text='''Orders''')
        self.ButtonOrders.configure(command=self.OrderTab)

        self.ButtonProducts = tk.Button(top)
        self.ButtonProducts.place(relx=0.1, rely=0.689, height=44, width=87)
        self.ButtonProducts.configure(activebackground="#ececec")
        self.ButtonProducts.configure(activeforeground="#000000")
        self.ButtonProducts.configure(background="#ffffff")
        self.ButtonProducts.configure(disabledforeground="#a3a3a3")
        self.ButtonProducts.configure(foreground="#000000")
        self.ButtonProducts.configure(highlightbackground="#d9d9d9")
        self.ButtonProducts.configure(highlightcolor="black")
        self.ButtonProducts.configure(pady="0")
        self.ButtonProducts.configure(relief="groove")
        self.ButtonProducts.configure(text='''Products''')

        self.ButtonSuppliers = tk.Button(top)
        self.ButtonSuppliers.place(relx=0.283, rely=0.222, height=44, width=87)
        self.ButtonSuppliers.configure(activebackground="#ececec")
        self.ButtonSuppliers.configure(activeforeground="#000000")
        self.ButtonSuppliers.configure(background="#ffffff")
        self.ButtonSuppliers.configure(disabledforeground="#a3a3a3")
        self.ButtonSuppliers.configure(foreground="#000000")
        self.ButtonSuppliers.configure(highlightbackground="#d9d9d9")
        self.ButtonSuppliers.configure(highlightcolor="black")
        self.ButtonSuppliers.configure(pady="0")
        self.ButtonSuppliers.configure(relief="groove")
        self.ButtonSuppliers.configure(text='''Suppliers''')

        self.ButtonPrescriptions = tk.Button(top)
        self.ButtonPrescriptions.place(relx=0.283, rely=0.378, height=44
                , width=87)
        self.ButtonPrescriptions.configure(activebackground="#ececec")
        self.ButtonPrescriptions.configure(activeforeground="#000000")
        self.ButtonPrescriptions.configure(background="#ffffff")
        self.ButtonPrescriptions.configure(disabledforeground="#a3a3a3")
        self.ButtonPrescriptions.configure(foreground="#000000")
        self.ButtonPrescriptions.configure(highlightbackground="#d9d9d9")
        self.ButtonPrescriptions.configure(highlightcolor="black")
        self.ButtonPrescriptions.configure(pady="0")
        self.ButtonPrescriptions.configure(relief="groove")
        self.ButtonPrescriptions.configure(text='''Prescriptions''')
        self.ButtonPrescriptions.configure(command=self.PrescriptionTab)

        self.ButtonBranches = tk.Button(top)
        self.ButtonBranches.place(relx=0.283, rely=0.533, height=44, width=87)
        self.ButtonBranches.configure(activebackground="#ececec")
        self.ButtonBranches.configure(activeforeground="#000000")
        self.ButtonBranches.configure(background="#ffffff")
        self.ButtonBranches.configure(cursor="fleur")
        self.ButtonBranches.configure(disabledforeground="#a3a3a3")
        self.ButtonBranches.configure(foreground="#000000")
        self.ButtonBranches.configure(highlightbackground="#ffffff")
        self.ButtonBranches.configure(highlightcolor="black")
        self.ButtonBranches.configure(pady="0")
        self.ButtonBranches.configure(relief="groove")
        self.ButtonBranches.configure(text='''Branches''')
        self.ButtonBranches.configure(command=self.BranchesTab)

        self.ButtonStaff = tk.Button(top)
        self.ButtonStaff.place(relx=0.283, rely=0.689, height=44, width=87)
        self.ButtonStaff.configure(activebackground="#ececec")
        self.ButtonStaff.configure(activeforeground="#000000")
        self.ButtonStaff.configure(background="#ffffff")
        self.ButtonStaff.configure(disabledforeground="#a3a3a3")
        self.ButtonStaff.configure(foreground="#000000")
        self.ButtonStaff.configure(highlightbackground="#d9d9d9")
        self.ButtonStaff.configure(highlightcolor="black")
        self.ButtonStaff.configure(pady="0")
        self.ButtonStaff.configure(relief="groove")
        self.ButtonStaff.configure(text='''Staff''')
        self.ButtonStaff.configure(command=self.StaffTab)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.667, rely=0.044, height=41, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.LogOutButton = tk.Button(top)
        self.LogOutButton.place(relx=0.833, rely=0.889, height=34, width=77)
        self.LogOutButton.configure(activebackground="#ececec")
        self.LogOutButton.configure(activeforeground="#000000")
        self.LogOutButton.configure(background="#ffffff")
        self.LogOutButton.configure(disabledforeground="#a3a3a3")
        self.LogOutButton.configure(foreground="#000000")
        self.LogOutButton.configure(highlightbackground="#d9d9d9")
        self.LogOutButton.configure(highlightcolor="black")
        self.LogOutButton.configure(pady="0")
        self.LogOutButton.configure(relief="groove")
        self.LogOutButton.configure(text='''Log Out''')
        self.LogOutButton.configure(command=self.quit)

if __name__ == '__main__':
    vp_start_gui()





