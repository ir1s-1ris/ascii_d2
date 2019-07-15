# Fetch last 100 very high skill games and filter out games that have leavers
import d2api
from myData import SteamApi

#print('Write steam_id: ')
#playerId = int(input()) can write
playerId = 78312288

api = d2api.APIWrapper(SteamApi)
vhs = api.get_match_history(account_id = playerId)

#matches = [api.get_match_details(m['match_id']) for m in vhs['matches']]
print(type(vhs))
print(type(vhs['matches']))
listMatches = vhs['matches'][0]

print(type(listMatches))
print(listMatches['match_id'])
lastMatchId = listMatches['match_id']

print(api.get_match_details(lastMatchId)['winner'])