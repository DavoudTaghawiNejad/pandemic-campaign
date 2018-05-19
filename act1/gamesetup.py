from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from act1.game import Game


class GameSetup(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='vertical')
        self.main = main
        self.add_widget(Label(text="Setup:"))
        self.add_widget(Label(text="""
        - Put the Washington, Atlanta and Tokio infection cards on the infection discard pile
        - Infect each of the three cities with three cubes
        - Choose 3 more cards randomly and infect them two cubes each
        - Choose 3 more cards randomly and infect them one cube each"""))

    def next(self):
        return Game(self.main)