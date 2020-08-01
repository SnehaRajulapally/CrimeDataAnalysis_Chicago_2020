#Name: Sneha Rajulapally
#CWID: A20457266
#Date: 07/27/2020
#Filename : GUI_finalproject.py
#Description: Python main file to run the GUI tkinter application

#Importing statements
import time

#Print programmer details and current Timestamp
print()
print("Programmed by Sneha Rajulapally")
print("Current Date and Time: " + time.strftime("%x") + " " + time.strftime("%X"))
print()

#importing statements
from tkinter import * 
from tkinter import messagebox as mbox
import sqlite3
from DB_finalproject import *
from Dataplots_finalproject import *
import tkinter as tk
import hashlib

#main Class
class main:
#Function for initialization(class constructor)
    def __init__(self,master):
    	# Master window for login screen
        self.master = master
        # Setting global variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Createing EntryWidgets
        self.entrywidgets()

#Function to validate login credentials
    def login(self):
        #Check if the username and password parameters are empty,throw error if they are empty
        if(self.username.get() ==" " or self.password.get() ==" "):
            print("Error: Invalid credentials!")
            mbox.showerror(title="Error Message", message = "Invalid Credentials!Re-enter.")
        else:
    	#Establish Connection to database
            try:
                conn = sqlite3.connect("finalproject.db")   #create a connection to SQLite db
                cursor = conn.cursor()
            except:                 #throw an error message of connection fails
                print("Error:Connection to database unsuccessful!")
        #Fetch data to check if the login credentials exists for the user
        # create hash password for security purposes
            hashed_password = hashlib.sha256(self.password.get().encode('utf-8')).hexdigest()
            cursor.execute("SELECT * FROM USERSDATA WHERE USERNAME = ? and PASSWRD = ?", (self.username.get(),hashed_password))
            res = cursor.fetchall()
            #if the data exists, display success message and take user to next screem
            if res:
                mbox.showinfo(title="Welcome Message", message = "You have logged in successfully!")
                print("User logged in successfully!")
                root.destroy()
            # call next screen after destroying previous screen
                print("User screen")
                userscreen()
            #if the user doesn't exist display error message and reset parameters
            else: 
                mbox.showerror(title="Error Message", message = "User not found. Please Re-enter!")
                print("Error: User not found. Please Re-enter!")
                self.username.set('') # existing users check
                self.password.set('')

#Function to create a new login account for signups
    def new_users(self):
        #Throw error if the input parameters are empty
        if( self.n_username.get() ==" " or self.n_password.get() ==" "):
            print("Error: Invalid credentials!")
            mbox.showerror(title="Error Message", message = "Invalid Credentials!Re-enter.")
        else:
    	#Establish Connection to database
            try:
                conn = sqlite3.connect("finalproject.db")   #create a connection to SQLite db
                cursor = conn.cursor()
            except:                 #throw an error message of connection fails
                print("Error:Connection to database unsuccessful!")

            #Check if user is already in the system
            try:
                query= ("SELECT * FROM USERSDATA WHERE USERNAME = ?")
                cursor.execute(query, [(self.n_username.get())])
                res = cursor.fetchall()
                #user data exists, throw error
                if res:
                    print("Error: User already exists! Please Re-enter.")
                    mbox.showerror(title="Error Message", message =  'User already exists! Please Re-enter.')
                    self.username.set('') # existing users check
                    self.password.set('')
                    self.n_username.set('') # new users info
                    self.n_password.set('')
                else:
                    try:
                    #Else Create a  New Account
                        file = open('usersdata.csv', 'a')
                        fields = [self.n_username.get(),self.n_password.get()]
                        string = ','.join(fields)
                        file.write("\n" + string) #writing new login details to CSV file
                        file.close()
                        newuserdb(self.n_username.get(),self.n_password.get()) #insert new credentials to database
                        self.n_username.set('') # new users info
                        self.n_password.set('')
                        mbox.showinfo(title="Success Message", message = 'Account has been successfully created! Goback to login screen.')
                        print('Account has been successfully created!')
                    except:
                        print("Error: Account creation unsuccessful!")
            except:
                print("Error: Account creation unsuccessful!")
        
#Frame Packing Methods
    def log(self):
        self.username.set('') # existing users check
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Enter username and password to logIn. SignUp if you are a new user.' 
        self.logf.pack()
        print("This is login screen")
        root.title("Login Screen")

    def cr(self):
        self.n_username.set('') # new users info
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Enter your details to create an account.'
        self.crf.pack()
        print("This is SignUp screen")
        root.title("SignUp Screen")

#function to exit out of application if users selects the button
    def exit(self):
        if (mbox.askokcancel(title="Exit", message="Do you really want to quit?") == 1) :
            print("Exiting Application!")
            root.destroy()

#clearing parameters if user clicks on clear button
    def clear(self):
        self.username.set('') 
        self.password.set('')
        
#Draw Widgets for login screen
    def entrywidgets(self):

        #Login screen
        self.head = Label(self.master,text = 'Please enter username and password to logIn. \n SignUp if you are a new user.',font = ('',10),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =50,pady = 50)
        Label(self.logf,text = 'Username*: ',font = ('',15)).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',10)).grid(row=0,column=1)
        Label(self.logf,text = 'Password*: ',font = ('',15)).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',10),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' LogIn ',bd = 5 ,font = ('',10),command=self.login).grid()
        Button(self.logf,text = ' SignUp ',bd = 5 ,font = ('',10),command=self.cr).grid(row=2,column=1)
        Button(self.logf,text = ' Clear ',bd = 5, font = ('',10),command=self.clear).grid()
        Button(self.logf,text = ' Exit ',bd = 5, font = ('',10),command=self.exit).grid(row=3,column=1)
        self.logf.pack() # pack initial elements to frame
        
        #SignUp screen
        self.crf = Frame(self.master,padx =50,pady = 50)
        Label(self.crf,text = 'Username*: ',font = ('',15)).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',10)).grid(row=0,column=1)
        Label(self.crf,text = 'Password*: ',font = ('',15)).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',10),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 5 ,font = ('',10),command=self.new_users).grid()
        Button(self.crf,text = ' Go to LogIn ',bd = 5 ,font = ('',10),command=self.log).grid(row=2,column=1)

#function to center the pack based on application size
def center():
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight() 

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

#function to take user to next screen after successful login to view data analysis
def userscreen():
    # Creating master Tkinter window 
    master = Tk() 
    master.geometry("500x350") 
    master.title("User Screen")
    head = Label(master,text = 'Please select from below options to view data:\n\n',font = ('',15),pady = 10)
    head.pack()
  
    # Tkinter string variable 
    # able to store any string value 
    v = StringVar(master)
    #function to get user's radio button selection
    def showsel():
        global sel      
        print("Your selection is " + v.get())
        sel = v.get()
        return sel

    #function to display data based on user selection
    def displaydata():
        if ( sel == '1'):
            allcrimes()
        elif( sel == '2'):
            top5crimes()
        elif( sel == '3'):
            monthlyfreq()
        elif( sel == '4'):
            arrests()
        elif( sel == '5'):
            districts()
        else:
            print("Error in displaying data!")
            mbox.showerror(title="Error Message", message = "Invalid Selection!Re-enter.")

    # Dictionary to create multiple buttons 
    values = {"All crimes in Chicago in 2020 till date (Horizontal Bar Chart)" : "1", 
          "Top 5 crimes in Chicago in 2020 till date (Bar Chart)" : "2", 
          "Monthly frequency of top 5 crimes (Line chart)" : "3", 
          "Ratio of Arrest to Non Arrest cases (Pie chart)" : "4",
          "Districtwise distribution of top crimes (Catplot-bar Chart)" :"5" } 
  
# Loop is used to create multiple Radiobuttons 
# rather than creating each button separately 
    for (text, value) in values.items(): 
        Radiobutton(master, text = text, variable = v, command=showsel, value = value, indicator = 0, background = "light blue",).pack(fill = X, ipady = 5) 
    
    #function to close the application
    def close():
        if (mbox.askokcancel(title="Close", message="Do you really want to close the application?") == 1) :
            print("Closing Application!")
            master.destroy()

    Button(master,text = "View Data Analysis",bd = 5 ,font = ('',10),command=displaydata).pack()
    Button(master,text = "Close",bd = 5 ,font = ('',10),command=close).pack()
    mainloop() 

#create window and application object
root = Tk()
root.title("Login Page") 
print("Application loaded!")
center()
createTabledb() #create table
inserttodb()  #insert records into table
main(root) # instantiate class
root.mainloop()
 
