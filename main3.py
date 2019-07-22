# nachalo raboti

import d2api
import psycopg2
from myData import SteamApi

#connect to api, and player
api = d2api.APIWrapper(SteamApi)

#variables
playerId = 78312288
playerInfo = []	
playerIds = []
playerIds.append(playerId)
playersInfo = api.get_player_summaries(account_ids = playerIds)

def checkPlayerInDb(SteamId):
	#проверить есть ли этот персонаж уже  вбазе 1, если нету то создать ему новую базу для матчей
	#проверить дату последней игры в бд и спарсить последнюю игру(проверка актуальности базы) -> если она оказывается не последней то добавлять игры до момента пока первоначально *последняя* айди матча не совпадёт

def playerGamesInfo1(SteamId):
	#алгоритм который выводит информацию из бд, по всем матчам которые были сыграны на данной неделе. вывод информации в виде вывода табличных данных. пока что.

def playerGamesInfo2(SteamId):
	#алгоритм который выводит информацию из бд, по всем матчам которые были сыграны на данной неделе. вывод информации в виде вывода табличных данных. пока что.




'''
def createTest2():
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("i am unable to connect to the database")

	cursor = conn.cursor()

	try:
		cursor.execute("CREATE TABLE test2 ( id serial, avatar char(150), lastlogoff int, personaname char(30), personastate char(15), profileurl char(60), steamaccount32 numeric(8), steamaccount64 numeric(17), steamid numeric(17), timecreated int);")
	except:
		print("I can't drop our test DATABASE")

	conn.commit()
	conn.close()
	cursor.close()

def addPlayer():
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("i am unable to connect to the database")

	cursor = conn.cursor()

	
	#create list var for parse playerId
	

	playerInfo.append(playersInfo['players'][0]['avatarmedium'])
	playerInfo.append(playersInfo['players'][0]['lastlogoff'])
	playerInfo.append(playersInfo['players'][0]['personaname'])
	playerInfo.append(playersInfo['players'][0]['personastate'])
	playerInfo.append(playersInfo['players'][0]['profileurl'])
	playerInfo.append(playersInfo['players'][0]['steam_account']['id32'])
	playerInfo.append(playersInfo['players'][0]['steam_account']['id64'])
	playerInfo.append(playersInfo['players'][0]['steamid'])
	playerInfo.append(playersInfo['players'][0]['timecreated'])

	try:
		cursor.execute("INSERT INTO test2 (avatar, lastlogoff, personaname, personastate, profileurl, steamaccount32, steamaccount64, steamid, timecreated) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(playerInfo[0],playerInfo[1],playerInfo[2],playerInfo[3],playerInfo[4],playerInfo[5],playerInfo[6],playerInfo[7],playerInfo[8]))
	except:
		print(cursor.fetchall())
		print("Insert into been failed ;c")

	conn.commit()
	conn.close()
	cursor.close()

def checkDbPlayer(steamId):
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("i am unable to connect to the database")

	cursor = conn.cursor()
	
	cursor.execute("SELECT personaname FROM test2 WHERE steamaccount32 = %s;", (steamId,))
	
	try:
		dbbuff = cursor.fetchall()
		print(dbbuff)
		print(type(dbbuff))
	except:
		print('error fetchall()')
	
	conn.commit()
	conn.close()
	cursor.close()

	if isinstance(dbbuff, list):
		dbbuff = dbbuff[0]
		dbbuff = dbbuff[0]
		return dbbuff
	else:
		return None



print(checkDbPlayer(playerId))

'''

'''
	try:
		cursor.execute("SELECT personaname FROM test2 WHERE profileurl = %s;", steamId)
		print(cursor.fetchall())
		return true
	except:
		print(cursor.fetchall())
		print("checkDbPlayer - error")
		return false
#cursor.execute("UPDATE test2 set id = '2' WHERE id = '3';")
#print(type(dbbuff))
	#print(dbbuff)
'''
'''

def dbconn():
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("dbconn() is unable to connect to the database")
	cursor = conn.cursor()

def dbclose():
	conn.commit()
	conn.close()
	cursor.close()


#dbconn()

try:
	dbconn()

	cursor.execute("""INSERT INTO test (num,data)
	VALUES
	(1,'beka'),
	(2,'val'),
	(3,'sason'),
	 """)
	dbclose()
except:
	print("I can't insert in db!")

#dbclose()

def fetchAll():
	try:
		print(cursor.fetchall())
	except:
		print("No results to fetch, or other error.")

def addPlayer():
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		fetchAll()
		print("i am unable to connect to the database")
	
	cursor = conn.cursor()

	try:
		cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar(30));")
	except:
		fetchAll()
		print("I can't drop our test DATABASE")

	fetchAll()

	conn.commit()
	conn.close()
	cursor.close()



	#cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar(30));")

addPlayer()
'''