"""
====================================================================

____Be able to extract info and compare results via results.db

Vegas Streak          Totals           Teams Played        Harrys Ratings  Coaching        How Hary Did           What does Harry have

   LAR             Over Over Over       CLE  DEN  ATL      Like             No opinion     Correct Wrong Correct        Over
   DAL             Under Under Under    KAN  BUF  CAR      Dont Like        Do not like    Correct Wrong Wrong          Under
   PHI             Over Over Over       BAL  SEA  PIT      No Opinion       Nutrual        Correct Correct Correct      Under
   PHI             Over Over Over       SEA  PIT  LAC      No Opinion       Nutrual        Correct Correct Correct      Under

====================================================================
"""
import os
import sys
import sqlite3
 
if __name__ == '__main__':
     
    os.system('rm game_results.db')
    # Create new results db
    os.system('python game_results.py')
 
    smasher_correct_total = 0
    smasher_wrong_total = 0
    smasher_pushed_total = 0
    smasher_passed_on_total = 0 
 
     
#    for season in [2015, 2016, 2017]:
    for season in [2017]:
        print "\nSeason:", season
        for week in range(18, 19):
             
            #print season, week
            os.system("python prediction_generator.py " + '-s ' + str(season) + ' -w ' + str(week))
         
    # Read from the results db to print out results.
     
    conn = sqlite3.connect('game_results.db')
    c = conn.cursor() 
 
    cmd = 'SELECT home_team, season, week, over_correct_cnt, under_correct_cnt, over_wrong_cnt, under_wrong_cnt, did_not_play_cnt, over_pushed_cnt, under_pushed_cnt, on_streak, streak_type, teams_played, coaching, how_harry_did, what_does_harry_have FROM game_results;'
    print cmd
    c.execute(cmd)
    rows = c.fetchall()
    for row in rows:
    #    print "   %s\t     %s\t %s\t      %02d    \t%02.1f\t %02.1f\t    %02.1f         %s" % (home_team, prediction, predicted_result, details['actual_total'], details['margin'], details['average'], details['ou_total'], final_result)
 
        
        season = row[1]
        week = row[2]
        over_correct = row[3]
        under_correct = row[4]
        over_wrong = row[5]
        under_wrong = row[6]
        passed = row[7]
        over_pushed = row[8] 
        under_pushed = row[9]
        
        test_on_streak = row[10]
        
        
        
        
        
        print "\nOn Streak Test:", test_on_streak        
        print "\nSeason:", season
        print "Week:", week
#        print "over correct this week", over_correct
#        print "under correct this week", under_correct
#        print "over wrong this week", over_wrong
#        print "under wrong this week", under_wrong
        print "passed on", passed #todo need to fix this
#        print "over pushed this week", over_pushed 
#        print "under pushed this week", under_pushed 
         
        correct_for_week_result = over_correct + under_correct
        print "correct this week result", correct_for_week_result
        wrong_for_week_result = over_wrong + under_wrong
        print "wrong this week result", wrong_for_week_result
        pushed_for_week_result = over_pushed + under_pushed
        print "pushed this week result", pushed_for_week_result
        
        
        smasher_correct_total += correct_for_week_result
        #smasher_passed_on_total += 
        smasher_pushed_total += pushed_for_week_result
        smasher_wrong_total += wrong_for_week_result
     
    print "\n\nThe Smasher Result"
    print "  Correct:", smasher_correct_total
    print "  Wrong:", smasher_wrong_total
    print "  Pushed:", smasher_pushed_total
    
    tt = 'DAL'
    tot = 'Over'
    tp = 'DAL ATL PIT'
    hrc = 'good'
    hhd = 'won won won'
    hh = 'Over'
    
    print "\n\nOn Streak | Type | Teams Played |  Coaching |  How Hary Did | What does Harry have"
    print "%s\t   %s\t   %s\t   %s\t       %s\t  %s\t  " % (tt, tot, tp, hrc, hhd, hh)
 