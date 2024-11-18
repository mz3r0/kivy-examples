from kivy.lang import Builder
import pandas as pd
import numpy as np

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.app import App

from kivy.core.window import Window

KV = """
Screen:
    name: 'main'

    ScrollView:
        do_scroll_y: False
        
        scroll_wheel_distance: dp(100)
        bar_width: dp(10)
        bar_color: 146/255, 146/255, 146/255, 1
        bar_inactive_color: 146/255, 146/255, 146/255, 1
        
        BoxLayout:
            orientation: 'horizontal'
            padding: [30]
            spacing: 30
            size_hint_x: None
            width: self.minimum_width
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_x: None
                width: 600
                height: self.minimum_height
                
                MyRecycleView:
                    do_scroll_x: False
                
            BoxLayout:
                orientation: 'vertical'
                size_hint_x: None
                width: 400
                
            BoxLayout:
                orientation: 'vertical'
                size_hint_x: None
                width: 400
                
            BoxLayout:
                orientation: 'vertical'
                size_hint_x: None
                width: 400

<MyTableCell>:
    text_size: self.size
    adaptive_height: True
    halign: "center"

<MyRecycleView>:
    viewclass: "MyTableCell"
    RecycleGridLayout:
        cols: 6
        id: rgl
        spacing: 10
        default_size_hint: None, None
        default_size: dp(98), dp(48)
        size_hint_y: None
        height: self.minimum_height
        width: self.cols * dp(94)

"""

def load_rv_data():
    """ Returns a list of dictionaries {'text': 'cell_value'}
     for all cells in RecycleGridLayout """
    df_data = []

    df = pd.DataFrame(np.random.rand(100, 6))
    arr = df.to_numpy()
    num_rows, num_cols = arr.shape

    tuple_generator = ((i, j) for i in range(num_rows) for j in range(num_cols))
    for tup in tuple_generator:
        cell = str(arr[tup])
        df_data.append(dict(text=cell))

    return df_data


class MyTableCell(RecycleDataViewBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.text = data['text']
        return super(MyTableCell, self).refresh_view_attrs(rv, index, data)


class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = load_rv_data()
        self.default_size_hint = (None, None)


class SampleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # Window
        Window.always_on_top = True
        Window.minimum_width = 500
        Window.minimum_height = 400
        Window.size = (1080, 720)
        # Window.clearcolor = (1, 1, 1, 1)

        # Build the app
        return Builder.load_string(KV)

if __name__ == '__main__':
    SampleApp().run()

# Problem: Scrollbars not working
