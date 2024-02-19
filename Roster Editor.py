import os
import json
import random

DefaultDir = os.getcwd()

if not os.path.exists(os.path.join(DefaultDir,"Edited Rosters")):
    os.makedirs(os.path.join(DefaultDir,"Edited Rosters"))
if not os.path.exists(os.path.join(DefaultDir,"iRacing Rosters")):
    os.makedirs(os.path.join(DefaultDir,"iRacing Rosters"))
if not os.path.exists(os.path.join(DefaultDir,"Ratings")):
    os.makedirs(os.path.join(DefaultDir,"Ratings"))

UserInput = input("Enter iRacing roster name to edit: ")
if not UserInput.endswith(".json"):
    UserInput+=".json"
JSONName=UserInput
FilePath=os.path.join(DefaultDir,"iRacing Rosters",UserInput)
try:
    with open(FilePath,'r') as file:
        Data = json.load(file)
except Exception as e:
    print("Error loading JSON file:",e)
    input()
    exit()

DriverRatings={}
UnmatchedDrivers=[]

UserInput=input("Enter rating file to use: ")
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
            elif 70<=DriverSkill<=79:
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