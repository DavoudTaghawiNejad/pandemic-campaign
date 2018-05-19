from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from act2.game import Game
from random import sample


class GameSetup(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='vertical')
        self.main = main
        self.add_widget(Label(text="Setup:"))
        self.add_widget(Label(text="""- Remove all blue cards from the infection deck"""))
        print(sample(self.main.legacy.cdcs, 2))
        self.add_widget(Label(text=""" Set up a cdc in %s and %s""" % tuple(sample(self.main.legacy.cdcs, 2))))

    def next(self):
        return Game(self.main)