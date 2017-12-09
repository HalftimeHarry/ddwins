import sys
import sqlite3
 
conn = sqlite3.connect('game_results.db')
 
 
 
c = conn.cursor()
 
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS game_results
             (home_team text, 
              end_date text, 
              o_u_diff float
             )''')
              
 
 
# Save (commit) the changes
conn.commit()
 
# Just be sure any changes have been committed or they will be lost.
conn.close()
#The data you've saved is persistent and is available in subsequent sessions: