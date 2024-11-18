import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.properties import ListProperty

class testApp(App):
	rect_pos = ListProperty([50,50])

	def build(self):
		dummy = Widget()
		root = GridLayout(cols=2)
		root_left = GridLayout(rows=2)
		
		btn1 = Button(text='To the right')
		btn2 = Button(text='To the left')

		with dummy.canvas:
			self.rect = Rectangle(pos=self.rect_pos, size=(dp(150), dp(150)))
			rect = self.rect

		def update_rect_right(instance):
			x, y = rect.pos
			x += dp(150)
			rect.pos = (x, y) # or self.rect
			print('self here is:{}'.format(type(self)))

		btn1.bind(on_press=update_rect_right)
		btn2.bind(on_press=self.update_rect_left)

		root_left.add_widget(btn1)
		root_left.add_widget(btn2)

		root.add_widget(root_left)
		root.add_widget(dummy)
		
		return root

	def update_rect_left(self, instance):
		x, y = self.rect.pos
		x -= dp(150)
		self.rect.pos = (x, y)
		print('self here is:{}'.format(type(self)))


if __name__ == '__main__':
	testApp().run()

	