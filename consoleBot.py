import d2api
import psycopg2
from myData import steamApi, defaultPlayerId


# надо всё передалть на sqllite3
def checkDbPlayer(steamId):
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("i am unable to connect to the database")

	cursor = conn.cursor()
	
	cursor.execute("SELECT personaname FROM test2 WHERE steamaccount32 = %s;", (steamId,))
	
	try:
		dbbuff = cursor.fetchall()
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

def userMenu():

	print('1. Добавление к отслеживаемому (в разработке)')

	choice = input()
	if choice == '1':
		print('---Добавление к отслеживаемому. --- \nВведите steamId:')
		steamId = input()
		
		try:
			baseCheck = checkDbPlayer(steamId)
		except:
			baseCheck = None;
		if baseCheck == None: 
			addPlayer(steamId)
		else:
			print("Есть совпадение:", baseCheck)



def addPlayer(steamId):
	try:
		conn = psycopg2.connect(dbname='sammy1', password='admin', user='postgres', host='localhost')
	except:
		print("i am unable to connect to the database")

	api = d2api.APIWrapper(steamApi)
	cursor = conn.cursor()
	#create list var for parse playerId
	#api = d2api.APIWrapper(steamApi)

	#variables
	playerId = steamId
	playerInfo = []	
	playerIds = []
	playerIds.append(playerId)
	playersInfo = api.get_player_summaries(account_ids = playerIds)

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

	playerInfo.clear()

	userMenu()



#функция ожидания ввода в меню пользователя
def main():
	userMenu()


main()