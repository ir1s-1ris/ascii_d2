#пробуем sqlite3

import getpass
import sqlite3
import sys
import datetime
import time
import d2api
from myData import SteamApi

def dbConnect():
    
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        print('Удачное соединение к ДБ.')
    except:
        print('Неудачное соединение к ДБ. Завершение программы.')
        sys.exit()

    try:
        cursor.execute("""
        CREATE TABLE if not exists users (
            id INTEGER PRIMARY KEY NOT NULL,
            user TEXT NOT NULL,
            regDate INTEGER,
            steamId INTEGER,
            players TEXT
        );
        """)
    except:
        print('Не получилось создать юзерс')
        
    
    return cursor, conn
    


def registration(user, cursor, conn):
    # timeNow = time.time()
    sql = "SELECT * FROM users WHERE user =?"
    cursor.execute(sql, [(user)])
    temp = cursor.fetchall()
    if (temp == []):
        sql = """
        INSERT INTO users (user, regDate)
        VALUES (?,?);
        """
        cursor.execute(sql, [(user), (time.time())])
        results = cursor.fetchall()
        print(results)
        conn.commit()
        print('Запись о вашем юзере добавлена!')
    else:
        print('Здраствуйте ', user,'.')

def weekReport(cursor, conn):
    today = datetime.datetime.today()
    monday = today - datetime.timedelta(datetime.datetime.weekday(today))
    sunday = today + datetime.timedelta(6 - datetime.datetime.weekday(today))
    lastMonday = monday - datetime.timedelta(days=7)
    lastSunday = sunday - datetime.timedelta(days=7)

    print('Неделя ' + str(datetime.date.today().isocalendar()[1]) +'. ' + str(monday.day) + ' ' + str(monday.strftime("%B")) + ' - ' + str(sunday.day) + ' ' + str(sunday.strftime("%B")) + '.')
    time2 = time.mktime(monday.timetuple())
    time3 = time2 - 604800
    api = d2api.APIWrapper(SteamApi)
    
    sql = """
    SELECT steamId FROM users WHERE user = ?
    """

    cursor.execute(sql,[(getpass.getuser())])
    temp = cursor.fetchall()[0][0]
    steamId32 = temp


    sql = """
    SELECT * FROM match"""+str(temp)+""" ORDER BY start_time DESC
    """

    cursor.execute(sql)
    fetch = cursor.fetchall()

    time1 = fetch[0][7]

    # print(fetch['num_results'])
    tempMatches = []
    for row in cursor.execute("""
    SELECT rowid, * FROM match"""+str(temp)+""" ORDER BY start_time DESC
    """):
        if((row[8] < time2) & (row[8] > time3)):
            tempMatches.append(row)
    matchDetails = api.get_match_details(tempMatches[0][3])
    
    print('На прошлой неделе: ' + str(datetime.date.today().isocalendar()[1] - 1) + '. ' + str(lastMonday.day) + ' ' + str(lastMonday.strftime("%B")) + ' - ' + str(lastSunday.day) + ' ' + str(lastSunday.strftime("%B")) + '.')
    # print('Неделя ' + str(datetime.date.today().isocalendar()[1]) +'. ' + str(monday.day) + ' ' + str(monday.strftime("%B")) + ' - ' + str(sunday.day) + ' ' + str(sunday.strftime("%B")) + '.')
    win = 0;
    for match in tempMatches:
        # print(match)
        matchDetails = api.get_match_details(match[4])
        wonside = matchDetails['winner']
        for player in range(10):
            if(matchDetails['players'][player]['steam_account']['id32'] == steamId32):
                if(wonside == matchDetails['players'][player]['side']):
                    win = win + 1
        
    if(win == 0):
        temp = 0
    else:
        temp = win/(len(tempMatches)/100)
    print('Количество игр: ' + str(len(tempMatches)) + '. ' + 'Win: ' + str(win) + '  Lose: ' + str(len(tempMatches) - win) + ' . WR: ' + str(temp))
    
    for match in tempMatches:
        matchDetails = api.get_match_details(match[4])
        #ищем лучшее кда
        topkda = []
        topkda.insert(0, matchDetails['players'][0]['hero']['hero_name'])
        topkda.insert(1, matchDetails['players'][0]['kills'])
        topkda.insert(2, matchDetails['players'][0]['deaths'])
        topkda.insert(3, matchDetails['players'][0]['assists'])
        temp = (matchDetails['players'][0]['kills'] + matchDetails['players'][0]['assists']) / matchDetails['players'][0]['deaths']
        topkda.insert(4, temp)
        temp = ''
        for num in matchDetails['players'][0]['inventory']:
            # print(num['item_name'])
            temp = temp + num['item_name'] + ';'
        topkda.insert(5, temp)
        topkda.insert(6, matchDetails['duration'])
        topkda.insert(7, matchDetails['start_time'])
        topkda.insert(8, matchDetails['match_id'])
        topkda.insert(9, matchDetails['winner'])

        mytopkda = []

        for player in range(10):
            kda = (matchDetails['players'][player]['kills'] + matchDetails['players'][player]['assists']) / matchDetails['players'][player]['deaths']
            if (matchDetails['players'][player]['steam_account']['id32'] == steamId32):
                if (mytopkda == []):
                    mytopkda.insert(1, matchDetails['players'][player]['kills'])
                    mytopkda.insert(0, matchDetails['players'][player]['hero']['hero_name'])
                    mytopkda.insert(2, matchDetails['players'][player]['deaths'])
                    mytopkda.insert(3, matchDetails['players'][player]['assists'])
                    temp = (matchDetails['players'][player]['kills'] + matchDetails['players'][player]['assists']) / matchDetails['players'][player]['deaths']
                    mytopkda.insert(4, temp)
                    temp = ''
                    for num in matchDetails['players'][player]['inventory']:
                        temp = temp + num['item_name'] + ';'
                    mytopkda.insert(5, temp)
                    mytopkda.insert(6, matchDetails['duration'])
                    mytopkda.insert(7, matchDetails['start_time'])
                    mytopkda.insert(8, matchDetails['match_id'])
                    mytopkda.insert(9, matchDetails['winner'])
                elif(kda > mytopkda[5]):
                    mytopkda.clear()
                    mytopkda.insert(1, matchDetails['players'][player]['kills'])
                    mytopkda.insert(0, matchDetails['players'][player]['hero']['hero_name'])
                    mytopkda.insert(2, matchDetails['players'][player]['deaths'])
                    mytopkda.insert(3, matchDetails['players'][player]['assists'])
                    temp = (matchDetails['players'][player]['kills'] + matchDetails['players'][player]['assists']) / matchDetails['players'][player]['deaths']
                    mytopkda.insert(4, temp)
                    temp = ''
                    for num in matchDetails['players'][player]['inventory']:
                        temp = temp + num['item_name'] + ';'
                    mytopkda.insert(5, temp)
                    mytopkda.insert(6, matchDetails['duration'])
                    mytopkda.insert(7, matchDetails['start_time'])
                    mytopkda.insert(8, matchDetails['match_id'])
                    mytopkda.insert(9, matchDetails['winner'])
            if (kda > topkda[4]):
                topkda.clear()
                topkda.insert(0, matchDetails['players'][player]['hero']['hero_name'])
                topkda.insert(1, matchDetails['players'][player]['kills'])
                topkda.insert(2, matchDetails['players'][player]['deaths'])
                topkda.insert(3, matchDetails['players'][player]['assists'])
                temp = (matchDetails['players'][player]['kills'] + matchDetails['players'][player]['assists']) / matchDetails['players'][player]['deaths']
                topkda.insert(4, temp)
                temp = ''
                for num in matchDetails['players'][player]['inventory']:
                    temp = temp + num['item_name'] + ';'
                topkda.insert(5, temp)
                topkda.insert(6, matchDetails['duration'])
                topkda.insert(7, matchDetails['start_time'])
                topkda.insert(8, matchDetails['match_id'])
                topkda.insert(9, matchDetails['winner'])



    print(topkda)
    print(mytopkda)
    print('Количество побед')

    

    if(time1 > time2):
        print('На этой неделе были игры')

    else:
        print('на данной неделе вы не играли никаких игр.')
    

    sql = """
    SELECT players FROM users WHERE user = ?
    """
    cursor.execute(sql,[(getpass.getuser())])
    temp = cursor.fetchall()[0][0]
    print(temp)

    tempStr = '{}{}'.format('match', temp)
    sql="""
    CREATE TABLE if not exists """ + tempStr + """ (
        id INTEGER PRIMARY KEY NOT NULL,
        dire_team_id INTEGER,
        lobby_type INTEGER,
        match_id INTEGER UNIQUE,
        match_seq_num INTEGER,
        players TEXT,
        radiant_team_id INTEGER,
        start_time INTEGER
    );
    """
    cursor.execute(sql)


    playerHistory = api.get_match_history(account_id = temp)
    # matchDetails = api.get_match_details()

    for number1 in range(playerHistory['num_results']):
        tempStr2 = ""
        for number2 in range(10):
            tempStr2 += "(" + str(playerHistory['matches'][number1]['players'][number2]['hero']) + ", " + str(playerHistory['matches'][number1]['players'][number2]['side']) + ", " + str(playerHistory['matches'][number1]['players'][number2]['steam_account']) + ");\n "

        sql="""
        INSERT OR IGNORE INTO """ + tempStr + """ (dire_team_id, lobby_type, match_id, match_seq_num, players, radiant_team_id, start_time)
        VALUES (""" + str(playerHistory['matches'][number1]['dire_team_id']) +""",""" + str(playerHistory['matches'][number1]['lobby_type']) +""",""" + str(playerHistory['matches'][number1]['match_id']) +""",""" +  str(playerHistory['matches'][number1]['match_seq_num']) +""", '""" + tempStr2 +"""',""" + str(playerHistory['matches'][number1]['radiant_team_id']) +""",""" + str(playerHistory['matches'][number1]['start_time']) + """);"""

        cursor.execute(sql)    
    
    
    

    sql = """
    SELECT * FROM match"""+str(temp)+""" ORDER BY start_time DESC
    """
    cursor.execute(sql)

    fetch = cursor.fetchall()
    playerIds = []
    playerIds.append(temp)
    playersInfo = api.get_player_summaries(account_ids = playerIds)
    print(playersInfo['players'][0]['personaname'])


    if(fetch[0][7]>time2):
        # print(fetch[0])
        print('На этой неделе у игрока не было')
    # for number in range(playerHistory['num_results'] - 1):
    #     print(fetch[number][7])

    
  
    conn.commit()


    


