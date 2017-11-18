'''
games.db columns
----------------
Season,
Week,
Date,
Home_Team,
Home_Score,
Home_Opening_Spread,
Home_Closing_Spread,
Home_Opening_ML,
Home_Opening_ML_Decimal,
Home_Closing_ML,
Home_Closing_ML_decimal,
Away_Team,
Away_Score,
Away_Opening_Spread,
Away_Closing_Spread,
Away_Opening_ML,
Away_Opening_ML_Decimal,
Away_Closing_ML,
Away_Closing_ML_decimal,
Opening_O_U_Total,
Closing_O_U_Total
 
'''
 
import sys
import csv
import sqlite3
 
 
class Sql:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.db = db
        self.home_team = 'DAL'
        self.away_team = 'Not set'
        self.week = 'Not set'
        self.season = 'Not set'
        self.venue = 'Not set'
        self.start_date = '2015-11-01'
        self.end_date = '2016-10-30'
        self.total = 'Not set'
        self.closing_spred = 'Not set'
        self.closing_total = 'Not set'
        self.number_of_prior_games = '8'
        self.recent_total_result = ''
 
    def clean_up(self):
        self.conn.commit()
        self.conn.close()
 
    def get_db_name(self):
        return self.db
 
    def get_game_list(self, db, season, week):
        game_list = []
        print "Week:", week
        cmd = 'SELECT * FROM ' + db + ' WHERE Season = "' + season + '" AND Week = "' + week + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            game_list.append(row)
 
        return game_list
 
    def get_home_team_list_for_season_week(self, season, week):
        home_team_list = []
        print "Week:", week
        print "Season:", season
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
        cmd = 'SELECT Home_Team FROM ' + db + ' WHERE Season = "' + season + '" AND Week = "' + week + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            home_team_list.append(row)
 
        return home_team_list
 
    def get_games_from_home_team_between_date_range(self, home_team, start_date, end_date):
        home_game_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        cmd = 'SELECT Away_Team, Away_Score, Home_Team, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Date >= "' + start_date + '" AND Date <= "' + end_date + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            home_game_list.append(row)
 
        return home_game_list
 
    def get_average_total_of_prior_games_within_date_range(self, home_team, start_date, end_date):
        '''Returns an average for the total score for the previous number of games'''
         
        score_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        cmd = 'SELECT Away_Score, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team  + '" AND Date >= "' + start_date + '" AND Date <= "' + end_date + '" ORDER BY Date DESC;'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            score_list.append(row)
         
        print score_list
        sum = 0
        for score in score_list:
            sum += score[0]
            sum += score[1]
         
        self.recent_total_result = score_list[0][0] + score_list[0][1]
        print "recent_total_result:", self.recent_total_result
 
        number_of_games = len(rows)
        print "number of games:", number_of_games
        average = sum / float(number_of_games)
        return average
 
    # def get_last_number_of_games_from_home_team_within_date_range(self, home_team, number_of_prior_games, start_date, end_date):
    def get_last_number_of_games_from_home_team_within_date_range(self, home_team, start_date, end_date):
        '''Returns the last number of games from the home team'''
         
        game_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        #cmd = 'SELECT Date, Away_Team, Away_Score, Home_Team, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Date >= "' + start_date + '" AND Date <= "' + end_date + '" + ORDER BY Date DESC LIMIT "' + number_of_prior_games + '" ;'
        cmd = 'SELECT Date, Away_Team, Away_Score, Home_Team, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Date >= "' + start_date + '" AND Date <= "' + end_date + '" ORDER BY Date DESC;'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            game_list.append(row)
         
        return game_list
 
    def get_teams_scores_ou_total_within_time_range(self, start_date, end_date):
        game_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        cmd = 'SELECT Date, Away_Team, Away_Score, Home_Team, Home_Score, Closing_O_U_Total FROM ' + db + ' WHERE Date >= "' + start_date + '" AND Date <= "' + end_date + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            game_list.append(row)
 
        return game_list
 
    def set_teams(self):
        self.home_team = raw_input(" Enter home team: ")
        self.away_team = raw_input(" Enter away team: ")
        self.venue = raw_input(" Enter venue: ")
        return(self.home_team, self.away_team, self.venue)
 
    def set_home_team(self):
        self.home_team = raw_input(" Enter home team: ")
        return(self.home_team)
        
    def set_season (self):
        self.season = raw_input(" Enter Season Example 2016-2017: ")
        return(self.season)
        
    def set_week (self):
        self.week = raw_input(" Enter Week Example 1: ")
        return(self.week)
 
    def set_date_range(self):
        self.start_date = raw_input(" Enter start date (YYYY-MM-DD): ")
        self.end_date = raw_input(" Enter end date (YYYY-MM-DD): ")
 
    def set_total(self):
        self.total = raw_input(" Enter total: ")
 
    def set_closing_spred(self):
        self.closing_spred = raw_input(" Enter closing spred: ")
 
    def set_closing_ou_total(self):
        self.closing_total = raw_input(" Enter closing total: ")
 
    def get_closing_ou_total(self, home_team, date):
        '''Read from games.db to get ou_total from a particular game
           and return that floating point number'''
            
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
           db = db[:-3]
 
        cmd = 'SELECT Closing_O_U_Total FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Date = "' + date + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            ou_total = row[0]
            print "Vegas Total was:", ou_total
            return ou_total
 
    def get_targeted_game_details(self, home_team, start_date, end_date):
        '''Read from games.db to get targeted game details
           and return all game details '''
            
        average = self.get_average_total_of_prior_games_within_date_range(home_team, start_date, end_date)
        total_ou = self.get_closing_ou_total(home_team, end_date)
        print "Average: %02.1f, Vegas Total: %02.1f" % (average, total_ou)
        # margin = total_ou - average
        margin = average - total_ou
        print "margin: %02.1f" % margin
        print "Prediction was:",
        if margin > 0:
            print "over"
        elif margin < 0:
            print "under"
        else:
            print "Do not play"
 
        print "Actual total:", self.recent_total_result
        actual_margin = self.recent_total_result - margin
        print "Prediction result:",
        if margin > 0 and actual_margin > total_ou:
            print "Correct Over"
        if margin < 0 and actual_margin < total_ou:
            print "Correct Under"
        if margin > 0 and actual_margin < total_ou:
            print "Wrong Over"
        if margin < 0 and actual_margin > total_ou:
            print "Wrong Under"
        if margin > 0 and actual_margin == total_ou:
            print "Pushed Over"
        if margin > 0 and actual_margin == total_ou:
            print "Pushed Under"
        elif margin > 0 and actual_margin == total_ou:
            print "Did not play the game"
            
    def set_number_of_prior_games(self):
        self.number_of_prior_games = raw_input(" Enter number of prior games: ")
 
    def run(self):
        pass
 
if __name__ == '__main__':
     
    s = Sql('games.db')
    gl = s.get_game_list('games', '2015-2016', '7')
    for g in gl:
        print g
    s.clean_up