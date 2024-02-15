def mainmenu():
    while True:
        os.system('cls')
        print("Welcome to Tyler's Driver Rating Calculator")
        print("Python Version 0.1")
        print()
        print("With this tool, you can calculate a driver's rating based on their stats for a season.")
        print("This tool was made with the stats available from https://www.racing-reference.info/ in mind.")
        print()
        print(f"Current data pool: {rostername}") #formatted string literals, Python 3.6 or later
        print("To begin calculations, enter 'Calc'")
        print("To load a data pool, type 'Load'")
        print("To save the current data pool, type 'Save'")
        print("To enter a new data pool, type 'Edit'")
        print("To edit calculation settings, type 'Settings'")
        print("To view all current data, type 'View'")
        print("To view the changelog, type 'Log'")
        print("To see the current to do list, type 'To Do'")
        print("To quit, type 'Exit'")
        userinput=input(">").lower()
        if userinput=='exit':
            break
        elif userinput=='log':
            changelog()
        elif userinput=='view':
            viewdata()
        elif userinput=='edit':
            editdata()
        elif userinput=='load':
            loaddata()
        elif userinput=='save':
            savedata()
        elif userinput=='settings':
            settings()
        elif userinput=='calc':
            ratingcalc()
        elif userinput=='to do':
            todo()
        else:
            input("Invalid choice.")

def changelog():
    os.system('cls')
    print("v0.1 02/xx/2024")
    print("-initial python build, port from basic to make a version i might eventually be willing to share")
    input()

def todo():
    os.system('cls')
    print("-save ratings to text file while calculating")
    print("-check weight when inputting to ensure they add up to 100%")
    print("-check normalization values to ensure they are valid iracing options")
    print("-general error handling")
    print(" -entered value outside data range")
    print("-have program save a text file with the settings, load existing settings if present when program starts")
    input("-implement compensation calculation")

def viewdata():
    os.system('cls')
    global rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf,winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight,normmin,normmax
    print(f"Roster name: {rostername}")
    print(f"Best championship finish: {champfinbest}")
    print(f"Worst championship finish: {champfinworst}")
    print(f"Max races: {maxrace}")
    print(f"Min races: {minrace}")
    print(f"Max wins: {maxwin}")
    print(f"Min wins: {minwin}")
    print(f"Max top fives: {maxtopfive}")
    print(f"Min top fives: {mintopfive}")
    print(f"Max top tens: {maxtopten}")
    print(f"Min top tens: {mintopten}")
    print(f"Max poles: {maxpole}")
    print(f"Min poles: {minpole}")
    print(f"Max laps ran: {maxlap}")
    print(f"Min laps ran: {minlap}")
    print(f"Max laps led: {maxled}")
    print(f"Min laps led: {minled}")
    print(f"Best average start: {beststart}")
    print(f"Worst average start: {worststart}")
    print(f"Best average finish: {bestfin}")
    print(f"Worst average finish: {worstfin}")
    print(f"Max RAF: {maxraf}")
    print(f"Min RAF: {minraf}")
    print(f"Max LLF: {maxllf}")
    print(f"Min LLF: {minllf}")
    print(f"Win weight: {winweight*100}%")
    print(f"Top five weight: {topfiveweight*100}%")
    print(f"Top ten weight: {toptenweight*100}%")
    print(f"Pole weight: {poleweight*100}%")
    print(f"Laps ran weight: {lapweight*100}%")
    print(f"Laps led weight: {ledweight*100}%")
    print(f"Average start weight: {startweight*100}%")
    print(f"Average finish weight: {finweight*100}%")
    print(f"RAF weight: {rafweight*100}%")
    print(f"LLF weight: {llfweight*100}%")
    print(f"Normalization minimum: {normmin}%")
    input(f"Normalization maximum: {normmax}%")

def editdata():
    os.system('cls')
    global rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf
    print("Enter the number -1 to exit without saving.")
    prompts=[
        "Roster name: ",
        "Highest championship finish: ",
        "Lowest championship finish: ",
        "Maximum races entered: ",
        "Minimum races entered: ",
        "Maximum races won: ",
        "Minimum races won: ",
        "Maximum top fives: ",
        "Minimum top fives: ",
        "Maximum top tens: ",
        "Minimum top tens: ",
        "Maximum poles: ",
        "Minimum poles: ",
        "Maximum laps ran: ",
        "Minimum laps ran: ",
        "Maximum laps led: ",
        "Minimum laps led: ",
        "Best average start: ",
        "Worst average start: ",
        "Best average finish: ",
        "Worst average finish: ",
        "Maximum RAFs: ",
        "Minimum RAFs: ",
        "Maximum LLFs: ",
        "Minimum LLFs: "
    ]
    userinputs=[]
    for prompt in prompts:
        userinput=input(prompt)
        if userinput=='-1':return
        userinputs.append(userinput)
    if len(userinputs)==len(prompts):
        rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf=userinputs
    os.system('cls')
    input("Data pool entered.")

