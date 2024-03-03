import os
import json
import random
import pandas as pd
from bs4 import BeautifulSoup

WinWeightNASCAR,TopFiveWeightNASCAR,TopTenWeightNASCAR,PoleWeightNASCAR,LapWeightNASCAR=.25,.16,.11,.06,.04
LedWeightNASCAR,StartWeightNASCAR,FinWeightNASCAR,RAFWeightNASCAR,LLFWeightNASCAR=.09,.05,.12,.04,.08
WinWeightTraditional,PodiumWeightTraditional,PoleWeightTraditional,LapWeightTraditional,LedWeightTraditional=.3,.18,.05,.08,.06
StartWeightTraditional,FinWeightTraditional,RAFWeightTraditional,LLFWeightTraditional=.08,.1,.05,.1
NormMin,NormMax=70,100
DefaultDir=os.getcwd()

if not os.path.exists(os.path.join(DefaultDir,"Ratings")):
    os.makedirs(os.path.join(DefaultDir,"Ratings"))
if not os.path.exists(os.path.join(DefaultDir,"Season Files")):
    os.makedirs(os.path.join(DefaultDir,"Season Files"))
if not os.path.exists(os.path.join(DefaultDir,"Edited Rosters")):
    os.makedirs(os.path.join(DefaultDir,"Edited Rosters"))
if not os.path.exists(os.path.join(DefaultDir,"iRacing Rosters")):
    os.makedirs(os.path.join(DefaultDir,"iRacing Rosters"))

def MainMenu():
    while True:
        os.system('cls')
        print("Welcome to Tyler's Driver Rating Calculator")
        print("Python Version 2.4.0")
        print("\nWith this tool, you can easily generate driver ratings and append them to AI rosters.")
        print("For information on how to prepare a .html file for use, please reference the readme.\n")
        print("NASCAR-Style Standings Weights:")
        print(f"Win weight: {int(WinWeightNASCAR*100)}% Top five weight: {int(TopFiveWeightNASCAR*100)}% Top ten weight: {int(TopTenWeightNASCAR*100)}% Pole weight: {int(PoleWeightNASCAR*100)}% Laps ran weight: {int(LapWeightNASCAR*100)}%")
        print(f"Laps led weight: {int(LedWeightNASCAR*100)}% Average start weight: {int(StartWeightNASCAR*100)}% Average finish weight: {int(FinWeightNASCAR*100)}% RAF weight: {int(RAFWeightNASCAR*100)}% LLF weight: {int(LLFWeightNASCAR*100)}%")
        print("\nTraditional Motorsports Standings Weights:")
        print(f"Win weight: {int(WinWeightTraditional*100)}% Podium weight: {int(PodiumWeightTraditional*100)}% Pole weight: {int(PoleWeightTraditional*100)}% Laps ran weight: {int(LapWeightTraditional*100)}%")
        print(f"Laps led weight: {int(LedWeightTraditional*100)}% Average start weight: {int(StartWeightTraditional*100)}% Average finish weight: {int(FinWeightTraditional*100)}% RAF weight: {int(RAFWeightTraditional*100)}% LLF weight: {int(LLFWeightTraditional*100)}%")
        print(f"\nNormalization minimum: {int(NormMin)}% Normalization maximum: {int(NormMax)}%")
        print("\nTo enter a .html file to calculate ratings with, type 'Calc'")
        print("To append an AI roster, type 'Append'")
        print("To view a .html file, type 'View'")
        print("To quit, type 'Exit'\n")
        UserInput=input(">").lower()
        if UserInput=='exit':break
        elif UserInput=='calc':EnterHTML()
        elif UserInput=='view':ViewTable()
        elif UserInput=='append':Append()

