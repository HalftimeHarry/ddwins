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
  
      # TO DO: create a get_streak_list_for_season_week(season, week)
    streak_list = s.get_streak_list_for_season_week(season, week)
    print "Streak list for week:", week
    print streak_list
  
    print "Streak  Prediction  Predicted result  Actual total  Margin  Calc Avg  Vegas Line   Past or Pending"
    over_streak_cnt = 0
    under_streak_cnt = 0
     
    conn = sqlite3.connect('game_results.db')
 
    c = conn.cursor()
     
    for streak in streak_list:
        
        # TO DO: create a function called get_targeted_game_streak_details
        details2 = s.get_targeted_game_details23(streak, season, week)
          
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
        if details2['margin'] != 0:
            on_streak_text = "Is on a streak!"
            on_streak = streaking_team
         
        if details2['margin'] > 0 and float(details2['actual_total']) > details2['ou_total']:
            predicted_result = "Correct Over"
            over_correct_cnt += 1
        if details2['margin'] < 0 and float(details2['actual_total']) < details2['ou_total']:
            predicted_result = "Correct Under"
            under_correct_cnt += 1
        if details2['margin'] > 0 and float(details2['actual_total']) < details2['ou_total']:
            predicted_result = "Wrong Over"
            over_wrong_cnt += 1
        if details2['margin'] < 0 and float(details2['actual_total']) > details2['ou_total']:
            predicted_result = "Wrong Under"
            under_wrong_cnt += 1
        if details2['margin'] > 0 and float(details2['actual_total']) == details2['ou_total']:
            predicted_result = "Pushed Over"
            over_pushed_cnt += 1
        if details2['margin'] > 0 and float(details2['actual_total']) == details2['ou_total']:
            predicted_result = "Pushed Under"
            under_pushed_cnt += 1
        if details2['margin'] < 0 and float(details2['actual_total']) == details2['ou_total']:
            predicted_result = "Pushed Under"
            under_pushed_cnt += 1
        elif details2['margin'] > 0 and float(details2['actual_total']) == details2['ou_total']:
            predicted_result = "Did not play"
            did_not_play_cnt += 1
#        print "Actual total:", details2['actual_total']
#        print "Actual margin:", details2['average']
        if details2['actual_total'] == '0':
            final_result = "Pending Game"
        elif details2['average'] >= 0:
            final_result = "Past Game"
  
        print "   %s\t     %s\t %s\t      %d\t%02.1f\t %02.1f\t    %02.1f         %s" % (streak, prediction, predicted_result, details2['actual_total'], details2['margin'], details2['average'], details2['ou_total'], final_result)
 
    streak_type = 'over'
    teams_played = 'DAL WAS PHI'
    coaching = 'sucks'
    how_harry_did = 'won'
    what_does_harry_have = 'Over'
    
    cmd = "INSERT INTO game_results VALUES ('" + streak + "','" + str(season) + "','" + str(week) + "','" + str(over_correct_cnt) + "','" + str(under_correct_cnt) + "','"\
                                               + str(over_wrong_cnt) + "','" + str(under_wrong_cnt) + "','"+ str(did_not_play_cnt) + "','" + str(over_pushed_cnt) + "','"\
                                               + str(under_pushed_cnt) + "','" + str(on_streak) + "','" + str(streak_type) + "','" + str(teams_played) + "','" + str(coaching) + "','" + str(how_harry_did) + "','" + str(what_does_harry_have) + "')"
    print cmd
    c.execute(cmd)
 
    conn.commit()
    conn.close()