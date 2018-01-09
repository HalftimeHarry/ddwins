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



====================================================================
"""
import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

key = 'ymtkrbbkec6q2hcfqegv8mqc'

conn.request("GET", "/nfl-ot2/stream/events/subscribe?api_key={your_api_key}&status=inprogress&match=sd:match:673b459c-7506-4c11-9273-1b9502537f1d")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
