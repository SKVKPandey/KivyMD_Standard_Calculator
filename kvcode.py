code="""
ScreenManager:
	MainScreen:

<MainScreen>:
	
	name:'main'

	field:field
	
	NavigationLayout:
		ScreenManager:
			Screen:
		
				MDGridLayout:
					cols:1

					MDToolbar:
						title: "Standard Calculator"

					BoxLayout:
						orientation:'vertical'
						spacing: '20dp'

						MDFloatLayout:
							MDTextField:
								id:field
								size_hint: (0.95,0.25)
								disabled:False
								pos_hint:{'center_x':0.5,'center_y':0.1}
								on_text_validate:root.Eq()
			
					BoxLayout:
						orientation:'vertical'
						spacing: '50dp'

						MDFloatLayout:
							MDGridLayout:
								cols:3
								size_hint: (0.98,1)
								pos_hint:{'center_x':0.5,'center_y':0.5}

								MDFlatButton:
									text:"÷"
									on_press:root.Div()

								MDFlatButton:
									text:"^"
									on_press:root.Pow()

								MDFlatButton:
									text:"="
									on_press:root.Eq()

								MDFlatButton:
									text:"+"
									on_press:root.Plus()

								MDFlatButton:
									text:"-"
									on_press:root.Sub()

								MDFlatButton:
									text:"x"
									on_press:root.Mul()

								MDFlatButton:
									text:"7"
									on_press:root.Seven()

								MDFlatButton:
									text:"8"
									on_press:root.Eight()

								MDFlatButton:
									text:"9"
									on_press:root.Nine()

								MDFlatButton:
									text:"4"
									on_press:root.Four()

								MDFlatButton:
									text:"5"
									on_press:root.Five()

								MDFlatButton:
									text:"6"
									on_press:root.Six()

								MDFlatButton:
									text:"1"
									on_press:root.One()

								MDFlatButton:
									text:"2"
									on_press:root.Two()

								MDFlatButton:
									text:"3"
									on_press:root.Three()

								MDFlatButton:
									text:"0"
									on_press:root.Zero()

								MDFlatButton:
									text:"Back"
									on_press:root.Bck()

								MDFlatButton:
									text:"M"
									on_press:root.MryStr()

								MDFlatButton:
									text:"."
									on_press:root.Deci()

								MDFlatButton:
									text:"Clear"
									on_press:root.Clr()

								MDFlatButton:
									text:"MC"
									on_press:root.MryClr()
"""
