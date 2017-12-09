import sys
import csv
import sqlite3
 
conn = sqlite3.connect('games.db')
# You can also supply the special name :memory: to create a database in RAM.
 
# Once you have a Connection, you can create a Cursor object and call its 
# execute() method to perform SQL commands:
 
c = conn.cursor()
 
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS games
             (Season text, Week text, Date text, Home_Team text,
              Home_Score text, Home_Opening_Spread text, Home_Closing_Spread text, Home_Opening_ML text,
              Home_Opening_ML_Decimal text, Home_Closing_ML text, Home_Closing_ML_decimal text, Away_Team text,
              Away_Score text, Away_Opening_Spread text, Away_Closing_Spread text, Away_Opening_ML text, 
              Away_Opening_ML_Decimal text, Away_Closing_ML text, Away_Closing_ML_decimal text, Opening_O_U_Total text,
              Closing_O_U_Total text)''')
              
with open('past_games.txt', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        print row
        if i > 0:
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