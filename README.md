# CrimeDataAnalysis_Chicago_2020
Python GUI Application to view the Crime Data Analysis in Chicago in year 2020
1.	Abstract

In this project we are going to conduct crime analysis in city of Chicago starting in year 2020 to till date. The city’s overall crime rate is substantially higher than the US average crime rate. Keeping this in mind, we have fetched dataset to analyze the trend in latest crime events that are occurring in the city to understand the crime patterns.

2.	Introduction

Crime has been a prevalent anti-social trait in human society. Surging crime rates have been major problem. In order to record the crime in Chicago, the Chicago police department developed a tool to assist city residents in combating crime and to maintain transparency. Understanding crime patterns and criminal behaviors would largely be helpful for police force and for public. We are using the dataset provided by Chicago police department that reflects the reported incidents of crime. Data is extracted from Citizen Law Enforcement Analysis and Reporting System. We are using some data science technologies with combination of python libraries to get the desired results.

3.	Project Overview

  1.	Focus
      
 	Crimes of Chicago Dataset has been extracted from the below URL and filtered out to get data of    2020 to till date and converted into CSV file.
                 https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data

  2.	Scope
  
•	GUI login for user to login to the application
•	User name and password are validated using SQLite3 database
•	If new user, allowing to signup and create new account and update SQLite3 database
•	After successful login, user to select from the radio button options to view the data/graph
•	Close and exit options to logout or close the application

  3.	Files

•	GUI_finaproject.py -> runs as main file to open the application
•	DB_finalproject.py -> Load and user credential validations using SQLite3 Database
•	Dataplots_finalproject.py -> get the data and display the plots, charts, graphs based on user selection
•	Jupyter_finalproject.py ->works same as above
•	Userdsdata.csv -> SQLite3 DB will validate login credentials using this file
•	Crimes_-_2020.csv -> read the data from the csv file and display the results based on user selection in GUI.
•	Finalproject.db -> DB connection is created

  4.	 Libraries

•	Tkinter
•	Sqlite3
•	Hashlib
•	Pandas
•	Matplotlib
•	Numpy
•	Seaborn
•	Datetime
•	Csv

4.	Functionalities
                 
1.	Login Screen
  1.	SQLite3 DB
    a.	Finalproject.db is created with USERSDATA table.
    USERSDATA table is populated with records in usersdata.csv file
    Passwords are hashed in DB table.
    User Credentials:

    Username : admin	
    Password: admin

    Username: sneha
    Password: test
    
  2.	GUI
    b.	Run GUI_finalproject.py file to load the application.
    
  3.	User credential validations
    c.	Enter Invalid credentials that are not present in CSV file or DB table.
        •	Message box with error appears, saying user not found. Please re-enter.
    d.	When correct credentials are entered, information with message box appears that you have successfully logged in.
    
 2.	SignUp Screen
  1.	GUI
    a.	This is signup screen. 
       •	Create button allows to create new account after validation.
       •	Go to login button takes back to login screen
    b.	Throw an error when you try to create existing user.
        •	Message box appears that the user already exists.
     c.	Throw a success message, when you add new users
        •	Message box appears that the account has been creates successfully.
                                  
 2.	SQLite3 DB
 a.	SQLite 3 DB has been updates with new record and CSV file has been updated.

3.	 Exit Button
a.	When exit button is clicked, message box appears if you want to quit application.

4.	Clear Button
a.	When clear button is clicked, the input texts will be cleared.

  5.	User Screen
    a.	After successful login, users screen is appeared.
    •	View data analysis button is clicked after selecting any button from the 5 choices to view data.
    •	Close button, exists you from the application

    1.	Radio Button 1: All crimes in Chicago in 2020 till date (Horizontal Bar Chart)
    2.	Radio Button 2: Top 5 crimes in Chicago in 2020 till date (Bar Chart)
    3.	Radio Button 3: Monthly frequency of top 5 crimes (Line Chart)
    4.	Radio Button 4: Ratio of Arrest to Non-Arrest cases (Pie Chart)
    5.	Radio Button 5: District wise distribution of top crimes (Catplot-bar chart)

5.	Extra Credits
  1.	Intuitive charting: Side by side graphical depiction
  2.	Stats on Mean, Standard deviation, variances, counts, averages, correlations etc
  3.	SQLite3 DB
  4.	Jupyter note book
                    
6.	Future Work
  •	Perform predictive analysis on crime events.
  •	Gather Crime vs Time frequency
  •	Yearly increase in crimes with large dataset file
  
7.	Conclusion

Through the analysis of crime data, we were able to find out a few answers regarding the crimes in Chicago. Few of the answers include, most committed crimes in Chicago in 2020 and found that no arrests were made in 83% of the crimes. This project has a great deal of scope and with future work, predictive models can be built.
