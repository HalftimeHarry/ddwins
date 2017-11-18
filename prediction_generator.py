import sys
import sql
import datetime
import time
 
# Forget which one of these is the newest
import argparse
import optparse
 
 
'''
 
This program will output all the home team the predictions over/under for a week.
input arguments: Date to run. The result column only shows up if the date selected
was from the past.
 
Output:
    Home team  Prediction    margin      result
    ---------------------------------------------
       DAL         over        4          correct
       ATL         under       -5         wron
 
'''
 
if __name__ == '__main__':
     
    s = sql.Sql('games.db')
 
    ht_list = s.get_home_team_list_for_season_week("2016-2017", "3")
    print ht_list
 
    for ht in ht_list:
        print ht