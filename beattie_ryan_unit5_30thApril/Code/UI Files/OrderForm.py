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

import OrderForm_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    OrderForm_support.init(root, top)
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
    OrderForm_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x716+394+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Order Form")
        top.configure(background="#ffffff")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.733, rely=0.237, relheight=0.567
                , relwidth=0.208)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.AddBtn = tk.Button(self.Frame1)
        self.AddBtn.place(relx=0.24, rely=0.049, height=24, width=63)
        self.AddBtn.configure(activebackground="#ececec")
        self.AddBtn.configure(activeforeground="#000000")
        self.AddBtn.configure(background="#ffffff")
        self.AddBtn.configure(disabledforeground="#a3a3a3")
        self.AddBtn.configure(foreground="#000000")
        self.AddBtn.configure(highlightbackground="#d9d9d9")
        self.AddBtn.configure(highlightcolor="black")
        self.AddBtn.configure(pady="0")
        self.AddBtn.configure(text='''Add''')

        self.SearchBtn = tk.Button(self.Frame1)
        self.SearchBtn.place(relx=0.24, rely=0.172, height=24, width=66)
        self.SearchBtn.configure(activebackground="#ececec")
        self.SearchBtn.configure(activeforeground="#000000")
        self.SearchBtn.configure(background="#ffffff")
        self.SearchBtn.configure(disabledforeground="#a3a3a3")
        self.SearchBtn.configure(foreground="#000000")
        self.SearchBtn.configure(highlightbackground="#d9d9d9")
        self.SearchBtn.configure(highlightcolor="black")
        self.SearchBtn.configure(pady="0")
        self.SearchBtn.configure(text='''Search''')

        self.DeleteBtn = tk.Button(self.Frame1)
        self.DeleteBtn.place(relx=0.24, rely=0.296, height=24, width=64)
        self.DeleteBtn.configure(activebackground="#ececec")
        self.DeleteBtn.configure(activeforeground="#000000")
        self.DeleteBtn.configure(background="#ffffff")
        self.DeleteBtn.configure(cursor="fleur")
        self.DeleteBtn.configure(disabledforeground="#a3a3a3")
        self.DeleteBtn.configure(foreground="#000000")
        self.DeleteBtn.configure(highlightbackground="#d9d9d9")
        self.DeleteBtn.configure(highlightcolor="black")
        self.DeleteBtn.configure(pady="0")
        self.DeleteBtn.configure(text='''Delete''')

        self.UpdateBtn = tk.Button(self.Frame1)
        self.UpdateBtn.place(relx=0.24, rely=0.419, height=24, width=69)
        self.UpdateBtn.configure(activebackground="#ececec")
        self.UpdateBtn.configure(activeforeground="#000000")
        self.UpdateBtn.configure(background="#ffffff")
        self.UpdateBtn.configure(disabledforeground="#a3a3a3")
        self.UpdateBtn.configure(foreground="#000000")
        self.UpdateBtn.configure(highlightbackground="#d9d9d9")
        self.UpdateBtn.configure(highlightcolor="black")
        self.UpdateBtn.configure(pady="0")
        self.UpdateBtn.configure(text='''Update''')

        self.PrintBtn = tk.Button(self.Frame1)
        self.PrintBtn.place(relx=0.16, rely=0.542, height=24, width=87)
        self.PrintBtn.configure(activebackground="#ececec")
        self.PrintBtn.configure(activeforeground="#000000")
        self.PrintBtn.configure(background="#ffffff")
        self.PrintBtn.configure(cursor="fleur")
        self.PrintBtn.configure(disabledforeground="#a3a3a3")
        self.PrintBtn.configure(foreground="#000000")
        self.PrintBtn.configure(highlightbackground="#d9d9d9")
        self.PrintBtn.configure(highlightcolor="black")
        self.PrintBtn.configure(pady="0")
        self.PrintBtn.configure(text='''Print Invoice''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=1.12, rely=0.714, height=24, width=47)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Button''')

        self.CloseBtn = tk.Button(self.Frame1)
        self.CloseBtn.place(relx=0.16, rely=0.887, height=24, width=91)
        self.CloseBtn.configure(activebackground="#ececec")
        self.CloseBtn.configure(activeforeground="#000000")
        self.CloseBtn.configure(background="#ffffff")
        self.CloseBtn.configure(disabledforeground="#a3a3a3")
        self.CloseBtn.configure(foreground="#000000")
        self.CloseBtn.configure(highlightbackground="#d9d9d9")
        self.CloseBtn.configure(highlightcolor="black")
        self.CloseBtn.configure(pady="0")
        self.CloseBtn.configure(text='''Close Form''')

        self.OrderIDEntry = tk.Entry(top)
        self.OrderIDEntry.place(relx=0.15, rely=0.265, height=20, relwidth=0.523)

        self.OrderIDEntry.configure(background="white")
        self.OrderIDEntry.configure(cursor="fleur")
        self.OrderIDEntry.configure(disabledforeground="#a3a3a3")
        self.OrderIDEntry.configure(font="TkFixedFont")
        self.OrderIDEntry.configure(foreground="#000000")
        self.OrderIDEntry.configure(insertbackground="black")

        self.OrderDateEntry = tk.Entry(top)
        self.OrderDateEntry.place(relx=0.15, rely=0.377, height=20
                , relwidth=0.523)
        self.OrderDateEntry.configure(background="white")
        self.OrderDateEntry.configure(cursor="fleur")
        self.OrderDateEntry.configure(disabledforeground="#a3a3a3")
        self.OrderDateEntry.configure(font="TkFixedFont")
        self.OrderDateEntry.configure(foreground="#000000")
        self.OrderDateEntry.configure(insertbackground="black")

        self.SupplierIDEntry = tk.Entry(top)
        self.SupplierIDEntry.place(relx=0.15, rely=0.433, height=20
                , relwidth=0.523)
        self.SupplierIDEntry.configure(background="white")
        self.SupplierIDEntry.configure(disabledforeground="#a3a3a3")
        self.SupplierIDEntry.configure(font="TkFixedFont")
        self.SupplierIDEntry.configure(foreground="#000000")
        self.SupplierIDEntry.configure(insertbackground="black")

        self.ProductIDEntry = tk.Entry(top)
        self.ProductIDEntry.place(relx=0.15, rely=0.489, height=20
                , relwidth=0.523)
        self.ProductIDEntry.configure(background="white")
        self.ProductIDEntry.configure(disabledforeground="#a3a3a3")
        self.ProductIDEntry.configure(font="TkFixedFont")
        self.ProductIDEntry.configure(foreground="#000000")
        self.ProductIDEntry.configure(insertbackground="black")

        self.QuantityEntry = tk.Entry(top)
        self.QuantityEntry.place(relx=0.15, rely=0.545, height=20
                , relwidth=0.523)
        self.QuantityEntry.configure(background="white")
        self.QuantityEntry.configure(disabledforeground="#a3a3a3")
        self.QuantityEntry.configure(font="TkFixedFont")
        self.QuantityEntry.configure(foreground="#000000")
        self.QuantityEntry.configure(insertbackground="black")

        self.OrderIDLabel = tk.Label(top)
        self.OrderIDLabel.place(relx=0.05, rely=0.265, height=21, width=54)
        self.OrderIDLabel.configure(background="#ffffff")
        self.OrderIDLabel.configure(disabledforeground="#a3a3a3")
        self.OrderIDLabel.configure(foreground="#000000")
        self.OrderIDLabel.configure(text='''OrderID''')

        self.OrderDateLabel = tk.Label(top)
        self.OrderDateLabel.place(relx=0.017, rely=0.377, height=21, width=74)
        self.OrderDateLabel.configure(background="#ffffff")
        self.OrderDateLabel.configure(disabledforeground="#a3a3a3")
        self.OrderDateLabel.configure(foreground="#000000")
        self.OrderDateLabel.configure(text='''OrderDate''')

        self.SupplierIDLabel = tk.Label(top)
        self.SupplierIDLabel.place(relx=0.0, rely=0.433, height=21, width=90)
        self.SupplierIDLabel.configure(background="#ffffff")
        self.SupplierIDLabel.configure(disabledforeground="#a3a3a3")
        self.SupplierIDLabel.configure(foreground="#000000")
        self.SupplierIDLabel.configure(text='''SupplierID''')

        self.ProductIDLabel = tk.Label(top)
        self.ProductIDLabel.place(relx=0.017, rely=0.489, height=21, width=69)
        self.ProductIDLabel.configure(background="#ffffff")
        self.ProductIDLabel.configure(disabledforeground="#a3a3a3")
        self.ProductIDLabel.configure(foreground="#000000")
        self.ProductIDLabel.configure(text='''ProductID''')

        self.QuantityLabel = tk.Label(top)
        self.QuantityLabel.place(relx=0.017, rely=0.545, height=21, width=72)
        self.QuantityLabel.configure(background="#ffffff")
        self.QuantityLabel.configure(disabledforeground="#a3a3a3")
        self.QuantityLabel.configure(foreground="#000000")
        self.QuantityLabel.configure(text='''Quantity''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.333, rely=0.112, height=51, width=174)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"../Users/ryanb/OneDrive - C2k/A2 2020-2021/Computer Science/A2 Unit 5/Code/LeeOpticianslogo.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label6.configure(image=_img0)
        self.Label6.configure(text='''Label''')

        self.BranchIDEntry = tk.Entry(top)
        self.BranchIDEntry.place(relx=0.15, rely=0.321, height=20
                , relwidth=0.523)
        self.BranchIDEntry.configure(background="white")
        self.BranchIDEntry.configure(cursor="fleur")
        self.BranchIDEntry.configure(disabledforeground="#a3a3a3")
        self.BranchIDEntry.configure(font="TkFixedFont")
        self.BranchIDEntry.configure(foreground="#000000")
        self.BranchIDEntry.configure(insertbackground="black")

        self.BranchIDLbl = tk.Label(top)
        self.BranchIDLbl.place(relx=0.033, rely=0.321, height=21, width=64)
        self.BranchIDLbl.configure(background="#ffffff")
        self.BranchIDLbl.configure(disabledforeground="#a3a3a3")
        self.BranchIDLbl.configure(foreground="#000000")
        self.BranchIDLbl.configure(text='''BranchID''')

        self.PriceLbl = tk.Label(top)
        self.PriceLbl.place(relx=0.05, rely=0.601, height=21, width=42)
        self.PriceLbl.configure(background="#ffffff")
        self.PriceLbl.configure(disabledforeground="#a3a3a3")
        self.PriceLbl.configure(foreground="#000000")
        self.PriceLbl.configure(text='''Total''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.15, rely=0.601,height=20, relwidth=0.523)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

if __name__ == '__main__':
    vp_start_gui()