def EnterHTML():
    global DefaultDir
    os.system('cls')
    UserInput=input("Enter .html file to parse: ")
    try:
        if not UserInput.endswith(".html"):
            UserInput+=".html"
        FilePath=os.path.join(DefaultDir,"Season Files",UserInput)
        with open(FilePath,'r') as file:
            html_content = file.read()
        print("Reading .html file...")
        soup=BeautifulSoup(html_content,'html.parser')
        table=soup.find('table')
        headers=[header.text.strip() for header in table.find_all('th')]
        rows=[]
        for row in table.find_all('tr')[1:]:
            rows.append([data.text.strip() for data in row.find_all('td')])
        DataFrame=pd.DataFrame(rows,columns=headers)
        if 'Podium' in headers:
            NumericColumns=['Races','Win','Podium','Pole','Laps','Led','AvSt','AvFn','Raf','LLF']
        else:
            NumericColumns=['Races','Win','T5','T10','Pole','Laps','Led','AvSt','AvFn','Raf','LLF']
        DataFrame[NumericColumns]=DataFrame[NumericColumns].apply(pd.to_numeric,errors='coerce')
        MaxValues=DataFrame.max()
        MinValues=DataFrame.min()
        MaxRace,MinRace=MaxValues['Races'],MinValues['Races']
        MaxWin,MinWin=MaxValues['Win'],MinValues['Win']
        if 'Podium' in headers:
            MaxPode,MinPode=MaxValues['Podium'],MinValues['Podium']
        else:
            MaxTopFive,MinTopFive=MaxValues['T5'],MinValues['T5']
            MaxTopTen,MinTopTen=MaxValues['T10'],MinValues['T10']
        MaxPole,MinPole=MaxValues['Pole'],MinValues['Pole']
        MaxLap,MinLap=MaxValues['Laps'],MinValues['Laps']
        MaxLed,MinLed=MaxValues['Led'],MinValues['Led']
        MaxAvSt,MinAvSt=MaxValues['AvSt'],MinValues['AvSt']
        MaxAvFn,MinAvFn=MaxValues['AvFn'],MinValues['AvFn']
        MaxRAF,MinRAF=MaxValues['Raf'],MinValues['Raf']
        MaxLLF,MinLLF=MaxValues['LLF'],MinValues['LLF']
        try:
            print("Beginning calculations...")
            DataFrame.loc[:,'RacePercentage']=(DataFrame['Races']/MaxRace)*100
            for stat in NumericColumns:
                if stat!='Races' and stat!='AvSt' and stat!='AvFn':
                    DataFrame.loc[:,stat]=(DataFrame[stat]/DataFrame['RacePercentage']*100).astype(int)
            if 'Podium' in headers:
                DataFrame['Rating']=DataFrame.apply(lambda row:CalculateRatingsTraditional(row,MinWin,MinPode,MinPole,MinLap,MinLed,MinAvSt,MinAvFn,MinRAF,MinLLF,MaxWin,MaxPode,MaxPole,MaxLap,MaxLed,MaxAvSt,MaxAvFn,MaxRAF,MaxLLF),axis=1)
            else:
                DataFrame['Rating']=DataFrame.apply(lambda row:CalculateRatingsNASCAR(row,MinWin,MinTopFive,MinTopTen,MinPole,MinLap,MinLed,MinAvSt,MinAvFn,MinRAF,MinLLF,MaxWin,MaxTopFive,MaxTopTen,MaxPole,MaxLap,MaxLed,MaxAvSt,MaxAvFn,MaxRAF,MaxLLF),axis=1)
            UserInput=UserInput[:-5]
            UserInput+=".txt"
            FilePath=os.path.join(DefaultDir,"Ratings",UserInput)
            print("Writing to text file...")
            with open(FilePath,'w') as file:
                for index,row in DataFrame.iterrows():
                    file.write(f"{row['Driver']}: {int(row['Rating'])}\n")
            print("Calculations and export finished.")
            input()
        except Exception as e:
            print("Error:",e)
            input()
    except FileNotFoundError:
        print(f"Error: {UserInput} not found.")
        input()
    except Exception as e:
        print("Error:",e)
        input()

