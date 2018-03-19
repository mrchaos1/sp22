#!/usr/bin/python3

from kivy.app 				import App
from kivy.uix.boxlayout 	import BoxLayout
from kivy.uix.button 		import Button
from kivy.uix.codeinput		import CodeInput
from pygments.lexers 		import HtmlLexer
from kivy.config 			import Config
from kivy.uix.floatlayout 	import FloatLayout
from kivy.uix.boxlayout 	import BoxLayout
from kivy.uix.widget 		import Widget
from kivy.uix.textinput 	import TextInput
from kivy.uix.label 		import Label



# Disable window resize
#Config.set("graphics", 'resizable', 0)

# Set window's size
#Config.set("graphics", 'width', '500')
#Config.set("graphics", 'height', '300')


class TemplateApp(App):
		
	def test(self):
        root = Builder.load_string(KV)
        return root






class testApp(App):
	
	

		
	def build(self):
		
					
		
		layout = BoxLayout(padding = [10, 10])
		sub_layout = BoxLayout(orientation = 'vertical')
		
		layout.add_widget(Button(text = "Button 1"))
		layout.add_widget(Button(text = "Button 2"))
		
		sub_layout.add_widget(Button(text = "sButton 1"))
		sub_layout.add_widget(Button(text = "sButton 2"))
		
		layout.add_widget(sub_layout)
		
		
		return layout
		
	def btn_press(self, instance):
		print('Кнопка нажата')
		instance.text = "Нажато"
		instance.background_color = [0, 0, 1, 1]
	
if __name__ == "__main__":
	TemplateApp().run()
	
	
	
	
	
