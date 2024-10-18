import tkinter
import tkinter.ttk
import tkinter as tk
from tkinter import PhotoImage
import tkinter.messagebox
from datetime import datetime           
import sqlite3
# import os
# from PIL import Image,ImageTk

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_table (id PRIMARYKEY text, firstname text, lastname text, dateOfBirth text, gender text, address text, contactNumber text, emailAddress text, bloodType text, history text, currentdate text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, firstname, lastname, dateOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, currentdate):
        self.dbCursor.execute("INSERT INTO patient_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        id, firstname, lastname, dateOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, currentdate))
        self.dbConnection.commit()

    def Update(self, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, currentdate, id):
        self.dbCursor.execute(
            "UPDATE patient_table SET firstname = ?, lastname = ?, dateOfBirth = ?, gender = ?, address = ?, contactNumber = ?, emailAddress = ?, bloodType = ?, history = ?, currentdate = ? WHERE id = ?",
            (firstname, lastname, dateOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, currentdate, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM patient_table WHERE id = ?", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM patient_table WHERE id = ?", (id,))
        tkinter.messagebox.showinfo("Deleted data", "Successfully Deleted the Patient data in the database")
        self.dbConnection.commit()

    def Display(self, currentdate):
        self.dbCursor.execute("SELECT * FROM patient_table WHERE currentdate = ?", (currentdate,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

class Values:
    def Validate(self, id, firstname, lastname, contactNumber, emailAdress, dateType, currentdate):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (firstname.isalpha()):
            return "firstname"
        elif not (lastname.isalpha()):
            return "lastname"
        elif not (contactNumber.isdigit() and (len(contactNumber) == 10)):
            return "contactNumber"
        elif not (emailAdress.count("@") == 1 and emailAdress.count(".") > 0):
            return "emailAddress"
        elif not (dateType.count("-") == 2):
            return "dateOfBirth"
        elif not (currentdate.count("-") == 2):
            return "dateOfBirth"
        else:
            return "DONE"

        
class InsertWindow:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Enter Patient Information")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        bg_color = "deeppink"
        fg_color = "white"


        self.id = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.contactNumber = tkinter.StringVar()
        self.emailAddress = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.currentdate = tkinter.StringVar()
        self.dateType = tkinter.StringVar()

        self.genderType = ["Male", "Female", "Transgender", "Other"]
        # self.dateType = datetime.strptime("%Y-%m-%d")
        self.bloodListType = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient Id", font=("times new roman",10,"bold"), width=65, height=2).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, text="Patient First Name", font=("times new roman",10,"bold"), width=65, height=2).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Patient Last Name", width=65, height=2).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Date of Birth", width=65, height=2).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Gender", width=65, height=2).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Address", width=65, height=2).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Contact Number", width=65, height=2).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Email Address", width=65, height=2).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Blood Type", width=65, height=2).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Patient Problem", width=65, height=2).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Current date", width=65, height=2).grid(pady=5, column=1, row=11)


        self.idEntry = tkinter.Entry(self.window, width=65,   textvariable=self.id)
        self.firstnameEntry = tkinter.Entry(self.window, width=65,  textvariable=self.firstname)
        self.lastnameEntry = tkinter.Entry(self.window, width=65,  textvariable=self.lastname)
        self.addressEntry = tkinter.Entry(self.window, width=65,  textvariable=self.address)
        self.contactNumberEntry = tkinter.Entry(self.window, width=65,  textvariable=self.contactNumber)
        self.emailAddressEntry = tkinter.Entry(self.window, width=65,  textvariable=self.emailAddress)
        self.historyEntry = tkinter.Entry(self.window, width=65,  textvariable=self.history)
        self.currentdateEntry = tkinter.Entry(self.window, width=65,  textvariable=self.currentdate)
        self.dateTypeEntry = tkinter.Entry(self.window, width=65, textvariable=self.dateType)

        self.idEntry.grid(pady=5, column=3, row=1)
        self.firstnameEntry.grid(pady=5, column=3, row=2)
        self.lastnameEntry.grid(pady=5, column=3, row=3)
        self.addressEntry.grid(pady=5, column=3, row=6)
        self.contactNumberEntry.grid(pady=5, column=3, row=7)
        self.emailAddressEntry.grid(pady=5, column=3, row=8)
        self.historyEntry.grid(pady=5, column=3, row=10)
        self.currentdateEntry.grid(pady=5, column=3, row=11)
        self.dateTypeEntry.grid(pady=5, column=3, row=4)

        # Combobox widgets
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderType, width=62)
        self.bloodListBox = tkinter.ttk.Combobox(self.window, values=self.bloodListType, width=62)

        self.genderBox.grid(pady=5, column=3, row=5)
        self.bloodListBox.grid(pady=5, column=3, row=9)

        # Button widgets
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Close", command=self.backhome).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    def backhome(self):
        self.window.destroy()
        self.home = HomePage()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                         self.contactNumberEntry.get(), self.emailAddressEntry.get(), self.dateTypeEntry.get(), self.currentdateEntry.get())
        if (self.test == "DONE"):
            self.database.Insert(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                 self.dateTypeEntry.get(),self.genderBox.get(), self.addressEntry.get(),
                                 self.contactNumberEntry.get(), self.emailAddressEntry.get(), self.bloodListBox.get(),
                                 self.historyEntry.get(), self.currentdateEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
            self.window.destroy()
            self.home = HomePage()
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.firstnameEntry.delete(0, tkinter.END)
        self.lastnameEntry.delete(0, tkinter.END)
        self.dateTypeEntry.delete(0, tkinter.END)
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.contactNumberEntry.delete(0, tkinter.END)
        self.emailAddressEntry.delete(0, tkinter.END)
        self.bloodListBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.currentdateEntry.delete(0, tkinter.END)


class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data") 
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        bg_color = "Blue"
        fg_color = "white"

        # Initializing all the variables
        self.id = id

        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.contactNumber = tkinter.StringVar()
        self.emailAddress = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.currentdate = tkinter.StringVar()
        self.dateType = tkinter.StringVar()

        self.genderType = ["Male", "Female", "Transgender", "Other"]
        self.bloodListType = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient Id", font=("times new roman", 10, "bold"),
                      width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient First Name",
                      font=("times new roman", 10, "bold"), width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"), text="Date of Birth",
                      width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Gender", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Address", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Contact Number", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Email Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Blood Type", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Problem", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Date", width=25).grid(pady=5, column=1, row=11)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id)

        tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=3, row=2)
        tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=3, row=3)
        tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=3, row=4)
        tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=3, row=5)
        tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=3, row=6)
        tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=3, row=7)
        tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=3, row=8)
        tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=3, row=9)


        self.idEntry =text=self.searchResults[0][0]
        self.firstnameEntry =text=self.searchResults[0][1]
        self.lastnameEntry = text=self.searchResults[0][2]
        self.dateTypeEntry =text=self.searchResults[0][3]
        self.genderboxEntry = text=self.searchResults[0][4]
        self.addressEntry = text=self.searchResults[0][5]
        self.contactNumberEntry =text=self.searchResults[0][6]
        self.emailAddressEntry = text=self.searchResults[0][7]
        self.bloodListBox = text=self.searchResults[0][8]

        self.currentdateEntry = tkinter.Entry(self.window, width=25, textvariable=self.currentdate)
        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)

        
        self.historyEntry.grid(pady=5, column=3, row=10)
        self.currentdateEntry.grid(pady=5, column=3, row=11)
        
    
        # Button
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Update", command=self.Update).grid(pady=15, padx=5, column=1,
                                                                row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Close", command=self.backhome).grid(pady=15, padx=5, column=3,
                                                                       row=14)

        self.window.mainloop()
    def backhome(self):
        self.window.destroy()

    def Update(self):
        self.database = Database()
        self.database.Insert( self.idEntry, self.firstnameEntry, self.lastnameEntry, self.dateTypeEntry,  self.genderboxEntry, self.addressEntry, self.contactNumberEntry,
                             self.emailAddressEntry, self.bloodListBox, self.historyEntry.get(),
                             self.currentdateEntry.get())
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")
        self.window.destroy()
        self.home = HomePage()

    def Reset(self):
        self.historyEntry.delete(0, tkinter.END)
        self.currentdateEntry.delete(0, tkinter.END)


