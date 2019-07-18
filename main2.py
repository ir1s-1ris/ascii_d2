"""

import d2api
from d2api.src import entities
from myData import SteamApi

api = d2api.APIWrapper(SteamApi)

#pre init variable
playerId = 78312288

# fetch latest matches
match_history = api.get_match_history(account_id = playerId)

# get frequency of heroes played in the latest 100 games
heroes = {}

for match in match_history['matches']:
    for player in match['players']:
        hero_id = player['hero']['hero_id']
        if not hero_id in heroes:
            heroes[hero_id] = 0
        heroes[hero_id] += 1

# print hero frequency by name
for hero_id, freq in heroes.items():
    print(entities.Hero(hero_id)['hero_name'], freq)
"""

"""
{'avatar': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f5/f52b28a0b240d1ee68225cb66d6b4a9b7cf858ae.jpg',
 'avatarfull': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f5/f52b28a0b240d1ee68225cb66d6b4a9b7cf858ae_full.jpg',
 'avatarmedium': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f5/f52b28a0b240d1ee68225cb66d6b4a9b7cf858ae_medium.jpg',
 'commentpermission': 1,
 'communityvisibility': 'friends_of_friends',
 'lastlogoff': 1563317681,
 'personaname': 'xXx_Kiler2008_xXx',
 'personastate': 'offline',
 'personastateflags': 0,
 'primaryclanid': '103582791438125171',
 'profilestate': 1,
 'profileurl': 'https://steamcommunity.com/id/MASYAPROHOR/',
 'steam_account': SteamAccount(account_id = 78312288),
 'steamid': '76561198038578016',
 'timecreated': 1298477064}
"""
import d2api
import psycopg2
from contextlib import closing
from myData import SteamApi

#variables
playerId = 78312288

#connect to api, and player
api = d2api.APIWrapper(SteamApi)

#create list var for parse playerId
playerIds = []
playerIds.append(playerId)

#create var for playerinfo and addPlayer().
playerInfo = []


conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
cursor = conn.cursor()
print('ALL RIGHT')



'''
with closing(psycopg2.connect("dbname=postgres user=postgres host=localhost")) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM myplayers LIMIT 5')
        for row in cursor:
            print(row)
'''

def dbconn():
	conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
	cursor = conn.cursor()
	print('Success connected to DB')
	cursor.execute("CREATE TABLE customers( id serial, avatar char(50), lastlogoff int, personaname char(30), personastate char(15), profileurl char(60), steamaccount32 numeric(8), steamaccount64 numeric(17), steamid numeric(17), timecreated int);")
	results = cursor.fetchall()
	print(results)


78312288


def addPlayer():
	dbconn()
	playersInfo = api.get_player_summaries(account_ids = playerIds)
	#print(type(playersInfo['players'][0]['steam_account']['id32']))
	playerInfo.append(playersInfo['players'][0]['avatarmedium'])
	playerInfo.append(playersInfo['players'][0]['lastlogoff'])
	playerInfo.append(playersInfo['players'][0]['personaname'])
	playerInfo.append(playersInfo['players'][0]['personastate'])
	playerInfo.append(playersInfo['players'][0]['steam_account']['id32'])
	playerInfo.append(playersInfo['players'][0]['steam_account']['id64'])
	playerInfo.append(playersInfo['players'][0]['steamid'])
	playerInfo.append(playersInfo['players'][0]['timecreated'])
	print(playerInfo[1])
	
	cursor.execute("INSERT INTO myplayers (avatarmd, lastlogoff, personaname, personastate, steamaccount32, steamaccount64, steamid, timecreated) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",(playerInfo[0],playerInfo[1],playerInfo[2],playerInfo[3],playerInfo[4],playerInfo[5],playerInfo[6],playerInfo[7]))
	#records = cursor.fetchall()
	print(cursor.fetchall())
	return print('Add player - success')
	

#addPlayer()

