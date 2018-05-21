from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from citychooser import CityChooser
from act1.end import End


# More stuff must happen earlier on

class Game(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='horizontal')
        self.main = main
        self.main.next_visible(False)
        self.moves = 0
        self.cdc = 1
        self.legacy = main.legacy

        buttonboxes = BoxLayout(orientation='vertical')
        move_btn = Button(text="Confirm Move")
        move_btn.bind(on_press=self.move)
        buttonboxes.add_widget(move_btn)
        cdc_btn = Button(text="Confirm CDC")
        cdc_btn.bind(on_press=self.build_cdc)
        buttonboxes.add_widget(cdc_btn)
        self.add_widget(buttonboxes)
        self.objective = Label(text="""Objective cure all diseases 
        
        - Confirm after each move and new
         Center of Disease control""")
        self.add_widget(self.objective)

    def move(self, _):
        self.moves += 1
        if self.moves == 10:
            self.objective.text = """Trumpf defunded the CDC, remove the CDC in Atlanta\
        
                                           New objective: 
                                           - build a CDC in ASIA
                                           - build a CDC in South America"""

            print('10')
        self.test_end()

    def build_cdc(self, _):
        self.main.callnext(CityChooser(self.main, self, End(self.main), self.cdc_choosen))
        self.test_end()

    def cdc_choosen(self, city):
        if city.lower() in ['tokio', 'sau paulo', 'lima']:
            self.legacy.cdcs.add(city)
            return len(self.legacy.cdcs) >= 2 and self.moves >= 10
        return False


    def test_end(self):
        if self.moves >= 10 and len(self.legacy.cdcs) >= 2:
            self.main.callnext(End(self.main))
