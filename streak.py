import sys
import sql
import datetime
import time
import argparse
import sqlite3
  
PRED_GEN_VERSION = '0.5'
  
  
'''
    ------------------
    
    Go through each team durring the season to deturmine who is on a streak
    
  
'''
  
  
  
  
if __name__ == '__main__':
      
    s = sql.Sql('games.db')
  
    parser = argparse.ArgumentParser(description='Predicts sports outcomes.', prog='prediction_generator.py')
      
    parser.add_argument('-s', '--season', type=str, action='store', required=True, help="season in the form: 2015-2016")
    parser.add_argument('-w', '--week', type=str, action='store', required=True, help='Week of season: 1')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s' + PRED_GEN_VERSION)
    args = parser.parse_args()
      
    season, week = [args.season, args.week]
     
 
    print "\nSeason: %s, Week: %s" % (season, week)
  
      # TO DO: create a get_teams_on_streak_list(season, week)
    streak_list = s.get_teams_on_streak_list(season, week)
#    streak_list = ('DAL','KAN')
    print "Streak list for week:", week
    print streak_list
  
    print "Streak  Prediction  Predicted result  Actual total  Margin  Calc Avg  Vegas Line   Past or Pending"
    over_streak_cnt = 0
    under_streak_cnt = 0
     
    conn = sqlite3.connect('game_results.db')
 
    c = conn.cursor()
     
    for streak in streak_list:
        
        # TO DO: create a function called get_targeted_game_streak_details
        details2 = s.get_targeted_game_streak_details(season, week)
          
        #print "Streak:", streak
        #print "details2:", details2
          
        #print "Predicted:",
        if details2['margin'] > 0:
            prediction = "Over"
        elif details2['margin'] < 0:
            prediction = "Under"
        else:
            prediction = "Dont play"
   
        predicted_result = "No Action"
 #       print "Predicted:",
  
        streaking_team = 'The streaking team'
  
 #here is where I start trying to add this in the database testing 
        if details2['home_team'] != 0:
            on_streak_text = "Is on a streak!"
            on_streak = streaking_team
         
        print()
  
#        print "   %s\t     %s\t %s\t      %d\t%02.1f\t %02.1f\t    %02.1f         %s" % (streak, prediction, predicted_result, details2['actual_total'], details2['margin'], details2['average'], details2['ou_total'], final_result)
 
    streak_type = 'over'
    teams_played = 'DAL WAS PHI'
    coaching = 'sucks'
    how_harry_did = 'won'
    what_does_harry_have = 'Over'
    
 
    conn.commit()
    conn.close()