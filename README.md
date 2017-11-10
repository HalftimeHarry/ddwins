     _     _          _           
    | |   | |        (_)          
  __| | __| |_      ___ _ __  ___ 
 / _` |/ _` \ \ /\ / / | '_ \/ __|
| (_| | (_| |\ V  V /| | | | \__ \
 \__,_|\__,_| \_/\_/ |_|_| |_|___/
                                  
                                  

The date range compares might fail:
You probably will need to change the date format that 
is saved in the db.
1st check to see what date format is used in Sqlite3
then the past_games.txt should be modified. 

Also the WeekX, "Week X" fields should be changed to "Week_X" (underscore added)

You can change the default of 'Not Set' to something else in the sql.py file:
Ex. self.total = '45'


