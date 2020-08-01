#Name: Sneha Rajulapally
#CWID: A20457266
#Date: 07/27/2020
#Filename :Dataplots_finalproject.py
#Description: Python file to get data and plots based on user selection

#importing parameters
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

#Function to read data from the csv file
def getdata():
    global df
    #reading the chicago crime data set for year 2020 till date
    df = pd.read_csv('Crimes_-_2020.csv')
    print("Chicago crime Data for year 2020 has been successfully fetched from CSV file.")
    df.Date = pd.to_datetime(df.Date,format = '%m/%d/%Y %I:%M:%S %p')
    df.index = pd.DatetimeIndex(df.Date)
    df['time_hour']= df['Date'].apply(lambda x: x.hour) #getting time data
    df['month']=df['Date'].apply(lambda x: x.month) #getting month data

#function to display all the crimes with count 
def allcrimes():
    getdata()  #read dataset
    #data of number of crimes in chicago from 2020 to tilldate
    crimetypes = df['Primary Type'].unique()
    print("Total number of crime types in chicago in year 2020 to till date: ",len(crimetypes))
    print("Crimetypes:\n", crimetypes)
    print()
    #getting all the crimes in chicago in year 2020 to till date
    df.groupby(df['Primary Type']).size().sort_values(ascending = True).head(31).plot(kind ='barh',color = ['g', 'y', 'c', 'm', 'r'],figsize=(15,8))
    #figure = plt.figure(figsize=(10,10))
    plt.xlabel('Crime count')   #x axis label name
    plt.ylabel("Crime type")    #y axis label name
    plt.xticks(color="grey")    #x axis parameters setting color
    plt.yticks(color="grey")    #x axis parameters setting color
    plt.title("All crimes in Chicago(2020-tilldate)",fontsize=25)
    plt.subplots_adjust(left=0.22, right=0.99,top=0.85,bottom=0.1) 
    print("Displaying data of all crimes commited in Chicago in 2020 till date using horizontal bar graph.\n")
    plt.show()

#function to display top 5 crimes based on the number of crimes commited
def top5crimes():
    getdata()
    #getting data of top 5 crimes in chicago in year 2020 to till date
    topcrimes = df['Primary Type'].value_counts().sort_values(ascending=False).head()
    tp = df.groupby('Primary Type', as_index=False).agg({"ID": "count"})
    tp = tp.sort_values(by=['ID'], ascending=False).head()
    tp = tp.sort_values(by='ID', ascending=True)
    print("Top 5 crimes and counts: ")
    print(tp) #displaying as table
    print()
    colors = ['g', 'y', 'c', 'm', 'r']   #setting different colours
    tp.plot.bar(x='Primary Type',y='ID',color = colors,label ='crime count')
    plt.title("Top 5 crimes in Chicago in 2020 to till date\n",fontsize=15)
    plt.xlabel("Crime count")
    plt.ylabel("Crime type")
    plt.xticks(color="grey")
    plt.yticks(color="grey")
    plt.xticks(rotation=360)   #x axis parameters display
    print("Displaying data of top5 crimes commited in Chicago in 2020 till date using bar graph.\n")
    plt.show()

#function to display ratio of arrest vs non arrests
def arrests():
    getdata()
    #get ratio of arrest count to non-arrest count
    ar = df[['Arrest']]  # get a series from data frame
    arrests = ar.groupby('Arrest').size().sort_values(ascending=True).rename('counts')
    print(arrests.values[0], " were Arrested  and ", arrests.values[1], " weren't arrested")
    print("Arrests and Non-arrests count:")
    print(arrests)
    explode=[0,0.10]
    plt.figure(figsize=(6,5))
    lables=["Arrested","Not Arrested"]
    plt.pie(arrests,labels=lables, autopct="%.1f%%", explode=explode, colors=["r","g"],textprops={'fontsize': 15})
    plt.title("Ratio of Arrests and Non-Arrests",fontsize=20)
    print("Displaying data of ratio of arrests vs non arrests to the crimes commited in Chicago in 2020 till date using pie graph.\n")
    plt.show()