def userMenu(user, cursor, conn):

    sql = """
    SELECT steamId FROM users WHERE user = ?
    """
    cursor.execute(sql,[(user)])
    temp = cursor.fetchall()[0][0]

    if(temp == None):
        temp1 = input('Введите пожалуйста ваш steamId.')
        sql = """
        UPDATE users SET steamId = ? WHERE user = ?;
        """
        cursor.execute(sql, [(temp1),(user)])
        print(cursor.fetchall())
    api = d2api.APIWrapper(SteamApi)
    playerHistory = api.get_match_history(account_id = temp)

    tempStr = '{}{}'.format('match', temp)
    sql="""
    CREATE TABLE if not exists """ + tempStr + """ (
        id INTEGER PRIMARY KEY NOT NULL,
        dire_team_id INTEGER,
        lobby_type INTEGER,
        match_id INTEGER UNIQUE,
        match_seq_num INTEGER,
        players TEXT,
        radiant_team_id INTEGER,
        start_time INTEGER
    );
    """
    cursor.execute(sql)
    tempStr2 = ''

    

    for number1 in range(playerHistory['num_results']):
        tempStr2 = ""
        for number2 in range(10):
            tempStr2 += "(" + str(playerHistory['matches'][number1]['players'][number2]['hero']) + ", " + str(playerHistory['matches'][number1]['players'][number2]['side']) + ", " + str(playerHistory['matches'][number1]['players'][number2]['steam_account']) + ");\n "

        sql="""
        INSERT OR IGNORE INTO """ + tempStr + """ (dire_team_id, lobby_type, match_id, match_seq_num, players, radiant_team_id, start_time)
        VALUES (""" + str(playerHistory['matches'][number1]['dire_team_id']) +""",""" + str(playerHistory['matches'][number1]['lobby_type']) +""",""" + str(playerHistory['matches'][number1]['match_id']) +""",""" +  str(playerHistory['matches'][number1]['match_seq_num']) +""", '""" + tempStr2 +"""',""" + str(playerHistory['matches'][number1]['radiant_team_id']) +""",""" + str(playerHistory['matches'][number1]['start_time']) + """);"""

        cursor.execute(sql)
    

    sql = """
    SELECT players FROM users WHERE user = """ + getpass.getuser() + """
    """

    sql =  """
    SELECT players FROM users WHERE user = ?
    """


    cursor.execute(sql, [(getpass.getuser())])
    temp = cursor.fetchall()
    if(temp[0][0] == None):
        print('Ваш список Players пуст')
        ans = input('Хотите добавить игрока?(Y/N)')
        if(ans == 'y' or 'Y'):
            temp = input('Введите SteamId игрока: ')
            sql = """
            UPDATE users SET players = ? WHERE user = ?;
            """
            cursor.execute(sql,[(temp),getpass.getuser()])
            print(cursor.fetchall())
    

    conn.commit()

    weekReport(cursor, conn)



def main():
    cursor, conn = dbConnect()
    registration(getpass.getuser(), cursor, conn)
#    proverkaBazi(cursor, conn)
    userMenu(getpass.getuser(), cursor, conn)


main()
