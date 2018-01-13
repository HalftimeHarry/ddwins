import sys
import sqlite3
 
conn = sqlite3.connect('game_results.db')
 
 
 
c = conn.cursor()
 
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS game_results
             (home_team text, 
              season int, 
              week int, 
              over_correct_cnt int,
              under_correct_cnt int,
              over_wrong_cnt int,
              under_wrong_cnt int,
              did_not_play_cnt int,
              over_pushed_cnt int, 
              under_pushed_cnt int,
              on_streak text,
              streak_type text,
              teams_played text,
              coaching text,
              how_harry_did text,
              what_does_harry_have text
             )''')
              
 
# Save (commit) the changes
conn.commit()
 
# Just be sure any changes have been committed or they will be lost.
conn.close()
#The data you've saved is persistent and is available in subsequent sessions: