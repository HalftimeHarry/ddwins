import sys
import sql
import datetime
import time
import argparse
 
PRED_GEN_VERSION = '0.4'
 
 
'''
 
This program will output all the home team the predictions over/under for a week.
input arguments: Date to run. The result column only shows up if the date selected
was from the past.
 
Output:
    Home team  Prediction    margin      result
    ---------------------------------------------
       DAL         over        4          correct
       ATL         under       -5         wrong
 
'''
 
if __name__ == '__main__':
     
    s = sql.Sql('games.db')
 
    parser = argparse.ArgumentParser(description='Predicts sports outcomes.', prog='prediction_generator.py')
     
    parser.add_argument('-s', '--season', type=str, action='store', required=True, help="season in the form: 2015-2016")
    parser.add_argument('-w', '--week', type=str, action='store', required=True, help='Week of season: 1')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s' + PRED_GEN_VERSION)
    args = parser.parse_args()
     
    season, week = [args.season, args.week]
     
 
    print "Season: %s, Week: %s" % (season, week)
 
     
    ht_list = s.get_home_team_list_for_season_week(season, week)
    print ht_list
 
    for ht in ht_list:
        print ht