def read_numbers_from_file(filename):
    #the function that ensures text files contain the correct number of data entries
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(float(line.strip()))
    return numbers

def loaddata():
    os.system('cls')
    global rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf
    filename=input("Enter roster name to load: ").lower()
    try:
        if not filename.endswith(".txt"):
            filename+=".txt"
        storage=read_numbers_from_file(filename)
        if len(storage)!=24:
            input("Invalid file. Please ensure text file contains all required data.")
            return
        champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf=storage
        rostername=filename[:-4]
        input("Roster loaded.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        input()
    except ValueError:
        print("Error: The file must contain valid numbers on each line.")
        input()
    except Exception as e:
        print("An error occurred:", e)
        input()

def savedata():
    os.system('cls')
    global rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf
    print("Saving...")
    filename=rostername+".txt"
    try:
        with open(filename, 'w') as file:
            file.write(f"{champfinbest}")
            file.write(f"\n{champfinworst}")
            file.write(f"\n{maxrace}")
            file.write(f"\n{minrace}")
            file.write(f"\n{maxwin}")
            file.write(f"\n{minwin}")
            file.write(f"\n{maxtopfive}")
            file.write(f"\n{mintopfive}")
            file.write(f"\n{mintopfive}")
            file.write(f"\n{mintopten}")
            file.write(f"\n{maxpole}")
            file.write(f"\n{minpole}")
            file.write(f"\n{maxlap}")
            file.write(f"\n{minlap}")
            file.write(f"\n{maxled}")
            file.write(f"\n{minled}")
            file.write(f"\n{beststart}")
            file.write(f"\n{worststart}")
            file.write(f"\n{bestfin}")
            file.write(f"\n{worstfin}")
            file.write(f"\n{maxraf}")
            file.write(f"\n{maxraf}")
            file.write(f"\n{maxllf}")
            file.write(f"\n{minllf}")
        input("Data pool saved.")
    except Exception as e:
        print("An error occurred:", e)
        input()
  
def settings():
    os.system('cls')
    global winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight,normmin,normmax
    print("Enter the number -1 to exit without saving.")
    prompts=[
        "Win weight%: ",
        "Top five weight%: ",
        "Top ten weight%: ",
        "Pole weight%: ",
        "Laps ran weight%: ",
        "Laps led weight%: ",
        "Average start weight%: ",
        "Average finish weight%: ",
        "RAF weight%: ",
        "LLF weight%: ",
        "Normalization minimum: ",
        "Normalization maximum: ",
    ]
    userinputs=[]
    for prompt in prompts:
        userinput=input(prompt)
        if userinput=='-1':return
        userinputs.append(userinput)
    if len(userinputs)==len(prompts):
        winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight,normmin,normmax=userinputs
    os.system('cls')
    input("Settings saved.")

def ratingcalc():
    global rostername,champfinbest,champfinworst,maxrace,minrace,maxwin,minwin,maxtopfive,mintopfive,maxtopten,mintopten,maxpole,minpole,maxlap,minlap,maxled,minled,beststart,worststart,bestfin,worstfin,maxraf,minraf,maxllf,minllf,winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight,normmin,normmax
    while True:
        os.system('cls')
        print("Enter the number -1 to exit without saving.")
        prompts=[
            "Driver name: ",
            "Races started: ",
            "Races won: ",
            "Top fives: ",
            "Top tens: ",
            "Poles: ",
            "Laps ran: ",
            "Laps led: ",
            "Average start: ",
            "Average finish: ",
            "RAF: ",
            "LLF: "
        ]
        userinputs=[]
        for prompt in prompts:
            userinput=input(prompt)
            if userinput=='-1':return
            userinputs.append(userinput)
        if len(userinputs)==len(prompts):
            drivername,racestart,driverwin,driverfive,driverten,driverpole,driverlap,driverled,driverstart,driverfin,driverraf,driverllf=userinputs
        os.system('cls')
        print()
        print(f"Driver name: {drivername}")
        print(f"Races started: {racestart}")
        print(f"Races won: {driverwin}")
        print(f"Top fives: {driverfive}")
        print(f"Top tens: {driverten}")
        print(f"Poles: {driverpole}")
        print(f"Laps ran: {driverlap}")
        print(f"Laps led: {driverled}")
        print(f"Average start: {driverstart}")
        print(f"Average finish: {driverfin}")
        print(f"RAF: {driverraf}")
        print(f"LLF: {driverllf}")
        print()
        print("Confirm data entry? Y/N")
        userinput=input().lower()
        racestart=float(racestart)
        driverwin=float(driverwin)
        driverfive=float(driverfive)
        driverten=float(driverten)
        driverpole=float(driverpole)
        driverlap=float(driverlap)
        driverled=float(driverled)
        driverstart=float(driverstart)
        driverfin=float(driverfin)
        driverraf=float(driverraf)
        driverllf=float(driverllf)
        maxrace=float(maxrace)
        minrace=float(minrace)
        maxwin=float(maxwin)
        minwin=float(minwin)
        maxtopfive=float(maxtopfive)
        mintopfive=float(mintopfive)
        maxtopten=float(maxtopten)
        mintopten=float(mintopten)
        maxpole=float(maxpole)
        minpole=float(minpole)
        maxlap=float(maxlap)
        minlap=float(minlap)
        maxled=float(maxled)
        minled=float(minled)
        minled=float(minled)
        worststart=float(worststart)
        bestfin=float(bestfin)
        worstfin=float(worstfin)
        maxraf=float(maxraf)
        minraf=float(minraf)
        maxllf=float(maxllf)
        minllf=float(minllf)
        winweight=float(winweight)
        topfiveweight=float(topfiveweight)
        toptenweight=float(toptenweight)
        poleweight=float(poleweight)
        lapweight=float(lapweight)
        ledweight=float(ledweight)
        startweight=float(startweight)
        finweight=float(finweight)
        rafweight=float(rafweight)
        llfweight=float(llfweight)
        normmin=float(normmin)
        normmax=float(normmax)
        if racestart<maxrace:compensatecalc()
        ratewin=(((driverwin-minwin)/(maxwin-minwin))*100)*winweight
        ratefive=(((driverfive-mintopfive)/(maxtopfive-mintopfive))*100)*topfiveweight
        rateten=(((driverten-mintopten)/(maxtopten-mintopten))*100)*toptenweight
        ratepole=(((driverpole-minpole)/(maxpole-minpole))*100)*poleweight
        ratelap=(((driverlap-minlap)/(maxlap-minlap))*100)*lapweight
        rateled=(((driverled-minled)/(maxled-minled))*100)*ledweight
        ratestart=(((driverstart-worststart)/(beststart-worststart))*100)*startweight
        ratefin=(((driverfin-worstfin)/(bestfin-worstfin))*100)*finweight
        rateraf=(((driverraf-minraf)/(maxraf-minraf))*100)*rafweight
        ratellf=(((driverllf-minllf)/(maxllf-minllf))*100)*llfweight
        rating=normmin+(((ratewin+ratefive+rateten+ratepole+ratelap+rateled+ratestart+ratefin+rateraf+ratellf)*(normmax-normmin))/100)
        if rating>normmax:rating=normmax
        print()
        print(f"{drivername}'s rating is:")
        print(round(rating))
        input()
        
def compensatecalc():
    print("compensation")
    input()
    return

if __name__=="__main__":
    import os
    #this program was originally made because i needed to calculate driver ratings for the 2009 cup series
    #ive calculated jimmie johnson's rating so many times that i just use the 2009 season by default lol
    rostername="2009 nascar cup series"
    champfinbest,champfinworst=1,67
    maxrace,minrace=36,1
    maxwin,minwin=7,0
    maxtopfive,mintopfive=16,0
    maxtopten,mintopten=25,0
    maxpole,minpole=7,0
    maxlap,minlap=10468,8
    maxled,minled=2238,0
    beststart,worststart=8.3,43
    bestfin,worstfin=10.2,43
    maxraf,minraf=36,0
    maxllf,minllf=31,0
    winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight=.25,.16,.11,.06,.04,.09,.05,.12,.04,.08
    normmin,normmax=60,100
    mainmenu()