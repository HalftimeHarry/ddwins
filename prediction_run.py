import os
 
if __name__ == '__main__':
     
    for season in [2015, 2016]:
        print "\nSeason:", season
        for week in range(1, 18):
             
            #print season, week
            os.system("python prediction_generator.py " + '-s ' + str(season) + ' -w ' + str(week))