class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "id", "firstname", "lastname", "dateOfBirth", "gender", "address", "contactNumber", "emailAddress", "bloodType", "history",
        "currentdate")

        # Treeview column headings
        self.databaseView.heading("id", text="Patient ID")
        self.databaseView.heading("firstname", text="First Name")
        self.databaseView.heading("lastname", text="Last Name")
        self.databaseView.heading("dateOfBirth", text="Date of Birth")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("address", text="Home Address")
        self.databaseView.heading("contactNumber", text="Contact Number")
        self.databaseView.heading("emailAddress", text="Email Address")
        self.databaseView.heading("bloodType", text="Blood Type")
        self.databaseView.heading("history", text="History")
        self.databaseView.heading("currentdate", text="Date")

        # Treeview columns
        self.databaseView.column("id", width=100)
        self.databaseView.column("firstname", width=100)
        self.databaseView.column("lastname", width=100)
        self.databaseView.column("dateOfBirth", width=100)
        self.databaseView.column("gender", width=100)
        self.databaseView.column("address", width=200)
        self.databaseView.column("contactNumber", width=100)
        self.databaseView.column("emailAddress", width=200)
        self.databaseView.column("bloodType", width=100)
        self.databaseView.column("history", width=100)
        self.databaseView.column("currentdate", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.heading = "Please enter Patient ID to " + task

        # Labels
        tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tkinter.Label(window, text="Patient ID", width=10).grid(pady=5, row=2)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(pady=5, row=3)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
        elif (task == "Delete"):
            tkinter.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())

