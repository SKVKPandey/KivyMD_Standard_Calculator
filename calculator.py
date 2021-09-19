from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kvcode import code

Window.size=(270,570)

class MainScreen(Screen):

	Memory=""

	def MryStr(self):
		if len(self.Memory)==0:
			self.Memory=self.field.text
		else:
			self.field.text+=self.Memory

	def MryClr(self):
		self.Memory=""

	def Deci(self):
		self.field.text+="."

	def Zero(self):
		self.field.text+="0"

	def One(self):
		self.field.text+="1"

	def Two(self):
		self.field.text+="2"

	def Three(self):
		self.field.text+="3"

	def Four(self):
		self.field.text+="4"

	def Five(self):
		self.field.text+="5"

	def Six(self):
		self.field.text+="6"

	def Seven(self):
		self.field.text+="7"

	def Eight(self):
		self.field.text+="8"

	def Nine(self):
		self.field.text+="9"

	def Plus(self):
		self.field.text+="+"

	def Sub(self):
		self.field.text+="-"

	def Mul(self):
		self.field.text+="x"

	def Div(self):
		self.field.text+="÷"

	def Pow(self):
		self.field.text+="^"

	def Bck(self):
		self.field.text=self.field.text[:-1]

	def Clr(self):
		self.field.text=""

	def Eq(self):

		dic = {"x":"*","÷":"/","^":"**"}
		val=self.field.text

		for i in dic:
			val=val.replace(i,dic[i])

		try:
			self.field.text=str(eval(val))
		except:
			self.field.text="Invalid Operation"

sm=ScreenManager()
sm.add_widget(MainScreen(name='main'))

class CalculatorApp(MDApp):
	def build(self):
		theme_cls = ThemeManager()
		self.icon="a_icon.png"
		self.theme_cls.primary_palette='DeepPurple'
		self.theme_cls.primary_hue='900'
		self.screen=Builder.load_string(code)
		return self.screen

CalculatorApp().run()