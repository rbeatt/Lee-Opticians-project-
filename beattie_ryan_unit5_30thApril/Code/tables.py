import sqlite3 #Imports SQLite3 to create and write to the database file.
with sqlite3.connect("LeeOpt.db") as db: #Connects to the database file.
    cursor = db.cursor() #Creates the cursor.

#Create a table to store branch details.    
cursor.execute('''
CREATE TABLE IF NOT EXISTS Branches(
BranchID INTEGER PRIMARY KEY,
Town VARCHAR(30) NOT NULL,
Postcode VARCHAR(7) NOT NULL,
Email VARCHAR(30) NOT NULL,
Telephone VARCHAR(15) NOT NULL);
''')

#Create a table for customer records.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer(
CustomerID INTEGER PRIMARY KEY,
BranchID INTEGER NOT NULL,
Name VARCHAR(20) NOT NULL,
Surname VARCHAR(30) NOT NULL,
DateOfBirth DATE NOT NULL,
Town VARCHAR(30) NOT NULL,
Postcode VARCHAR(7) NOT NULL,
EmailAddress VARCHAR(30) NOT NULL,
TelephoneNo VARCHAR(15) NOT NULL,
MedicalConditions TEXT,
FOREIGN KEY(BranchID) REFERENCES Branches(BranchID));
''')

#Create a table for staff records.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Staff(
StaffID INTEGER PRIMARY KEY,
BranchID INTEGER NOT NULL,
Name VARCHAR(20) NOT NULL,
Surname VARCHAR(30) NOT NULL,
Position VARCHAR(15) NOT NULL,
Email VARCHAR(30) NOT NULL,
Telephone VARCHAR(15) NOT NULL,
FOREIGN KEY(BranchID) REFERENCES Branches(BranchID));
''')

#Create a table for supplier records.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Suppliers(
SupplierID INTEGER PRIMARY KEY,
SupplierName VARCHAR(40) NOT NULL,
Postcode VARCHAR(8) NOT NULL,
Email VARCHAR(30) NOT NULL,
Telephone VARCHAR(15) NOT NULL);
''')

#Create a table for product records.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
ProductID INTEGER PRIMARY KEY,
SupplierID INTEGER,
ProductName VARCHAR(30) NOT NULL,
ProductDescription TEXT,
Price REAL NOT NULL,
FOREIGN KEY(SupplierID) REFERENCES Suppliers(SupplierID));
''')

#Create a table for appointments.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments(
AppointmentID INTEGER PRIMARY KEY,
CustomerID INTEGER NOT NULL,
AppointmentDate DATE NOT NULL,
AppointmentTime TEXT NOT NULL,
StaffID INTEGER NOT NULL,
FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
FOREIGN KEY(StaffID) REFERENCES Staff(StaffID));
''')

#Create a table for order records.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders(
OrderID INTEGER PRIMARY KEY,
OrderDate DATE NOT NULL,
BranchID INTEGER NOT NULL,
SupplierID INTEGER NOT NULL,
ProductID INTEGER NOT NULL,
Quantity INTEGER NOT NULL,
OrderTotal REAL,
FOREIGN KEY(SupplierID) REFERENCES Suppliers(SupplierID),
FOREIGN KEY(ProductID) REFERENCES Products(ProductID),
FOREIGN KEY(BranchID) REFERENCES Branches(BranchID));
''')

#Create a table to store login details.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Login(
StaffID INTEGER NOT NULL,
Name VARCHAR(30) NOT NULL,
Password VARCHAR(30) NOT NULL,
AccessLevel INTEGER NOT NULL,
FOREIGN KEY(StaffID) REFERENCES Staff(StaffID));
''')

#Create a table for prescriptions.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Prescriptions(
PrescriptionID INTEGER NOT NULL,
PrescriptionDate VARCHAR(10) NOT NULL,
CustomerID INTEGER NOT NULL,
PrescriptionDetails TEXT,
StaffID INTEGER NOT NULL,
FOREIGN KEY(StaffID) REFERENCES Staff(StaffID));
''')

#Insert the details of the Lee Opticians branches into the branches table.
cursor.execute('''
INSERT INTO Branches (Town, Postcode, Email, Telephone)
VALUES ('Warrenpoint','BT34 3LF', 'info@leeopticians.com','028 4175 3030'),
('Crossmaglen','BT35 9HG','crossmaglen@leeopticians.com','028 3086 8866'),
('Camlough','BT35 7JG','camlough@leeopticians.com','028 3044 2612');
''')

db.commit() #Save the changes made to the database file.

#Insert an admin record into the login table for development and maintenance.
cursor.execute('''
INSERT INTO Login (StaffID, Name, Password, AccessLevel)
VALUES ('0','Ryan','admin123','1');
''')

db.commit() #Save the changes made to the database file.


