from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from act3.game import Game
from random import sample


class GameSetup(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='vertical')
        self.main = main
        self.add_widget(Label(text="Setup:"))
        self.add_widget(Label(text="""- Mix in all cards to the infection deck"""))
        if len(main.legacy.infected_by_bio_terrorist) > 9:
            infected_cities = sample(main.legacy.infected_by_bio_terrorist, 9)
            remaining = 0
        else:
            infected_cities = main.legacy.infected_by_bio_terrorist
            remaining = 9 - len(infected_cities)
        self.add_widget(Label(text="""Infect the following cities:"""))

        text = '\n'.join([""" - %s with %i cubes """ % (city, (11 - i) // 3)
                          for i, city in enumerate(infected_cities)])
        self.add_widget(Label(text=text))
        if remaining:
            self.add_widget(Label(text="""Infect the remaining %i cities as usual:""" % remaining))

    def next(self):
        return Game(self.main)
