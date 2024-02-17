import os
import pandas as pd
from bs4 import BeautifulSoup

WinWeight,TopFiveWeight,TopTenWeight,PoleWeight,LapWeight=.25,.16,.11,.06,.04
LedWeight,StartWeight,FinWeight,RAFWeight,LLFWeight=.09,.05,.12,.04,.08
NormMin,NormMax=70,100
DefaultDir=os.getcwd()

if not os.path.exists(os.path.join(DefaultDir,"Ratings")):
    os.makedirs(os.path.join(DefaultDir,"Ratings"))
if not os.path.exists(os.path.join(DefaultDir,"Season Files")):
    os.makedirs(os.path.join(DefaultDir,"Season Files"))

def MainMenu():
    while True:
        os.system('cls')
        print("Welcome to Tyler's Driver Rating Calculator")
        print("Python Version 2.0")
        print()
        print("With this tool, you can easily generate a text file containing a list of every driver and their rating.")
        print("For information on how to prepare a .html for use, please reference the readme.")
        print()
        print("To enter a .html file to calculate ratings with, type 'Calc'")
        print("To view a .html file, type 'View'")
        print("To edit calculation parameters, type 'Settings'")
        print("To view the changelog, type 'Log'")
        print("To quit, type 'Exit'")
        userinput=input(">").lower()
        if userinput=='exit':break
        elif userinput=='calc':EnterHTML()
        elif userinput=='view':ViewTable()
        elif userinput=='settings':Settings()
        elif userinput=='log':ChangeLog()

def EnterHTML():
    global DefaultDir
    os.system('cls')
    UserInput=input("Enter .html file to parse: ")
    try:
        if not UserInput.endswith(".html"):UserInput+=".html"
        FilePath=os.path.join(DefaultDir,"Season Files",UserInput)
        with open(UserInput,'r') as file:
            html_content=file.read()
        soup=BeautifulSoup(html_content,'html.parser')
        table=soup.find('table')
        headers=[header.text.strip() for header in table.find_all('th')]
        rows=[]
        for rows in table.find_all('tr')[1:]:
            rows.append([data.text.strip() for data in row.find_all('td')])
        DataFrame=pd.DataFrame(rows,columns=headers)
        
        NumericColumns=['Races','Win','T5','T10','Pole','Laps','Led','AvSt','AvFn','Raf','LLF']
        DataFrame[NumericColumns]=DataFrame[NumericColumns].apply(pd.to_numeric,errors='coerce')
        
        MaxValues=DataFrame.max()
        MinValues=DataFrame.min()
        MaxRace,MinRace=MaxValues['Races'],MinValues['Races']
        MaxWin,MinWin=MaxValues['Win'],MinWalues['Win']
        MaxTopFive,MinTopFive=MaxValues['T5'],MinWalues['T5']
        MaxTopTen,MinTopTen=MaxValues['T10'],MinWalues['T10']
        MaxPole,MinPole=MaxValues['Pole'],MinValues['Pole']
        MaxLap,MinLap=MaxValues['Laps'],MinValues['Laps']
        MaxLed,MinLed=MaxValues['Led'],MinValues['Led']
        MaxAvSt,MinAvSt=MaxValues['AvSt'],MinValues['AvSt']
        MaxAvFn,MinAvFn=MaxValues['AvFn'],MinValues['AvFn']
        MaxRAF,MinRAF=MaxValues['RAF'],MinValues['RAF']
        MaxLLF,MinLLF=MaxValues['LLF'],MinValues['LLF']
        try:
            DataFrame['RacePercentage']=(DataFrame['Races']/MaxRace)*100
            for stat in NumericColumns:
                if stat!='Races' and stat!='AvSt' and stat!='AvFn':
                    DataFrame[stat]=(DataFrame[stat]*DataFrame['RacePercentage'])/100
            DataFrame['Rating']=df.apply(CalculateRatings,axis=1)
            UserInput+=".txt"
            FilePath=os.path.join(DefaultDir,"Ratings",UserInput)
            with open(FilePath,'w') as file:
                for index, row in DataFrame.iterrows():
                    file.write(f"{row['Driver']}: {row['Rating']}\n")
        except Exception as e:
            print("Error:",e)
            input()
    except FileNotFoundError:
        print(f"Error: {UserInput} not found.")
        input()
    except Exception as e:
        print("Error:",e)
        input()

def CalculateRatings(row):
    global WinWeight,TopFiveWeight,TopTenWeight,PoleWeight,LapWeight,LedWeight,StartWeight,FinWeight,RAFWeight,LLFWeight,NormMin,NormMax

def ChangeLog():
    os.system('cls')
    print("v0.1 02/15/2024")
    print("-initial python build, port from basic to make a version i might eventually be willing to share")
    print("v1.0 02/16/2024")
    print("-now available as an executable")
    print("-fixed several errors during saving")
    print("-fixed incorrect file path when loading")
    print("-adjusted normalization minimum")
    print("v2.0 02/xx/2024")
    print("-rewrote from ground up")
    print("-much easier to use now")
    print("--enter html file with table containing season data")
    print("--program will take care of rest of the work for you")
    input()

if __name__=="__main__":
    MainMenu()
