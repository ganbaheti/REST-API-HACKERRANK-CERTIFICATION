//import two libraries : json and urllib3
  
import urllib3
import json
def getTotalGoals(team, year):
  goal=0
if team == "As Monaco":team = "AS Monaco"
    urls = ["https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1={1}&page={2}", 
    "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team2={1}&page={2}"]
    poolMan = urllib3.PoolManager()
    for url in urls:
        
        i = 1
        hasData = True
        while hasData != False:

            req = poolMan.request("GET", url.format(year, team, i))
            
            dec = json.loads(req.data.decode('utf-8'))['data']
            # print(dec)
            if dec != [] :
                for vals in dec:
                    
                    if vals['team1'] == team:
                        goal += int(vals['team1goals'])
                    if vals['team2'] == team:
                        goal += int(vals['team2goals'])
                i += 1
            else:
                hasData = False
    return goal
