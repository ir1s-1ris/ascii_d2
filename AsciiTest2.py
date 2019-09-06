from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, StopApplication, NextScene
from asciimatics.effects import Print
from asciimatics.widgets import Frame, Button, Divider, Layout
from asciimatics.renderers import FigletText

import sys
import getpass
import sqlite3

class ListView(Frame):
    def __init__(self, screen):
        super(ListView, self).__init__(screen,
        int(screen.height * 0.95),
        int(screen.width * 0.95),
        hover_focus=True,
        can_scroll=False,
        title="Contact List")

        self._edit_button = Button("Edit", self._quit)
        self._delete_button = Button("Delete", self._quit)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("add", self._add), 0)
        layout2.add_widget(self._delete_button, 2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.fix()
    
    def _add(self):
        raise NextScene("HelloScene")

    
    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

class myUser():
    def __init__(self):
        self.name = getpass.getuser()

class myDb(object):
    def __init__(self):

        self._db = sqlite3.connect('asciiDb.db')
        self._db.row_factory = sqlite3.Row

        self._db.cursor().execute('''
            CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                username TEXT,
                regdate INT,
                steamId INT
            )
        ''')
        self._db.commit()
    
    def write(self, sql):
        self._db.cursor().execute(sql)
        self._db.commit()

    def read(self, sql):
        self._db.cursor().execute(sql).fetchall()


#возвращает эффект
class HelloScene(Print): 
    def __init__(self, screen):
        activeUser = myUser()
        text = "Hello " + str(activeUser.name)
        super(HelloScene, self).__init__(
            screen,
            FigletText(text, "big"),
            screen.height // 3,
            screen.width // 3,
            colour = screen.COLOUR_GREEN,
            bg = screen.COLOUR_BLACK,
            speed = 1
        )

class frame1(Frame):
    def __init__(self, screen, activeDb):
        super(frame1, self).__init__(
            screen,
            int(screen.height * 0.99),
            int(screen.width * 0.99),
            on_load = self._reload_list,
            hover_focus=True,
            can_scroll=False,
            title="frame1"
        )
        self._activeDb = activeDb

        layout = Layout([100], fill_frame = True)
        self.add_layout(layout)
        

    def _reload_list(self):
        print('bak')

    


    




def demo(screen, scene):

    scenes = [
        Scene([ListView(screen)], -1, name="Main"),
        Scene([HelloScene(screen)], -1, name="HelloScene")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


activeDb = myDb()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene


































# from pyfiglet import Figlet

# from asciimatics.scene import Scene
# from asciimatics.screen import Screen
# from asciimatics.exceptions import ResizeScreenError
# from asciimatics.renderers import FigletText
# from asciimatics.effects import Print

# import sys

# def _credits(screen):
#     scenes = []
    
#     text = Figlet(font="banner", width=200).renderText("Функция работает")
#     width = max([len(x) for x in text.split("\n")])

#     effects = [
#         Print(screen,
#         FigletText("Function rabotaet", "big"),
#         screen.height - 9, x = (screen.width - width) // 2 + 1,
#         colour = Screen.COLOUR_GREEN,
#         speed = 1)
#     ]
#     scenes.append(Scene(effects, -1))

#     screen.play(scenes, stop_on_resize=True)

# if __name__ == "__main__":
#     while True:
#         try:
#             Screen.wrapper(_credits)
#             sys.exit(0)
#         except ResizeScreenError:
#             pass