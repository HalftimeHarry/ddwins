# ddwins Smasher

Info About this project
This is the info content
This is the NFL Smasher 1.1


output sample data :

Season: 2017, Week: 15
Home team list for week: 15
['IND', 'DET', 'KAN', 'CLE', 'JAX', 'MIN', 'NOR', 'NYG', 'WAS', 'BUF', 'CAR', 'SEA', 'SFO', 'PIT', 'OAK', 'TAM']
Home team  Prediction  Predicted result  Actual total  Margin  Calc Avg  Vegas Line
   IND       Under       Correct Under        38        -0.5     40.0       40.5         Past Game
   DET       Over        Wrong Over           30        6.9      50.9       44.0         Past Game
   KAN       Under       Correct Under        43        -6.0     40.0       46.0         Past Game
   CLE       Under       Correct Under        37        -5.9     36.1       42.0         Past Game
   JAX       Over        Correct Over         52        6.5      45.5       39.0         Past Game
   MIN       Under       Correct Under        41        -3.0     39.0       42.0         Past Game
   NOR       Over        Correct Over         50        6.9      53.9       47.0         Past Game
   NYG       Under       Wrong Under          63        -4.6     35.4       40.0         Past Game
   WAS       Over        Wrong Over           35        1.2      44.2       43.0         Past Game
   BUF       Over        Correct Over         40        4.0      43.5       39.5         Past Game
   CAR       Under       Wrong Under          55        -1.9     45.1       47.0         Past Game
   SEA       Over        Correct Over         49        1.4      48.9       47.5         Past Game
   SFO       Over        Correct Over         48        1.4      45.4       44.0         Past Game
   PIT       Under       Correct Under        51        -2.6     50.4       53.0         Past Game
   OAK       Over        Wrong Over           37        1.6      47.6       46.0         Past Game
   TAM       Under       Correct Under        45        -14.6    33.4       48.0         Past Game
INSERT INTO game_results VALUES ('TAM','2017','15','5','6','3','2','0','0','0')
SELECT home_team, season, week, over_correct_cnt, under_correct_cnt, over_wrong_cnt, under_wrong_cnt, did_not_play_cnt, over_pushed_cnt, under_pushed_cnt FROM game_results;

Season: 2017
Week: 15
passed on 0
correct this week result 11
wrong this week result 5
pushed this week result 0

--------------------------
I need to set up an automatic versioning
and is code after building updating the game_results.db I feel the code is at
stage one of a many goals



____Predict more winners than loses

____Set up for other sports

____Use API for line feeds and update the scores automatically 

Steps to automated data from api's

Step 1

go to raw url and view the data via a browser

Step 2 

after you see the data you then write the code to "bring json data so we can use it in python

Step 3 

print out some data you want to filter in on

for example

____Be able to extract info and compare results via results.db

Vegas Streak          Totals           Teams Played        Harrys Ratings  Coaching        How Hary Did           What does Harry have

   LAR             Over Over Over       CLE  DEN  ATL      Like             No opinion     Correct Wrong Correct        Over
   DAL             Under Under Under    KAN  BUF  CAR      Dont Like        Do not like    Correct Wrong Wrong          Under
   PHI             Over Over Over       BAL  SEA  PIT      No Opinion       Nutrual        Correct Correct Correct      Under
   PHI             Over Over Over       SEA  PIT  LAC      No Opinion       Nutrual        Correct Correct Correct      Under