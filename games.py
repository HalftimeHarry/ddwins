import sys
import csv
import sqlite3

conn = sqlite3.connect('games.db')
# You can also supply the special name :memory: to create a database in RAM.

# Once you have a Connection, you can create a Cursor object and call its 
# execute() method to perform SQL commands:


def fix_week(week):
    '''Converts the text Week_12 to 12, Week3 to 3
       i.e. strips Week and _ from Week field.'''
    week = week.replace('Week', '')
    week = week.replace('_', '')
    week = week.replace(' ', '')
    return week

def fix_date(date):
    '''Converts date format from 9/20/15 to a format
       Sqlite3 understands: 2015-20-09'''
    month_end = date.find('/')
    month = date[:month_end]
    day_end = date.find('/', month_end + 1)
    day = date[month_end + 1: day_end]
    new_date = "%4s-%02d-%02d" % ('20'+date[-2:], int(month), int(day))
    return new_date



c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS games
             (Season text, Week text, Date text, Home_Team text,
              Home_Score integer, Home_Opening_Spread real, Home_Closing_Spread real, Home_Opening_ML real,
              Home_Opening_ML_Decimal real, Home_Closing_ML real, Home_Closing_ML_decimal real, Away_Team text,
              Away_Score integer, Away_Opening_Spread real, Away_Closing_Spread real, Away_Opening_ML real, 
              Away_Opening_ML_Decimal real, Away_Closing_ML real, Away_Closing_ML_decimal real, Opening_O_U_Total real,
              Closing_O_U_Total real)''')
             
with open('past_games.txt', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i > 0:
            row[1] = fix_week(row[1]) # Just save the number: Week3 -> 3, Week_12 -> 12
            row[2] = fix_date(row[2]) # Change format from 9/20/15 -> 2015:20:09, 10/1/16 -> 2016:01:10
            cmd = "INSERT INTO games VALUES ('" + row[0] + "','" + row[1] + "','" + row[2] + "','" + row[3] + "','"\
                                                + row[4] + "','" + row[5] + "','" + row[6] + "','" + row[7] + "','"\
                                                + row[8] + "','" + row[9] + "','" + row[10] + "','" + row[11] + "','"\
                                                + row[12] + "','" + row[13] + "','" + row[14] + "','" + row[15] + "','"\
                                                + row[16] + "','" + row[17] + "','" + row[18] + "','" + row[19] + "','"\
                                                + row[20] + "')"

            print cmd
            c.execute(cmd)
        i += 1

# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()
#The data you've saved is persistent and is available in subsequent sessions:

