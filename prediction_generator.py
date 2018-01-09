import sys
import sql
import datetime
import time
import argparse
import sqlite3
  
PRED_GEN_VERSION = '0.5'
  
  
'''
  
This program will output all the home team the predictions over/under for a week.
input arguments: Date to run. The result column only shows up if the date selected
was from the past.
  
Output:
Season: 2016, Week: 17
Home team list for week: 17
['ATL', 'MIN', 'IND', 'PHI', 'DET', 'MIA', 'NYJ', 'TAM', 'WAS', 'TEN', 'CIN', 'PIT', 'LAC', 'DEN', 'SFO', 'LAR']
Home team  Prediction  Predicted result  Actual total  Margin  Calc Avg  Vegas Line
   ATL       Over        Correct Over         70        4.2      62.8       58.5         Past Game
   MIN       Under       Wrong Under          48        -8.3     35.7       44.0         Past Game
   IND       Under       Correct Under        44        -1.4     47.1       48.5         Past Game
    
   Correct Over 44
   Wrong Over 22
   Correct Under 55
   Wrong Under 21
   Off 3
    
    
  
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
  
      
    home_team_list = s.get_home_team_list_for_season_week2(season, week)
    print "Home team list for week:", week
    print home_team_list
  
    print "Home team  Prediction  Predicted result  Actual total  Margin  Calc Avg  Vegas Line   Past or Pending"
    over_correct_cnt = 0
    over_wrong_cnt = 0
    under_correct_cnt = 0
    under_wrong_cnt = 0
    did_not_play_cnt = 0
    over_pushed_cnt = 0
    under_pushed_cnt = 0
     
    conn = sqlite3.connect('game_results.db')
 
    c = conn.cursor()
     
    for home_team in home_team_list:
        details = s.get_targeted_game_details3(home_team, season, week)
          
        #print "Home team:", home_team
        #print "Details:", details
          
        #print "Predicted:",
        if details['margin'] > 0:
            prediction = "Over"
        elif details['margin'] < 0:
            prediction = "Under"
        else:
            prediction = "Dont play"
   
        predicted_result = "No Action"
 #       print "Predicted:",
  
         
        if details['margin'] > 0 and float(details['actual_total']) > details['ou_total']:
            predicted_result = "Correct Over"
            over_correct_cnt += 1
        if details['margin'] < 0 and float(details['actual_total']) < details['ou_total']:
            predicted_result = "Correct Under"
            under_correct_cnt += 1
        if details['margin'] > 0 and float(details['actual_total']) < details['ou_total']:
            predicted_result = "Wrong Over"
            over_wrong_cnt += 1
        if details['margin'] < 0 and float(details['actual_total']) > details['ou_total']:
            predicted_result = "Wrong Under"
            under_wrong_cnt += 1
        if details['margin'] > 0 and float(details['actual_total']) == details['ou_total']:
            predicted_result = "Pushed Over"
            over_pushed_cnt += 1
        if details['margin'] > 0 and float(details['actual_total']) == details['ou_total']:
            predicted_result = "Pushed Under"
            under_pushed_cnt += 1
        if details['margin'] < 0 and float(details['actual_total']) == details['ou_total']:
            predicted_result = "Pushed Under"
            under_pushed_cnt += 1
        elif details['margin'] > 0 and float(details['actual_total']) == details['ou_total']:
            predicted_result = "Did not play"
            did_not_play_cnt += 1
#        print "Actual total:", details['actual_total']
#        print "Actual margin:", details['average']
        if details['actual_total'] == '0':
            final_result = "Pending Game"
        elif details['average'] >= 0:
            final_result = "Past Game"
  
        print "   %s\t     %s\t %s\t      %d\t%02.1f\t %02.1f\t    %02.1f         %s" % (home_team, prediction, predicted_result, details['actual_total'], details['margin'], details['average'], details['ou_total'], final_result)
 
    cmd = "INSERT INTO game_results VALUES ('" + home_team + "','" + str(season) + "','" + str(week) + "','" + str(over_correct_cnt) + "','" + str(under_correct_cnt) + "','"\
                                               + str(over_wrong_cnt) + "','" + str(under_wrong_cnt) + "','"+ str(did_not_play_cnt) + "','" + str(over_pushed_cnt) + "','"\
                                               + str(under_pushed_cnt) + "')"
    print cmd
    c.execute(cmd)
 
    conn.commit()
    conn.close()