def CalculateRatingsNASCAR(row,MinWin,MinTopFive,MinTopTen,MinPole,MinLap,MinLed,MinAvSt,MinAvFn,MinRAF,MinLLF,MaxWin,MaxTopFive,MaxTopTen,MaxPole,MaxLap,MaxLed,MaxAvSt,MaxAvFn,MaxRAF,MaxLLF):
    global WinWeightNASCAR,TopFiveWeightNASCAR,TopTenWeightNASCAR,PoleWeightNASCAR,LapWeightNASCAR,LedWeightNASCAR,StartWeightNASCAR,FinWeightNASCAR,RAFWeightNASCAR,LLFWeightNASCAR,NormMin,NormMax
    MaxValues=row
    MinValues=row
    RateWin=(((row['Win']-MinWin)/(MaxWin-MinWin))*100)*WinWeightNASCAR
    RateTopFive=(((row['T5']-MinTopFive)/(MaxTopFive-MinTopFive))*100)*TopFiveWeightNASCAR
    RateTopTen=(((row['T10']-MinTopTen)/(MaxTopTen-MinTopTen))*100)*TopTenWeightNASCAR
    RatePole=(((row['Pole']-MinPole)/(MaxPole-MinPole))*100)*PoleWeightNASCAR
    RateLap=(((row['Laps']-MinLap)/(MaxLap-MinLap))*100)*LapWeightNASCAR
    RateLed=(((row['Led']-MinLed)/(MaxLed-MinLed))*100)*LedWeightNASCAR
    RateStart=(((row['AvSt']-MaxAvSt)/(MinAvSt-MaxAvSt))*100)*StartWeightNASCAR
    RateFin=(((row['AvFn']-MaxAvFn)/(MinAvFn-MaxAvFn))*100)*FinWeightNASCAR
    RateRAF=(((row['Raf']-MinRAF)/(MaxRAF-MinRAF))*100)*RAFWeightNASCAR
    RateLLF=(((row['LLF']-MinLLF)/(MaxLLF-MinLLF))*100)*LLFWeightNASCAR
    Rating=round(NormMin+(((RateWin+RateTopFive+RateTopTen+RatePole+RateLap+RateLed+RateStart+RateFin+RateRAF+RateLLF)*(NormMax-NormMin))/100))
    if Rating>NormMax:Rating=NormMax
    return Rating

def CalculateRatingsTraditional(row,MinWin,MinPode,MinPole,MinLap,MinLed,MinAvSt,MinAvFn,MinRAF,MinLLF,MaxWin,MaxPode,MaxPole,MaxLap,MaxLed,MaxAvSt,MaxAvFn,MaxRAF,MaxLLF):
    global WinWeightTraditional,PodeWeightTraditional,PoleWeightTraditional,LapWeightTraditional,LedWeightTraditional,StartWeightTraditional,FinWeightTraditional,RAFWeightTraditional,LLFWeightTraditional,NormMin,NormMax
    MaxValues=row
    MinValues=row
    RateWin=(((row['Win']-MinWin)/(MaxWin-MinWin))*100)*WinWeightTraditional
    RatePode=(((row['Podium']-MinPode)/(MaxPode-MinPode))*100)*PodiumWeightTraditional
    RatePole=(((row['Pole']-MinPole)/(MaxPole-MinPole))*100)*PoleWeightTraditional
    RateLap=(((row['Laps']-MinLap)/(MaxLap-MinLap))*100)*LapWeightTraditional
    RateLed=(((row['Led']-MinLed)/(MaxLed-MinLed))*100)*LedWeightTraditional
    RateStart=(((row['AvSt']-MaxAvSt)/(MinAvSt-MaxAvSt))*100)*StartWeightTraditional
    RateFin=(((row['AvFn']-MaxAvFn)/(MinAvFn-MaxAvFn))*100)*FinWeightTraditional
    RateRAF=(((row['Raf']-MinRAF)/(MaxRAF-MinRAF))*100)*RAFWeightTraditional
    RateLLF=(((row['LLF']-MinLLF)/(MaxLLF-MinLLF))*100)*LLFWeightTraditional
    Rating=round(NormMin+(((RateWin+RatePode+RatePole+RateLap+RateLed+RateStart+RateFin+RateRAF+RateLLF)*(NormMax-NormMin))/100))
    if Rating>NormMax:Rating=NormMax
    return Rating