#function to display districtwise distribution of top crimes
def districts():
    getdata()
    #get data of district wise top crimes
    districtcrimes = df.groupby(['District', 'Primary Type']).size().reset_index(name='count').groupby('District').apply(lambda x: x.sort_values('count',ascending=False).head(3))
    print(districtcrimes)
    #Creating multiple plots
    data =sns.catplot("Primary Type",y='count', col="District", col_wrap=6, data=districtcrimes, kind='bar',height=3)
    for x in data.axes:
        plt.setp(x.get_xticklabels(), rotation=90)
    plt.tight_layout()
    print("Displaying data of districtwise distribution of top crimes commited in Chicago in 2020 till date using catplot bar graph.\n")
    #plt.title("Districtwise distribution of crimes in Chicago 2020 till date")
    plt.subplots_adjust(hspace=0.5)
    plt.show()

#function to get the monthly occuring frequencies of top5 crimes
def monthlyfreq():
    getdata()
    def month(x):
        return x.strftime("%B")
    df['Month']= df['Date'].apply(month)
    #getting month from date field
    #Monthly data of most occuring crimes in Chicago in 2020 to till date
    theft ={} 
    battery= {}
    criminaldamage = {}
    assault = {}
    deceptivepractice = {}

    months = df["Month"].unique()
    for month in months :
        theft[month]=0
        battery[month]=0
        criminaldamage[month]=0
        assault[month]=0
        deceptivepractice[month]=0

    for element in df[df["Primary Type"]=="BATTERY"]["Month"]:
        if element in battery.keys():
            battery[element] += 1

    for element in df[df["Primary Type"]=="THEFT"]["Month"]:
        if element in theft.keys():
            theft[element] += 1
        
    for element in df[df["Primary Type"]=="CRIMINAL DAMAGE"]["Month"]:
        if element in criminaldamage.keys():
            criminaldamage[element] += 1
        
    for element in df[df["Primary Type"]=="ASSAULT"]["Month"]:
        if element in assault.keys():
            assault[element] += 1
        
    for element in df[df["Primary Type"]=="DECEPTIVE PRACTICE"]["Month"]:
        if element in deceptivepractice.keys():
            deceptivepractice[element] += 1

    #preparing data for plotting
    months=['January','February','March','April','May','June','July']
    theft_l= [(i,theft[i]) for i in months]
    battery_l = [(i,battery[i]) for i in months]
    criminaldamage_l = [(i,criminaldamage[i]) for i in months]
    assault_l= [(i,assault[i]) for i in months]
    deceptivepractice_l = [(i,deceptivepractice[i]) for i in months]

    # Plotting the graphs
    fig,p = plt.subplots(figsize=(7,5))
    plt.subplots_adjust(bottom=0.20)

    # Setting the ticks only on the bottom and the left of the graph
    p.get_xaxis().tick_bottom()    
    p.get_yaxis().tick_left()   

    plt.xticks(color="grey")
    plt.yticks(color="grey")

    x = [z[0] for z in battery_l]
    y = [z[1] for z in battery_l]
    p.plot(x,y, color="r")
    p.lines[0].set_linestyle("-")

    x = [z[0] for z in theft_l]
    y = [z[1] for z in theft_l]
    p.plot(x,y, color="m")
    p.lines[1].set_linestyle("-")

    x = [z[0] for z in criminaldamage_l]
    y = [z[1] for z in criminaldamage_l]
    p.plot(x,y, color="c")
    p.lines[2].set_linestyle("-")

    x = [z[0] for z in assault_l]
    y = [z[1] for z in assault_l]
    p.plot(x,y, color="y")
    p.lines[3].set_linestyle("-")

    x = [z[0] for z in deceptivepractice_l]
    y = [z[1] for z in deceptivepractice_l]
    p.plot(x,y, color="g")
    p.lines[4].set_linestyle("-")


    for tick in p.get_xticklabels():
        tick.set_rotation(90)

    
    plt.text(5,4000,"Theft",color="r")
    plt.text(5,3000,"Battery",color="m")
    plt.text(5,2200,"CriminalDamage",color="c")
    plt.text(5,1700,"Assault",color="y")
    plt.text(5,600,"DeceptivePractice",color="g")

    p.set_title("Monthly occurance of top 5 crimes\n",fontsize=15)
    p.set_xlabel("Month")
    p.set_ylabel("Crime count")
    print("Displaying data of monthly occuring frequency of top5 crimes commited in Chicago in 2020 till date using line graph.\n")
    
    plt.show()
