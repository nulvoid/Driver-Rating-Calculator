# V2.2.1 - Released 2/19/24

This Python program will convert a .html file containing a table of a race season's standings into a text file with the driver's name and their calculated rating. I'm hesitant to call it a skill rating calculator, but that is how I use this program. I originally wrote this program in BASIC (JustBasic specificially) because I wanted to use semi-realistic skill ratings in my AI rosters. I got sick of using ChatGPT to give me ratings, and they were highly inconsistent, so eventually I wrote this in BASIC. I have a way better understanding of BASIC than Python because I started programming on a TI-83 calculator when I was in middle school lol. The entire time I craved a program that I could just enter an entire season's worth of data into and get ratings, which is why I switched to Python. The first version of this program in Python was very similar to the BASIC version, requiring you to enter the stats for every single driver manually. I got sick of that very quickly though, and I'm sure you would too. After a lot of caffeine and weed, I finally learned how to write the program that I (mostly) wanted. I really wanted to be able to just enter a link and it does all the work for me, but I have absolutely no real training in any programming language and to be honest, I'm very lazy. I know it looks like I'm writing this all up and sharing it on Github with the intent of sharing this with many people to use, but realistically, I don't see any more than a handful of people other than me using this. The biggest reason I have this on here is because I was too stupid to make actual backups of the BASIC version of this program, and ended up losing days of work spread out over a span of two months because I had to reinstall Windows on my computer. Thankfully, for me, I had a version of the program from 1/05/24 backed up on my laptop. Only issue is, I had been working on it every couple of days and had lost a lot of changes and quality of life improvements I made over the course of a month. I am not letting that happen this time lol. In a way, I guess you could say I have been working on this program for three months now, since I started the BASIC version on 11/11/23.

## Requirements

- Python version 3.6+
- pandas
- BeautifulSoup4
- Racing Reference season standings with all required data
  - For example, the 1987 Busch North Series cannot be calculated because it is missing average start data for a number of drivers

The required Python libraries can be installed with the pip command in your terminal.\
    ```pip install pandas```
    ```pip install beautifulsoup4```

## Preparing a .html file

1. Navigate to the season's full point standings on Racing Reference.

2. Right click and inspect element the table containing the season's point standings. The table should found under the element beginning with:
   
   ```<table class="tb standingsTbl" width="100%" cellpadding="3" cellspacing="0">```

3. Copy the HTML code for the entire table element.

4. Save the HTML code as the season's name in the Season Files folder.

## Using the program

1. When you have your .html ready, run the program.
2. Type **calc** and press enter to start the program.
3. Enter the name of the .html file you created and press enter.
4. The program will save a text file of the same name in the Ratings folder.