"""
                                    Table "public.myplayers"
     Column     |      Type      | Collation | Nullable |                Default                
----------------+----------------+-----------+----------+---------------------------------------
 id             | integer        |           | not null | nextval('myplayers_id_seq'::regclass)
 avatarmd       | character(150) |           |          | 
 lastlogoff     | integer        |           |          | 
 personaname    | character(30)  |           |          | 
 personastate   | character(15)  |           |          | 
 steamaccount32 | numeric(8,0)   |           |          | 
 steamaccount64 | numeric(17,0)  |           |          | 
 steamid        | numeric(17,0)  |           |          | 
 timecreated    | integer        |           |          | 

"""
'''
	for number in range(8):
	playerInfo.append('')

	playerInfo.append('avatarMd!!!')
	playerInfo.append(111)
	playerInfo.append('personaname!!!')
	playerInfo.append('personastate!!!')
	playerinfo.append('')
'''

listPlayerInfo = [
	('avatarmd'),
	(111),
	('personaname!!!'),
	('personastate!!'),
	(12345678),
	(12345678901234567),
	(12345678901234567),
	(2000),
]

def createtable():
	dbconn()
	cursor.execute("CREATE TABLE customers( id serial, avatar char(50), lastlogoff int, personaname char(30), personastate char(15), profileurl char(60), steamaccount32 numeric(8), steamaccount64 numeric(17), steamid numeric(17), timecreated int);")
	results = cursor.fetchall()
	print(results)

createtable()

def checkbd():
	conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
	cursor = conn.cursor()
	#cursor.execute("CREATE TABLE tableTest(id SERIAL PRIMARY KEY, firstName CHARACTER(30));")
	playerInfo.append('avatarMd!!!')
	playerInfo.append(111)
	playerInfo.append('personaname!!!')
	playerInfo.append('personastate!!!')
	playerInfo.append('12345678')
	playerInfo.append('12345678901234567')
	playerInfo.append('12345678901234567')
	playerInfo.append('2000')
	#cursor.execute("INSERT INTO myplayers VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",(playerInfo[0],playerInfo[1],playerInfo[2],playerInfo[3],playerInfo[4],playerInfo[5],playerInfo[6],playerInfo[7]))

	#cursor.execute("INSERT INTO myplayers VALUES (Null, 'avatarMD', 111, 'personanem!!!', 'personastate!!!', 12345678, 123456781234567, 1234567891234567, 2000);")

	cursour.executemany("INSERT INTO myplayers ")
	cursor.execute("SELECT * FROM myplayers")
	results = cursor.fetchall()
	print(resulsts)

	#INSERT INTO myplayers VALUES ('avatarMD', 111, 'personanem!!!', 'personastate!!!', 12345678, 123456781234567, 1234567891234567, 2000);



	'''
	cursor.execute('INSERT INTO tabletest (avatarmd, lastlogoff, personaname, personastate, steamaccount32, steamaccount64, steamid, timecreated) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);',(playerInfo[0],playerInfo[1],playerInfo[2],playerInfo[3],playerInfo[4],playerInfo[5],playerInfo[6],playerInfo[7]))


	cursor.execute('SELECT * FROM myplayers')
	print(cursor.fetchall())
	'''
#checkbd()


playersInfo = api.get_player_summaries(account_ids = playerIds)
print(type(playersInfo['players'][0]['avatarmedium']))
print(playersInfo['players'][0]['avatarmedium'])
#print(type(playersInfo['players'][0]['steam_account']['id32']))

#

#print(playersInfo['players'][0]['steamid']) - parse steamId



'''
import psycopg2
https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f5/f52b28a0b240d1ee68225cb66d6b4a9b7cf858ae_full.jpg
INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2014-04-28');
https://steamcommunity.com/id/MASYAPROHOR/

INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2014-04-28');



try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")
xXx_Kiler2008_xXx

import psycopg2

conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
'''