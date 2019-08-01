#пробуем sqlite3

import sqlite3


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

import getpass
import sqlite3
import sys

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
            regDate INTEGER
        );
        """)
    except:
        print('Не получилось создать юзерс')
        
    
    return cursor
    


def registration(user, cursor):
    print(user)
    sql = "SELECT * FROM users WHERE user =?"
    cursor.execute(sql, [(user)])
    temp = type(cursor.fetchall())
    print(cursor.fetchall())
    if (temp[0] == None):
        print('null')



def main():
    cursor = dbConnect()
    registration(getpass.getuser(), cursor)



main()
