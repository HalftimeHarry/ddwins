"""
====================================================================

   Copyright (c) 2018-2019 Smasher Solutions, Inc.
      ALL RIGHTS RESERVED.

   C O N F I D E N T I A L    I N F O R M A T I O N

      This file contains confidential, proprietary and unpublished
      source code solely owned by Smasher Media Solutions, Inc.

   sports_data.py - gets all Sporting Events for today 

   Scrapes data from the api from : api.sportradar.us

   nfl - Current NFL data
   nba - Current NBA data
   more - all others to do
   
   Relace the above info for the sports data

http://api.sportradar.us/football-t1/american/en/schedules/2018-01-14/results.json?api_key=6ps4fbsxgmqbapmcs687vsmz
http://api.sportradar.us/football-t1/american/en/shedules/2018-01-14/results.json?api_key=6ps4fbsxgmqbapmcs687vsmz
====================================================================
"""
import requests
import json

SPORTRADAR_URL = "http://api.sportradar.us"
API_KEY = "6ps4fbsxgmqbapmcs687vsmz"
SPORT = "football-t1/american/"
LANG = 'en'
WEEK = "2018-01-14"
'''
conn = http.client.HTTPSConnection("api.sportradar.us")

key = 'ymtkrbbkec6q2hcfqegv8mqc'

sport = "/nfl-ot2/stream/events/subscribe?"
# api_key={your_api_key}&status=inprogress&match=sd:match:673b459c-7506-4c11-9273-1b9502537f1d")

res = conn.getresponse()
data = res.read()
&status=inprogress&match=sd:match:673b459c-7506-4c11-9273-1b9502537f1d")
'''
sport = "/nfl-ot2/stream/events/subscribe"

cmd = SPORTRADAR_URL + '/' + SPORT + LANG + '/' + 'schedules/' + WEEK + '/results.json?api_key=' + API_KEY
print '\n' + cmd
    
#s = sign.capitalize() + ':&nbsp;&nbsp;'
r = requests.get(cmd)
h = r.text
print h

oj = json.dumps(r.json, indent=4)
print oj
