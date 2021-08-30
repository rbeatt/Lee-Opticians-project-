Run index.py to start the application. 

===== LOGIN DETAILS =====
Admin Login Details - User Access Level 1
STAFFID - 0 
PASSWORD - admin123

===== ACCESS LEVELS =====
Level 1 - full access to the system.
Level 2 - created for receptionists, provides limited access to the system.
Level 3 - created for optometrists, provides limited access to the system.

===== CREATING A NEW USER =====
Creating a new user is done using the staff form. Creating a new staff record using this form automatically creates a record in the login table, which is used to log into the system.
Updating and deleting records using this form also applies the changes made to the record in the login table.

==== VALIDATION =====
Primary keys must be an integer. A value error wil occur and an error message will be displayed if the user attempts to enter a non-integer character. 
Primary keys are unique. An error will be displayed if the user attempts to create a new record with an existing primary key.
Primary keys must not be null, or a value error will occur and an error message will be displayed. 
Validation methods are used throughout the system. For a full list of the validation methods used and where they are used, view Design.pdf in the Documentation folder.

===== ADDING RECORDS ======
To add records to the database, the forms must be used. Fill in the forms with the relevant data and click the add button. A message box should be displayed telling the user a record has been added.

===== DELETING RECORDS =====
To delete records from the database, input the ID of the record and click the delete button. A message box should be displayed.

===== UPDATING RECORDS ======
To update records in the database, input the ID of the record and fill in the form with the updated details. A message box should be displayed.

===== SEARCHING RECORDS =====
To search records in the database, input the ID of the record and click the search button. A message box should be displayed showing the search results. For some forms, it is possible to search by name.

*Error messages with instructions or prompts as to what caused the error will be displayed if an error occurs when using the system. 

===== OUTPUTS =====
Outputs include screen outputs and the two text files: orderinvoice.txt and prescription.txt. When an order invoice or prescription is generated using the forms on the system, open the text files to view.


