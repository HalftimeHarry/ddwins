import os
import sys
import sql
import sqlite3
import prediction_generator

'''
  
This program will output all results data
  
Output:
Season: 2017
Week: 12
passed on 0
correct this week result 9
wrong this week result 7
pushed this week result 0

Starting on 2015 Week 1 to 2017 Week 16
The Smasher 
Correct 92
Wrong 33
Pushed 2
Passed on 2
    
  
'''
 
if __name__ == '__main__':
     
    os.system('del game_results.db')
    # Create new results db
    os.system('python game_results.py')
 
    for season in [2015, 2016, 2017]:
        print "\nSeason:", season
        for week in range(12,17):
             
            #print season, week
            os.system("python prediction_generator.py " + '-s ' + str(season) + ' -w ' + str(week))
         
    # Read from the results db to print out results.
     
    conn = sqlite3.connect('game_results.db')
    c = conn.cursor() 
 
    cmd = 'SELECT home_team, season, week, over_correct_cnt, under_correct_cnt, over_wrong_cnt, under_wrong_cnt, did_not_play_cnt, over_pushed_cnt, under_pushed_cnt FROM game_results;'
    print cmd
    c.execute(cmd)
    rows = c.fetchall()
    for row in rows:
        print "   %s\t     %s\t %s\t      %d    \t%02.1f\t %02.1f\t    %02.1f         %s" % (home_team, prediction, predicted_result, details['actual_total'], details['margin'], details['average'], details['ou_total'], final_result)
        print "\nSeason:", row[1]
        print "Week:", row[2]
#        print "over correct this week", row[3]
#        print "under correct this week", row[4]
#        print "over wrong this week", row[5]
#        print "under wrong this week", row[6]
        print "passed on", row[7] #todo need to fix this
#        print "over pushed this week", row[8] #todo need to fix this
#        print "under pushed this week", row[9] #todo need to fix this
         
        correct_for_week_result = row[3] + row[4]
        print "correct this week result", correct_for_week_result
        wrong_for_week_result = row[5] + row[6]
        print "wrong this week result", wrong_for_week_result
        pushed_for_week_result = row[8] + row[9]
        print "pushed this week result", pushed_for_week_result
        