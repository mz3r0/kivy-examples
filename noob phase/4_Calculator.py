import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


kivy.require('2.3.0')


class TestingApp(App):
    def build(self):

        def on_height_resize(label_widget, new_value):
            label_widget.font_size = 0.5 * label_widget.height

        def evaluate_result(*args):
            try:
                output.text = str(eval(output.text))
            except SyntaxError:
                output.text = 'Python syntax error!'

        def clear_label(*args):
            output.text = ''

        def print_button_text(instance):
            output.text += instance.text

        root = BoxLayout(orientation='vertical')
        output = Label(size_hint_y=1)
        buttons = GridLayout(cols=4, size_hint_y=2)

        symbols = ('1', '2', '3', '+',
                   '4', '5', '6', '-',
                   '7', '8', '9', '.',
                   '0', '*', '/', '=')

        for symbol in symbols:
            buttons.add_widget(Button(text=symbol))

        clear_button = Button(text='clear', size_hint_y=None, height=100)
        output.bind(height=on_height_resize)
        buttons.children[0].bind(on_press=evaluate_result)

        # Possibly due to insertion, the 0th child is the '=' button.

        clear_button.bind(on_press=clear_label)
        for button in buttons.children[1:]:
            button.bind(on_press=print_button_text)

        # Finalize
        root.add_widget(output)
        root.add_widget(buttons)
        root.add_widget(clear_button)

        return root


if __name__ == '__main__':
    TestingApp().run()
