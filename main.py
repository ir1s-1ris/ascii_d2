##api = d2api.APIWrapper('2BF19D0B6FA5E22C8364B7237B313F1B')

# Fetch last 100 very high skill games and filter out games that have leavers
import d2api

api = d2api.APIWrapper('2BF19D0B6FA5E22C8364B7237B313F1B')
vhs = api.get_match_history(skill = 3)

matches = [api.get_match_details(m['match_id']) for m in vhs['matches']]

# now filter out matches that have leavers
matches = [m for m in matches if not m.has_leavers()]

# number of matches that remain
print(len(matches))

# print the first match
print(matches[0])