# Fetch last 100 very high skill games and filter out games that have leavers
import d2api

api = d2api.APIWrapper('2BF19D0B6FA5E22C8364B7237B313F1B')
vhs = api.get_match_history(account_id = 78312288)

#matches = [api.get_match_details(m['match_id']) for m in vhs['matches']]
print(type(vhs))
print(type(vhs['matches']))
listMatches = vhs['matches'][0]

print(type(listMatches))
print(listMatches['match_id'])