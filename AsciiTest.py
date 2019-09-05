from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, StopApplication, NextScene
from asciimatics.effects import Print
from asciimatics.widgets import Frame, Button, Divider, Layout
from asciimatics.renderers import FigletText

import sys
import getpass

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


#возвращает эффект
class HelloScene(Print): 
    def __init__(self, screen):
        activeUser = myUser()
        text = activeUser.name
        super(HelloScene, self).__init__(
            screen,
            FigletText(text, "big"),
            screen.height // 3,
            screen.width // 3,
            colour = screen.COLOUR_GREEN,
            bg = screen.COLOUR_BLACK,
            speed = 1
        )

def demo(screen, scene):

    scenes = [
        Scene([ListView(screen)], -1, name="Main"),
        Scene([HelloScene(screen)], -1, name="HelloScene")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)



last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene























































# from asciimatics.screen import Screen
# from asciimatics.scene import Scene
# from asciimatics.exceptions import ResizeScreenError, NextScene
# from asciimatics.widgets import Frame, Layout
# from asciimatics.effects import Print
# from asciimatics.renderers import FigletText
# import sys

# # class HelloScene(frame):
# #     def __init__(self, screen):
# #         super(HelloScene, self).__init__(
# #             screen,
# #             screen.height,
# #             screen.width,
# #             has_border = False,
# #             name = "HelloScene"
# #         )

# #         # create form layout
# #         layout = Layout([1], fill_frame=True)
# #         self.add_layout(layout)

# #         #
# class HelloScene(Print):
#     def __init__(self, screen):
#         super(HelloScene, self).__init__(
#             screen,
#             FigletText("Class rabotaet", 'big'),
#             screen.width // 3,
#             colour=screen.COLOUR_GREEN,
#             bg=screen.COLOUR_WHITE,
#             speed=1,
#         )


# def demo(screen, scene):
#     scenes = [
#         Scene([HelloScene(screen)], -1, name="HelloScene")
#     ]

#     screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)



# last_scene = None
# while True:
#     try:
#         Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
#         sys.exit(0)
#     except ResizeScreenError as e:
#         last_scene = e.scene
        
