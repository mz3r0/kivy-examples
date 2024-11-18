from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.lang import Builder


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass


class Manager(ScreenManager):
    pass


KV = """
<ScreenOne>:

<ScreenTwo>:

<Manager>:
    # id: screen_manager
    # s1: the_first_screen
    # s2: the_second_screen

    ScreenOne:
        # id: the_first_screen
        name: 'screen1'
        Button:
            text: '1 > 2'
            on_press: root.current = 'screen2'

    ScreenTwo:
        # id: the_second_screen
        name: 'screen2'
        Button:
            text: '2 > 1'
            on_press: root.current = 'screen1'
"""

Builder.load_string(KV)


class ScreensApp(App):
    def build(self):
        return Manager(transition=WipeTransition())


if __name__ == '__main__':
    ScreensApp().run()