class DisplayWindow:
        def __init__(self):
            window = tkinter.Tk()
            window.wm_title("Dislpay data")

             # Initializing all the variables
            self.currentdate = tkinter.StringVar()
            self.firstname = tkinter.StringVar()
            self.lastname = tkinter.StringVar()
            self.heading = "Please enter Date of the Data Enter to Displays \n (Date Format: DD-MM-YYYY)"

            tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
            tkinter.Label(window, text="Date", width=10).grid(pady=5, row=2)

            self.currentdateEntry = tkinter.Entry(window, width=30, textvariable=self.currentdate)
            self.currentdateEntry.grid(pady=5, row=3)

            tkinter.Button(window, width=20, text="Display", command=self.displayy).grid(pady=15, padx=5, column=1, row=14)
            
        def displayy(self):
            self.database = Database()
            self.data = self.database.Display(self.currentdateEntry.get())
            self.databaseView = DatabaseView(self.data)

class Auth:

    def __inht__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS user_table (fullname text, dateofbirth text, gender text, contact text, Username text , Password text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()
    
    def Insertv(self, fullname, dateofbirth, gender, contact, Username, Password):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("INSERT INTO user_table VALUES (?, ?, ?, ?, ?, ?)",(
        fullname, dateofbirth, gender, contact, Username, Password    
        ))
        self.dbConnection.commit()

    def Displayv(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("SELECT * FROM user_table")
        records = self.dbCursor.fetchall()
        return records
    
    def deleteu(self, Username):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("DELETE FROM user_table WHERE Username = ?", (Username,))
        tkinter.messagebox.showinfo("Deleted data", "Successfully Deleted the User-Login data in the database")
        self.dbConnection.commit()
        

class DBView:
    def __init__(self, data):
        self.DBviewWindow = tkinter.Tk()
        self.DBviewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.DBviewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.DBview = tkinter.ttk.Treeview(self.DBviewWindow)
        self.DBview.grid(pady=5, column=1, row=2)
        self.DBview["show"] = "headings"
        self.DBview["columns"] = (
        "fullname", "dateofbirth", "gender", "contact", "Username", "Password")
        
        self.DBview.heading("fullname", text="NAME")
        self.DBview.heading("dateofbirth", text="DOB")
        self.DBview.heading("gender", text="GENDER")
        self.DBview.heading("contact", text="CONTACT")
        self.DBview.heading("Username", text="USERNAME")
        self.DBview.heading("Password", text="PASSWORD")

        self.DBview.column("fullname", width=100)
        self.DBview.column("dateofbirth", width=100)
        self.DBview.column("gender", width=100)
        self.DBview.column("contact", width=100)
        self.DBview.column("Username", width=100)
        self.DBview.column("Password", width=100)

        for record in data:
            self.DBview.insert('', 'end', values=(record))

        self.DBviewWindow.mainloop()
        
        
class uservalues:
    def Validate(self,dateofbirth, contact, password):
        if not(dateofbirth.count("-") == 2):
            return "Date Of Birth should be in the format DD-MM-YYYY"
        elif not(contact.isdigit() and (len(contact) == 10)):
            return "Contact number is invalid"
        elif not ((len(password)==8)):
            return "Password should have atleast 8 digits"
        else:
            return "ALLCLEAR"
        
        
class SigninWindow:
    def __init__(self):
        self.signinwindow = tkinter.Tk()
        self.signinwindow.wm_title("Sign IN")
        self.signinwindow.config(bg='grey')
        screen_width = self.signinwindow.winfo_screenwidth()
        screen_height = self.signinwindow.winfo_screenheight()
        self.signinwindow.geometry(f"{screen_width}x{screen_height}")
        self.signinwindow.columnconfigure(1, weight=2)
        self.signinwindow.columnconfigure(2, weight=2)
        self.signinwindow.columnconfigure(3, weight=2)
        self.signinwindow.columnconfigure(4, weight=1)
        bg_color = "deeppink"
        fg_color = "white"
        
        

        self.fullname = tkinter.StringVar()
        self.dateofbirth = tkinter.StringVar()
        self.contact = tkinter.StringVar()
        self.Username = tkinter.StringVar()
        self.Password = tkinter.StringVar()
        self.genderType = tkinter.StringVar()


        tkinter.Label(self.signinwindow, fg=fg_color, bg=bg_color, text="Enter Your Details", font=("times new roman",10,"bold"), width=65, height=2).grid(pady=20, column=2, row=0)

        tkinter.Label(self.signinwindow, fg=fg_color, bg=bg_color, text="Name", font=("times new roman",10,"bold"), width=65, height=2).grid(pady=5, column=1, row=1)
        tkinter.Label(self.signinwindow,  fg=fg_color, bg=bg_color, text="Date Of Birth", font=("times new roman",10,"bold"), width=65, height=2).grid(pady=5, column=1, row=2)
        tkinter.Label(self.signinwindow,  fg=fg_color, bg=bg_color, font=("Gender",10,"bold"), text="Gender", width=58, height=2).grid(pady=5, column=1, row=3)
        tkinter.Label(self.signinwindow, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Contact", width=65, height=2).grid(pady=5, column=1, row=4)
        tkinter.Label(self.signinwindow,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Username", width=65, height=2).grid(pady=5, column=1, row=5)
        tkinter.Label(self.signinwindow,  fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"),text="Password", width=65, height=2).grid(pady=5, column=1, row=6)
       

        self.fullnameEntry = tkinter.Entry(self.signinwindow, width=65,   textvariable=self.fullname)
        self.dateofbirthEntry = tkinter.Entry(self.signinwindow, width=65,  textvariable=self.dateofbirth)
        self.genderBox = tkinter.Entry(self.signinwindow, textvariable=self.genderType, width=65)
        self.contactEntry = tkinter.Entry(self.signinwindow, width=65,  textvariable=self.contact)
        self.UsernameEntry = tkinter.Entry(self.signinwindow, width=65,  textvariable=self.Username)
        self.PasswordEntry = tkinter.Entry(self.signinwindow, width=65,  textvariable=self.Password)


        self.fullnameEntry.grid(pady=5, column=3, row=1)
        self.dateofbirthEntry.grid(pady=5, column=3, row=2)
        self.genderBox.grid(pady=5, column=3, row=3)
        self.contactEntry.grid(pady=5, column=3, row=4)
        self.UsernameEntry.grid(pady=5, column=3, row=5)
        self.PasswordEntry.grid(pady=5, column=3, row=6)


        tkinter.Button(self.signinwindow, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Insert", command=self.SigninWindow).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        # tkinter.Button(self.signinwindow, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Reset", command=self.Display).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.signinwindow, width=10, fg=fg_color, bg=bg_color, font=("times new roman",10,"bold"), text="Close", command=self.backlogin).grid(pady=15, padx=5, column=3,
                                                                                              row=14)
        

        self.signinwindow.mainloop()
    
    def backlogin(self):
        self.signinwindow.destroy()
        self.window = LoginWindow()

    def SigninWindow(self):
        self.values = uservalues()
        self.database= Auth()
        self.test = self.values.Validate(self.dateofbirthEntry.get(), self.contactEntry.get(), self.PasswordEntry.get())
        if (self.test == "ALLCLEAR"):
            self.database.Insertv(self.fullnameEntry.get(), self.dateofbirthEntry.get(), self.genderType.get(), self.contactEntry.get(), self.UsernameEntry.get(), self.PasswordEntry.get())
            tkinter.messagebox.showinfo("Registered", "User Successfully Registered")
        else:
            self.valueErrorMessage =  self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)


class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Electronic Patient Record System")
        self.homePageWindow.columnconfigure(1, weight=1)
        self.homePageWindow.config(bg='grey')

        screen_width = self.homePageWindow.winfo_screenwidth()
        screen_height = self.homePageWindow.winfo_screenheight()
        self.homePageWindow.geometry(f"{screen_width}x{screen_height}")
        bg_color = "skyblue"
        fg_color = "black"
        lbl_color = 'GREEN'

        # background1_image = PhotoImage(file="F:\Visual Studio Code\Patient_Information_System\ground.png")
        # background1_label = tk.Label(image=background1_image)
        # background1_label.place(width=1400, height=750, x=0,y=0)

        tkinter.Label(self.homePageWindow, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Home Page", font=("times new roman",20,"bold"),height=2, width=40).grid(pady=60, column=1, row=1)

        tkinter.Button(self.homePageWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Insert", font=("times new roman",15,"bold"), command=self.Insert).grid(pady=15, column=1, row=2)
        tkinter.Button(self.homePageWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Update", font=("times new roman",15,"bold"), command=self.Update).grid(pady=15, column=1, row=3)
        tkinter.Button(self.homePageWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Search", font=("times new roman",15,"bold"), command=self.Search).grid(pady=15, column=1, row=4)
        tkinter.Button(self.homePageWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Delete", font=("times new roman",15,"bold"), command=self.Delete).grid(pady=15, column=1, row=5)
        tkinter.Button(self.homePageWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Display", font=("times new roman",15,"bold"), command=self.Display).grid(pady=15, column=1,
                                                                                                 row=6)
        tkinter.Button(self.homePageWindow, width=30, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Log-Out", font=("times new roman",15,"bold"), command=self.backlogin).grid(pady=15,
                                                                                                             column=1,
                                                                                                             row=7)

        self.homePageWindow.mainloop()



    def backlogin(self):
        self.homePageWindow.destroy()
        self.Loginwindow = LoginWindow()

    def Insert(self):
        self.homePageWindow.destroy()
        self.insertWindow = InsertWindow()

    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text="Enter the ID to update", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

        self.idEntry.grid(pady=10, row=2)

        # Button widgets
        tkinter.Button(self.updateIDWindow, width=20, text="Update", command=self.updateID).grid(pady=10, row=3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")


    # def Display(self):
    #     self.database = Database()
    #     self.data = self.database.Display()
    #     self.displayWindow = DatabaseView(self.data)

    def Display(self):
        self.displayallwindow = DisplayWindow()

class LoginWindow:

    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbcursor = self.dbConnection.cursor()
        self.loginwindow = tkinter.Tk()
        self.loginwindow.wm_title("Welcome User to EPR System")
        self.loginwindow.config(bg='grey')
        screen_width = self.loginwindow.winfo_screenwidth()
        screen_height = self.loginwindow.winfo_screenheight()
        self.loginwindow.geometry(f"{screen_width}x{screen_height}")
        self.loginwindow.columnconfigure(1, weight=30)
        self.loginwindow.columnconfigure(2, weight=1)
        self.loginwindow.columnconfigure(3, weight=30)
        fg_color = "black"
        bg_color = "skyblue"
        
        # img4 =Image.open(r"C:\Users\YASH\Downloads\img.jpg")
        # img4 =Image.resize(1530,1000)
        # self.photoimg4=ImageTk.PhototImage(img4)
        # bgimage=label(self.loginwindow, image=self.photoimg4)
        # bgimage.place(x=0,y=0,width=1500,height=1000)

        # background_image = PhotoImage(file="img1.png")
        # background_label = tk.Label(image=background_image)
        # background_label.place(width=1400, height=750, x=0,y=0)

        self.Username = tkinter.StringVar()
        self.Password= tkinter.StringVar()

        tkinter.Label(self.loginwindow, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Login to Continue", font=("times new roman",20,"bold"), width=40).grid(pady=50, column=2, row=1)
        tkinter.Button(self.loginwindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Login", font=("times new roman",15,"bold"), command=self.authen).grid(pady=10, column=2, row=8)
        tkinter.Button(self.loginwindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="New User ?  SignUp", font=("times new roman",15,"bold"), command=self.sign).grid(pady=10, column=2, row=9)
        tkinter.Button(self.loginwindow, width=30, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Exit", font=("times new roman",15,"bold"), command=self.loginwindow.destroy).grid(pady=10, column=2, row=10)


        tkinter.Label(self.loginwindow, relief=tkinter.GROOVE, text="Username:",font=("times new roman",20,"bold")).grid(row=4, column=2, pady=10)
        self.UsernameEntrylogin = tkinter.Entry(self.loginwindow, width=50, relief=tkinter.GROOVE,font=("times new roman",15,"bold"), textvariable=self.Username).grid(row=5, column=2, pady=10)
        tkinter.Label(self.loginwindow, relief=tkinter.GROOVE, text="Password:",font=("times new roman",20,"bold")).grid(row=6, column=2, pady=10)
        self.PasswordEntrylogin = tkinter.Entry(self.loginwindow, width=50, relief=tkinter.GROOVE,font=("times new roman",15,"bold"), show="*", textvariable=self.Password).grid(row=7, column=2, pady=10)

        self.loginwindow.mainloop()
        

    def authen(self):
        Username = self.Username.get()
        Password = self.Password.get()
        
        if Username and Password:
            self.connection = sqlite3.connect("Patientdb.db")
            self.cursor = self.connection.cursor()

            self.cursor.execute("SELECT * FROM user_table WHERE username=? AND password=?", (Username, Password))
            user = self.cursor.fetchone()

            self.connection.close()

            if user:
                tkinter.messagebox.showinfo("Login", "Login successful!")
                self.loginwindow.destroy()
                self.window = HomePage()
            elif Username == ("admin") and Password == ("admin"):
                self.loginwindow.destroy()
                self.window = adminsign() 
            else:
                tkinter.messagebox.showwarning("Error", "Invalid username or password.")      
        else:
            tkinter.messagebox.showwarning("Error", "Please enter both username and password.")

    def sign(self):
        self.loginwindow.destroy()
        self.window = SigninWindow()
  
class adminsign():
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbcursor = self.dbConnection.cursor()
        self.adminWindow = tkinter.Tk()
        self.adminWindow.wm_title("Welcome User to EPR System")
        self.adminWindow.config(bg='grey')
        screen_width = self.adminWindow.winfo_screenwidth()
        screen_height = self.adminWindow.winfo_screenheight()
        self.adminWindow.geometry(f"{screen_width}x{screen_height}")
        self.adminWindow.columnconfigure(1, weight=30)
        self.adminWindow.columnconfigure(2, weight=1)
        self.adminWindow.columnconfigure(3, weight=30)
        fg_color = "black"
        bg_color = "skyblue"
        tkinter.Label(self.adminWindow, relief=tkinter.GROOVE, text="ADMIN LOGIN",font=("times new roman",20,"bold")).grid(row=0, pady=20, column=2)
       
        tkinter.Button(self.adminWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Display User-Login Data", font=("times new roman",15,"bold"), command=self.Display).grid(pady=15,row = 2, column=2)
        tkinter.Button(self.adminWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Display Daily Data", font=("times new roman",15,"bold"), command=self.Display2).grid(pady=15,row = 3, column=2)
        tkinter.Button(self.adminWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Display Specific Patient Data", font=("times new roman",15,"bold"), command=self.Search).grid(pady=15,row = 4, column=2)
        tkinter.Button(self.adminWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Delete Patient Data", font=("times new roman",15,"bold"), command=self.Delete).grid(pady=15,row = 5, column=2)
        tkinter.Button(self.adminWindow, width=40, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Delete User_Login Data", font=("times new roman",15,"bold"), command=self.DeleteU).grid(pady=15,row = 6, column=2)
        tkinter.Button(self.adminWindow, width=24, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="LogOut", font=("times new roman",15,"bold"), command=self.back).grid(pady=15,row = 7, column=2)
        
        self.adminWindow.mainloop()

    def Display(self):
        self.database = Auth()
        self.data = self.database.Displayv()
        self.displayWindow = DBView(self.data)

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")

    def DeleteU(self):
        self.deleteWindow = DeleteuWindow()

    def Display2(self):
        self.displayallwindow = DisplayWindow()

    def back(self):
        self.adminWindow.destroy()
        self.window = LoginWindow()


class DeleteuWindow():
    def __init__(self):
        window = tkinter.Tk()
        window.wm_title("Delete User-Login data")

        # Initializing all the variables
        self.Username = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.heading = "Please enter Username to Delete" 

        # Labels
        tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tkinter.Label(window, text="Patient ID", width=10).grid(pady=5, row=2)

        # Entry widgets
        self.UsernameEntry = tkinter.Entry(window, width=5, textvariable=self.Username)
        self.UsernameEntry.grid(pady=5, row=3)

        
        tkinter.Button(window, width=20, text="Delete", command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Delete(self):
        self.database = Auth()
        self.database.deleteu(self.UsernameEntry.get())

homePage = LoginWindow()