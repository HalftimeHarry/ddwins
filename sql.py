'''
ARI: Arizona Cardinals
ATL: Atlanta Falcons
BAL: Baltimore Ravens
BUF: Buffalo Bills
CAR: Carolina Panthers
CHI: Chicago Bears
CIN: Cincinnati Bengals
CLE: Cleveland Browns
DAL: Dallas Cowboys
DEN: Denver Broncos
DET: Detroit Lions
GB: Green Bay Packers
HOU: Houston Texans
IND: Indianapolis Colts
JAX: Jacksonville Jaguars
KC: Kansas City Chiefs
LAC: Los Angeles Chargers
LAR: Los Angeles Raiders
MIA: Miami Dolphins
MIN: Minnesota Vikings
NE: New England Patriots
NO: New Orleans Saints
NYG: New York Giants
NYJ: New York Jets
OAK: Oakland Raiders
PHI: Philadelphia Eagles
PIT: Pittsburgh Steelers
SD: San Diego Chargers
SEA: Seattle Seahawks
SF: San Francisco 49ers
STL: Saint Louis Rams
TB: Tampa Bay Buccaneers
TEN Tennessee Titans
WAS: Washington Redskins
 
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
        self.week = '5'
        self.season = '2017'
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
 
    def get_week_parameters(season, week):
        ''' Returns the start_season and start_week values
            based on 8 home games prior to the input season 
            and week arguments'''
        pass
 
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
 
    def get_home_team_list_for_season_week2(self, season, week):
        home_team_list = []
        #print "Week:", week
        #print "Season:", season
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
        cmd = 'SELECT Home_Team FROM ' + db + ' WHERE Season = "' + season + '" AND Week = "' + week + '";'
        #print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            row = row[0].encode('utf-8') # change unicode tuple into a string
            home_team_list.append(row)
 
        return home_team_list
 
    def get_home_team_list_for_season_week(self, season, week, end_date):
        home_team_list = []
        print "Week:", week
        print "Season:", season
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
        cmd = 'SELECT Home_Team FROM ' + db + ' WHERE Season = "' + season + '" AND Week = "' + week + '" AND Date <= "' + end_date + '";'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            row = row[0].encode('utf-8') # change unicode tuple into a string
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
 
    def get_average_total_of_prior_games_within_week_range(self, home_team, season, week):
        '''Returns an average for the total score for the previous number of games'''
         
        score_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        # cmd = 'SELECT Away_Team, Away_Score, Home_Team, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team  + '" AND Season <= "' + season + '" AND Week <= "' + week + '" ORDER BY Date DESC LIMIT 8;'
        cmd = 'SELECT Away_Score, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team  + '" AND Season = "' + season + '" AND Week <= "' + week + '" ORDER BY Date DESC;'
        #print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            #print row
            score_list.append(row)
         
        if int(season) > 2014:
            cmd = 'SELECT Away_Score, Home_Score FROM ' + db + ' WHERE Home_Team = "' + home_team  + '" AND Season = "' + str(int(season) - 1) + '" ORDER BY Date DESC;'
            #print cmd
            self.c.execute(cmd)
            rows = self.c.fetchall()
            for row in rows:
                #print row
                score_list.append(row)
 
        b = score_list
        #print "len:", len(score_list)
        score_list = score_list[0:8] # Only use the prior 8 games
        score_list_b = b[1:9] # Only use the prior 8 games and this will exclude the 1st score
    #    print score_list_b
         
        sum = 0
        for score in score_list_b:
            sum += score[0]
            sum += score[1]
 
        self.recent_total_result = score_list[0][0] + score_list[0][1]
#        print "Home team:", home_team
#        print "recent_total_result:", self.recent_total_result
        x = 8
        number_of_games = len(rows)
#        print "number_of_games:", number_of_games
#        print "test x", x use this when doing Football
        average = sum / float(x)
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
 
        cmd = 'SELECT Closing_O_U_Total FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Date <= "' + date + '";'
        #print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        #print "Rows:", rows
        for row in rows:
            ou_total = row[0]
            #print "ou_total:", ou_total
            return ou_total
 
    def get_closing_ou_total2(self, home_team, season, week):
        '''Read from games.db to get ou_total from a particular game
           and return that floating point number'''
            
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
           db = db[:-3]
 
        cmd = 'SELECT Closing_O_U_Total FROM ' + db + ' WHERE Home_Team = "' + home_team + '" AND Season = "' + season +  '" AND Week = "' + week + '";'
        #print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        #print "Rows:", rows
        for row in rows:
            ou_total = row[0]
            #print "ou_total:", ou_total
            return ou_total
 
    def get_targeted_game_details2(self, home_team, start_date, end_date):
        '''Read from games.db to get targeted game details
           and return all game details '''
            
        average = self.get_average_total_of_prior_games_within_week_range(home_team, start_date, end_date)
        ou_total = self.get_closing_ou_total(home_team, end_date)
        print "average:", average
        print "ou_total:", ou_total
        print "Average: %02.1f, Total OU: %02.1f" % (average, ou_total)
        # margin = ou_total - average
        margin = average - ou_total
        print "margin: %02.1f" % margin
        print "Predicted:",
        if margin > 0:
            print "over"
        elif margin < 0:
            print "under"
        else:
            print "Do not play"
 
        print "Actual total:", self.recent_total_result
        actual_margin = self.recent_total_result - margin
        if actual_margin < 0:
            print "Correct"
        elif actual_margin >= 0:
            print "Wrong"
 
    def get_targeted_game_details3(self, home_team, season, week):
        '''Read from games.db to get targeted game details
           and return all game details '''
            
        details = {}
 
        average = self.get_average_total_of_prior_games_within_week_range(home_team, season, week)
        details['average'] = average
        ou_total = self.get_closing_ou_total2(home_team, season, week)
        details['ou_total'] = ou_total
        #print "average:", average
        #print "ou_total:", ou_total
        #print "Average: %02.1f, Total OU: %02.1f" % (average, ou_total)
        # margin = ou_total - average
        margin = average - ou_total
        details['margin'] = margin
        details['actual_total'] =  self.recent_total_result
        details['actual_margin'] = self.recent_total_result - margin
        return details
 
    def set_number_of_prior_games(self):
        self.number_of_prior_games = raw_input(" Enter number of prior games: ")
        
    def get_teams_on_streak_list(self, season, week):
        game_list = []
        db = self.get_db_name()
        if db.endswith('.db'): # remove .db from database name
            db = db[:-3]
 
        cmd = 'SELECT Date, Away_Team, Away_Score, Home_Team, Home_Score, Closing_O_U_Total FROM ' + db + ' WHERE Season >= "' + season + '" AND Week <= "' + week + '" ORDER BY Date DESC;'
        print cmd
        self.c.execute(cmd)
        rows = self.c.fetchall()
        for row in rows:
            game_list.append(row)
 
        return game_list
        
    def get_targeted_game_streak_details(self, season, week):
        '''Read from games.db to get targeted game details
           and return all the streaks start with over and use DAL'''
           
        possible_streaks = self.get_teams_on_streak_list(season, week)
#        ou_total = self.get_closing_ou_total(home_team, end_date)
        print "Away Team", possible_streaks[2]
 
    def run(self):
        pass
 
if __name__ == '__main__':
     
    s = Sql('games.db')
    gl = s.get_game_list('games', '2015-2016', '7')
    for g in gl:
        print g
    s.clean_up