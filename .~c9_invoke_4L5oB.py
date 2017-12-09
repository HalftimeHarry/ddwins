import sys
import sql
import datetime
import time
import argparse
 
PRED_GEN_VERSION = '0.5'
 
 
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
 
 
def get_week_parameters(season, week):
    ''' Returns the start_season, start_week values
        based on the input season and week arguments.
        You probably need to do 2 db queries. 1 for each season
        then join the results.
        
        If week is 8, then pick all games in current season and last
        8 games from previous season.
        
        '''
        
        
    start_season = season
    if week >= 2:
        start_week = week - 2
    else:
        start_week = week + 2
        if season == '2016':
            start_season = '2015'
        elif season == '2015':
            start_season = '2014'
    return(start_season, start_week)
 
 
 
if __name__ == '__main__':
     
    s = sql.Sql('games.db')
 
    parser = argparse.ArgumentParser(description='Predicts sports outcomes.', prog='prediction_generator.py')
     
    parser.add_argument('-s', '--season', type=str, action='store', required=True, help="season in the form: 2015-2016")
    parser.add_argument('-w', '--week', type=str, action='store', required=True, help='Week of season: 1')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s' + PRED_GEN_VERSION)
    args = parser.parse_args()
     
    season, week = [args.season, args.week]
     
 
    print "Season: %s, Week: %s" % (season, week)
 
     
    home_team_list = s.get_home_team_list_for_season_week2(season, week)
    print home_team_list

    for home_team in home_team_list:
        start_season, start_week = get_week_parameters(season, int(week))
        print "DE:", home_team
        targeted_game = s.get_targeted_game_details2(home_team, start_week, week)
        print "Targeted game:", targeted_game