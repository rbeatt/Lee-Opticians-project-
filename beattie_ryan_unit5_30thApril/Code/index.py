#Import modules
import sys
import sqlite3 #SQLite3 module to access the database.
import time
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

from PIL import Image, ImageTk #Module to display Lee Opticians logo.

import LoginScreen #Import the login screen.
import LoginScreen_support #Import the support file for the login screen.
import os.path
import tkinter.messagebox #Module to run tkinter message boxes.

LoginScreen.vp_start_gui() #Function to start the program.
