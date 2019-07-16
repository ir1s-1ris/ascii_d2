# Fetch last 100 very high skill games and filter out games that have leavers
import d2api
import time
import datetime
from myData import SteamApi

#pre init variable
playerId = 78312288

#connect to api, and player
api = d2api.APIWrapper(SteamApi)
playerHistory = api.get_match_history(account_id = playerId)

#checkweek and time
print(time.strftime("%U", time.localtime(time.time())))
weekNow = time.strftime("%U", time.localtime(time.time()))
print(type(weekNow))

# get frequency of heroes played in the latest 100 games
playerItems= {}

#init matches
#istMatches = [api.get_match_details(m['match_id']) for m in playerHistory['matches']]

#print(type(listMatches))

count = 0

#loop init
#for match in playerHistory['matches']:
for match in playerHistory['matches']:
	
	#print(type(match))
	weekGame = time.strftime("%U", time.localtime(api.get_match_details(match['match_id'])['start_time']))
	#print(type(weekGame))
	if int(weekGame) >= int(weekNow)-1:
		if int(weekGame) == int(weekNow)-1:
			count += 1
			print('Game on last week: ', count)
	else:
		break
	#match = playerHistory['matches'][m]
	#matchId= match['match_id']
	#weekGame = time.strftime("%U", time.localtime(api.get_match_details(lastMatchId)['start_time']))
	#api.get_match_details(lastMatchId)['start_time']
	#if weekGame == weekNow-1S
		




#matches = [m for m in matches if not m.has_leavers()]
#print(type(vhs))
#print(type(vhs['matches']))
listMatches = playerHistory['matches'][0]

#print(type(listMatches))
print(listMatches['match_id'])
lastMatchId = listMatches['match_id']

print(api.get_match_details(lastMatchId)['winner'])
#print(api.get_match_details(lastMatchId)['start_time'])

duration = api.get_match_details(lastMatchId)['duration']
#print(time.strftime("%d %H:%M:%S ", time.localtime(startMatchTime)))


print(duration ," sec or ", duration//60 ,"min")

