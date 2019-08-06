#пробуем sqlite3

import getpass
import sqlite3
import sys
import time
import d2api
from myData import SteamApi

# try:
#     cursor.execute("""Create table albums
#                 (title text, artist text, release_date text, publisher text, media_type text)
#                 """)
#     print('БД создалась')
# except: 
#     print('БД не создалась')

# cursor.execute("""INSERT INTO albums
#                 VALUES ('GLOW', 'Andy Hunter', '7/24/2012',
#                 'Xplore Records', 'MP3')"""
#                 )

# conn.commit()

# albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
#           ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
#           ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
#           ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

# cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)

# conn.commit() 

# sql = """
# SELECT * FROM albums WHERE artist = ?
# """

# print("Here's a listing of all the records in the table:")
# for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
#     print(row)

# print("Results from a like query:")
# sql = "SELECT * FROM albums WHERE title like 'The%'"
# cursor.execute(sql)

# print(cursor.fetchall())


# cursor.execute(sql, [("Red")])
# print(cursor.fetchall())
# conn.commit()


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
    print(temp)
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

# def proverkaBazi(cursor, conn):
#     sql = """
#     INSERT INTO users
#     VALUES (NULL, 'hhash', 12345);
#     """
#     cursor.execute(sql)
#     conn.commit()

def userMenu(user, cursor, conn):
    # sql = """
    # SELECT count(*) FROM sqlite_master WHERE type='table' AND name =?;
    # """
    # cursor.execute(sql,[(user)])
    # temp = cursor.fetchall()[0][0]
    # # temp = temp[0][0]
    # print(type(temp))
    # print(temp)
    # print('')
    # if(temp == 0):
    #     sql="""
    #     CREATE TABLE if not exists ? (
    #     id INTEGER PRIMARY KEY NOT NULL,
    #     user TEXT NOT NULL,
    #     regDate INTEGER
    #     );
    #     """

    sql = """
    SELECT steamId FROM users WHERE user = ?
    """
    cursor.execute(sql,[(user)])
    temp = cursor.fetchall()[0][0]
    print(type(temp))
    print(temp)
    

    if(temp == None):
        temp1 = input('Введите пожалуйста ваш steamId.')
        sql = """
        UPDATE users SET steamId = ? WHERE user = ?;
        """
        cursor.execute(sql, [(temp1),(user)])
        print(cursor.fetchall())

    api = d2api.APIWrapper(SteamApi)
    playerHistory = api.get_match_history(account_id = temp)
    print(type(playerHistory))
    # print(playerHistory)
    print(playerHistory['matches'][0]['dire_team_id'])


    print(temp)
    tempStr = '{}{}'.format('match', temp)
    print(tempStr)
    
    
    sql="""
    CREATE TABLE if not exists """ + tempStr + """ (
        id INTEGER PRIMARY KEY NOT NULL,
        dire_team_id INTEGER,
        lobby_type INTEGER,
        match_id INTEGER,
        match_seq_num INTEGER,
        players TEXT,
        radiant_team_id INTEGER,
        start_time INTEGER
    );
    """
    cursor.execute(sql)

    print(type(playerHistory['matches'][0]['players']))
    # print(playerHistory['matches'][0]['players'])
    print(playerHistory['matches'][0]['players'][0]['hero'])
    print(type(playerHistory['matches'][0]['players'][0]['side']))
    hero = playerHistory['matches'][0]['players'][0]['hero']
    print(str(playerHistory['matches'][0]['players'][0]['side']))

    print(type(str(hero)))
    
    tempStr2 = ''
    
    print(playerHistory['num_results'])

    for number in range(10):
        print(number)
        tempStr2 += "(" + str(playerHistory['matches'][0]['players'][number]['hero']) + ", " + str(playerHistory['matches'][0]['players'][number]['side']) + ", " + str(playerHistory['matches'][0]['players'][number]['steam_account']) + ");\n "
    print(tempStr2)
    tempStr3 = 'kaka'
    for number in range(playerHistory['num_results']):
        sql="""
        INSERT INTO """ + tempStr + """ (dire_team_id, lobby_type, match_id, match_seq_num, players, radiant_team_id, start_time)
        VALUES (""" + str(playerHistory['matches'][number]['dire_team_id']) +""",""" + str(playerHistory['matches'][number]['lobby_type']) +""",""" + str(playerHistory['matches'][number]['match_id']) +""",""" +  str(playerHistory['matches'][number]['match_seq_num']) +""", '""" + tempStr2 +"""',""" + str(playerHistory['matches'][number]['radiant_team_id']) +""",""" + str(playerHistory['matches'][number]['start_time']) + """);"""

        cursor.execute(sql)



    

        
    

    conn.commit()





    

def main():
    cursor, conn = dbConnect()
    registration(getpass.getuser(), cursor, conn)
#    proverkaBazi(cursor, conn)
    userMenu(getpass.getuser(), cursor, conn)


main()
