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

import BranchSearch_support
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
    BranchSearch_support.init(root, top)
    root.mainloop()

w = None
def create_BranchSearch(rt, *args, **kwargs):
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
    BranchSearch_support.init(w, top, *args, **kwargs)
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


    def SearchBranches(self):
        branchid = self.Entry1.get()
        town = self.Entry2.get()
        with sqlite3.connect("LeeOpt.db") as db:
            cursor = db.cursor()
            search_branch= ('''SELECT * FROM Branches WHERE BranchID = ? OR Town =?''')
            cursor.execute(search_branch, [(branchid),(town)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    tkinter.messagebox.showinfo("Record Found", "\n".join(str(x) for x in results))
                    self.ClearEntries()
            else:
                tkinter.messagebox.showerror("Error", "No record was found with this BranchID or Town name, please try again.")
                self.ClearEntries()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("329x242+425+136")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Branch Search")
        top.configure(background="#ffffff")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.243, rely=0.413,height=20, relwidth=0.559)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.061, rely=0.413, height=21, width=50)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''BranchID''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.426, rely=0.744, height=24, width=56)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(command=self.SearchBranches)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.243, rely=0.083, height=42, width=176)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)
        self.Label2.configure(text='''Label''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.79, rely=0.826, height=24, width=50)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Close''')
        self.Button2.configure(command=self.quit)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.243, rely=0.579,height=20, relwidth=0.559)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.091, rely=0.579, height=21, width=45)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Town''')

if __name__ == '__main__':
    vp_start_gui()