def ViewTable():
    global DefaultDir
    os.system('cls')
    UserInput=input("Enter .html file to view: ")
    try:
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        if not UserInput.endswith(".html"):UserInput+=".html"
        FilePath=os.path.join(DefaultDir,"Season Files",UserInput)
        with open(FilePath,'r') as file:
            html_content=file.read()
        soup=BeautifulSoup(html_content,'html.parser')
        table=soup.find('table')
        headers=[header.text.strip() for header in table.find_all('th')]
        rows=[]
        for row in table.find_all('tr')[1:]:
            rows.append([data.text.strip() for data in row.find_all('td')])
        DataFrame=pd.DataFrame(rows,columns=headers)
        print(DataFrame)
        input()
    except FileNotFoundError:
        print(f"Error: {UserInput} not found.")
        input()
    except Exception as e:
        print("Error:",e)
        input()

def Append():
    global DefaultDir
    os.system('cls')
    UserInput=input("Enter iRacing roster name to edit: ")
    if not UserInput.endswith(".json"):
        UserInput+=".json"
    JSONName=UserInput
    FilePath=os.path.join(DefaultDir,"iRacing Rosters",UserInput)
    try:
        with open(FilePath,'r') as file:
            Data=json.load(file)
    except Exception as e:
        print("Error loading JSON file:",e)
        input()
        return
    DriverRatings={}
    UnmatchedDrivers=[]
    UserInput=input("Enter raing file to use: ")
    if not UserInput.endswith(".txt"):
        UserInput+=".txt"
    FilePath=os.path.join(DefaultDir,"Ratings",UserInput)
    with open(FilePath,'r') as file:
        for line in file:
            parts=line.strip().split(': ')
            if len(parts)==2:
                DriverName=parts[0].replace(',', '').replace('.', '').strip()
                DriverRatings[DriverName]=int(parts[1])
            else:
                print("Invalid line format:",line)
                input()
                return
    print("Driver Ratings:",DriverRatings)
    RandomizationRanges={
        "high":{
            "driverOptimism":{"min":90,"max":100},
            "driverAggression":{"min":90,"max":100},
            "driverSmoothness":{"min":90,"max":100},
            "strategyRiskiness":{"min":75,"max":100},
            "pitCrewSkill":{"min":95,"max":100}
        },
        "medium":{
            "driverOptimism":{"min":80,"max":89},
            "driverAggression":{"min":80,"max":89},
            "driverSmoothness":{"min":80,"max":89},
            "strategyRiskiness":{"min":65,"max":80},
            "pitCrewSkill":{"min":80,"max":94}
        },
        "low":{
            "driverOptimism":{"min":70,"max":79},
            "driverAggression":{"min":70,"max":79},
            "driverSmoothness":{"min":70,"max":79},
            "strategyRiskiness":{"min":60,"max":70},
            "pitCrewSkill":{"min":60,"max":79}
        }
    }
    for driver in Data.get('drivers',[]):
        DriverName=driver.get('driverName','').strip()
        if DriverName:
            DriverNameCleaned=DriverName.replace(',','').replace('.','').strip()
            if DriverNameCleaned in DriverRatings:
                DriverSkill=DriverRatings[DriverNameCleaned]
                driver['driverSkill']=DriverSkill
                if DriverSkill>=90:
                    SkillLevel="high"
                elif 80<=DriverSkill<=89:
                    SkillLevel="medium"
                elif 0<=DriverSkill<=79:
                    SkillLevel="low"
                if SkillLevel:
                    ranges=RandomizationRanges[SkillLevel]
                    for param in ranges:
                        MinVal=ranges[param]['min']
                        MaxVal=ranges[param]['max']
                        driver[param]=random.randint(MinVal,MaxVal)
            else:
                UnmatchedDrivers.append(DriverNameCleaned)
    FilePath=os.path.join(DefaultDir,"Edited Rosters",JSONName)
    with open(FilePath,'w') as file:
        json.dump(Data,file,indent=4)
    if UnmatchedDrivers:
        print("Drivers not found in text file, please review:")
        for driver_name in UnmatchedDrivers:
            print(driver_name)
    else:
        print("All stats successfully updated.")
    input()

if __name__=="__main__":
    MainMenu()