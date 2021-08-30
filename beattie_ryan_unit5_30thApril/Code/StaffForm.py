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

import StaffForm_support
import os.path
import sqlite3
import tkinter.messagebox

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    StaffForm_support.init(root, top)
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
    StaffForm_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def quit(self):
        w.destroy()

    def ClearEntries(self):
        self.Entry1.delete(0,'end')
        self.Entry2.delete(0,'end')
        self.Entry3.delete(0,'end')
        self.Entry4.delete(0,'end')
        self.Entry5.delete(0,'end')
        self.Entry6.delete(0,'end')
        self.Entry7.delete(0,'end')
        self.Entry8.delete(0,'end')
        self.Entry9.delete(0,'end')

    def AddStaff(self):
        staffid = self.Entry1.get()
        branchid = self.Entry2.get()
        name = self.Entry3.get()
        surname = self.Entry4.get()
        position = self.Entry5.get()
        email = self.Entry6.get()
        telephone = self.Entry7.get()
        password = self.Entry8.get()
        accesslevel = self.Entry9.get()

        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            add_staff = ('''INSERT INTO Staff(StaffID, BranchID, Name, Surname, Position, Email, Telephone)
            VALUES (?,?,?,?,?,?,?)''')
            cursor.execute(add_staff, [(staffid),(branchid),(name),(surname),(position),(email),(telephone)])
            tkinter.messagebox.showinfo("Notification","Staff member added successfully")
            logindetails = ('''INSERT INTO Login(StaffID, Name, Password, AccessLevel)
            VALUES (?,?,?,?)''')
            cursor.execute(logindetails, [(staffid),(name),(password),(accesslevel)])
            tkinter.messagebox.showinfo("Notification","Staff login details created successfully")
            self.ClearEntries()

    def SearchStaff(self):
        staffid = self.Entry1.get()
        name = self.Entry3.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_staff = ('''SELECT * FROM Staff WHERE StaffID = ? OR Name = ?''')
            cursor.execute(search_staff, [(staffid),(name)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    tkinter.messagebox.showinfo("Record Found", "\n".join(str(x) for x in results))
                    self.ClearEntries()
            else:
                tkinter.messagebox.showerror("Error", "No staff member was found with this StaffID or name, please try again.")
                self.ClearEntries()

    def DeleteStaff(self):
        staffid = self.Entry1.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            delete_staff = ('''DELETE FROM Staff WHERE StaffID = ?''')
            cursor.execute(delete_staff, [(staffid)])
            tkinter.messagebox.showinfo("Notification","Staff member deleted successfully")
            delete_login = ('''DELETE FROM Login WHERE StaffID = ?''')
            cursor.execute(delete_login, [(staffid)])
            tkinter.messagebox.showinfo("Notification","Staff member login details deleted successfully")
            self.ClearEntries()

    def UpdateStaff(self):
        staffid = self.Entry1.get()
        branchid = self.Entry2.get()
        name = self.Entry3.get()
        surname = self.Entry4.get()
        position = self.Entry5.get()
        email = self.Entry6.get()
        telephone = self.Entry7.get()
        password = self.Entry8.get()
        accesslevel = self.Entry9.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            update_staff = ('''UPDATE Staff
            SET 
            BranchID = ?,
            Name = ?,
            Surname = ?,
            Position = ?,
            Email = ?,
            Telephone = ?
            WHERE StaffID = ?
            ''')
            db.commit()
            cursor.execute(update_staff,[(branchid),(name),(surname),(position),(email),(telephone),(staffid)])
            tkinter.messagebox.showinfo("Notification","Staff member record updated successfully")
            update_login = ('''UPDATE Login
            SET
            Name = ?,
            Password = ?,
            AccessLevel = ?
            WHERE StaffID = ?
            ''')
            db.commit()
            cursor.execute(update_login,[(name),(password),(accesslevel),(staffid)])
            tkinter.messagebox.showinfo("Notification","Staff member login details updated successfully.")
            self.ClearEntries()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x696+396+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Staff Form")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.35, rely=0.129, height=51, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.7, rely=0.273, relheight=0.568, relwidth=0.208)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.24, rely=0.051, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add''')
        self.Button1.configure(command=self.AddStaff)

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.24, rely=0.177, height=24, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Search''')
        self.Button2.configure(command=self.SearchStaff)

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.24, rely=0.304, height=24, width=67)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Delete''')
        self.Button3.configure(command=self.DeleteStaff)

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.24, rely=0.43, height=24, width=67)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Update''')
        self.Button4.configure(command=self.UpdateStaff)

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.16, rely=0.886, height=24, width=87)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Close Form''')
        self.Button5.configure(command=self.quit)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.167, rely=0.302,height=20, relwidth=0.49)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.167, rely=0.359,height=20, relwidth=0.49)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.167, rely=0.417,height=20, relwidth=0.49)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.167, rely=0.474,height=20, relwidth=0.49)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.167, rely=0.532,height=20, relwidth=0.49)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.167, rely=0.589,height=20, relwidth=0.49)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Entry7 = tk.Entry(top)
        self.Entry7.place(relx=0.167, rely=0.647,height=20, relwidth=0.49)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Entry8 = tk.Entry(top)
        self.Entry8.place(relx=0.167, rely=0.704,height=20, relwidth=0.49)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")

        self.Entry9 = tk.Entry(top)
        self.Entry9.place(relx=0.167, rely=0.761,height=20, relwidth=0.49)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.302, height=21, width=54)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''StaffID''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.05, rely=0.359, height=21, width=64)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BranchID''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.067, rely=0.417, height=21, width=54)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Name''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.05, rely=0.474, height=21, width=64)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Surname''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.05, rely=0.532, height=21, width=64)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Position''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.067, rely=0.589, height=21, width=54)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Email''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.033, rely=0.647, height=21, width=74)
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Telephone''')

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.05, rely=0.704, height=21, width=64)
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Password''')

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.033, rely=0.761, height=21, width=74)
        self.Label10.configure(background="#ffffff")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''AccessLevel''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





