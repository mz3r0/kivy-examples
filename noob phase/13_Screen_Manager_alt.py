from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Declare both screens
class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


KV = """
#:import NoTransition kivy.uix.screenmanager.NoTransition

<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.parent.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.parent.current = 'menu'

<Manager>:
    transition: NoTransition()
    MenuScreen:
        name: 'menu'
    SettingsScreen:
        name: 'settings'
"""

Builder.load_string(KV)


class TestApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    TestApp().run()
