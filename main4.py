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
    print('Неделя ' + str(datetime.date.today().isocalendar()[1]) +'. ' + str(monday.day) + ' ' + str(monday.strftime("%B")) + ' - ' + str(sunday.day) + ' ' + str(sunday.strftime("%B")) + '.')
    time2 = time.mktime(monday.timetuple())
    time3 = time2 - 604800
    api = d2api.APIWrapper(SteamApi)
    sql = """
    SELECT steamId FROM users WHERE user = ?
    """

    cursor.execute(sql,[(getpass.getuser())])
    temp = cursor.fetchall()[0][0]
    print(temp)
    print(type(temp))
    print(temp)

    sql = """
    SELECT * FROM match"""+str(temp)+""" ORDER BY start_time DESC
    """

    cursor.execute(sql)
    fetch = cursor.fetchall()
    print(fetch)
    time1 = fetch[0][7]
    print(fetch)
    print('TEST')
    # print(fetch['num_results'])
    tempMatches = []
    for row in cursor.execute("""
    SELECT rowid, * FROM match"""+str(temp)+""" ORDER BY start_time DESC
    """):
        if((row[8] < time2) & (row[8] > time3)):
            tempMatches.append(row)
    print(tempMatches)
    
    print(time3)
    print('На прошлой неделе..:')
    
    print('Количество игр: ' + str(len(tempMatches)))
    matchDetails = api.get_match_details(tempMatches[0][3])
    print(matchDetails)
    print(tempMatches[0])
    print(tempMatches[1])
    for match in tempMatches:
        print(match[4])
        matchDetails = api.get_match_details(match[4])
        #ищем лучшее кда
        topkda = []
        topkda.insert(0, matchDetails['players'][0]['hero']['hero_name'])
        topkda.insert(1, matchDetails['players'][0]['kills'])
        topkda.insert(2, matchDetails['players'][0]['deaths'])
        topkda.insert(3, matchDetails['players'][0]['assists'])
        temp = (matchDetails['players'][0]['kills'] + matchDetails['players'][0]['assists']) / matchDetails['players'][0]['deaths']
        topkda.insert
        for num in matchDetails['players'][0]['inventory']:
            print(num['item_name'])
        print(matchDetails['players'][0]['inventory'][0]['item_name'])
        print(type(matchDetails['players'][0]['inventory']))
        # print(matchDetails)
        print(type(matchDetails['players'][0]['hero']))
        print(type(topkda))
        
        for player in range(10):
            kda = (matchDetails['players'][player]['kills'] + matchDetails['players'][player]['assists']) / matchDetails['players'][player]['deaths']
            # if (kda > topkda):
                # topkda = 
            print(kda)
        print(type(matchDetails))

    print('Количество побед')

    

    if(time1 > time2):
        print('haha')
        # for number1 in range(fetch['num_results']):
        print('kek')
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
        print(fetch[0])
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

    print(sql)

    cursor.execute(sql, [(getpass.getuser())])
    temp = cursor.fetchall()
    print(type(temp))
    print(temp[0])
    print(type(temp[0]))
    print(temp[0][0])
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
