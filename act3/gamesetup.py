from imagetext import ImageText
from kivy.uix.label import Label
from act3.game import Game
from random import sample


class GameSetup(ImageText):
    def __init__(self, main, **kwargs):

        if len(main.legacy.infected_by_bio_terrorist) > 9:
            infected_cities = sample(main.legacy.infected_by_bio_terrorist, 9)
            remaining = 0
        else:
            infected_cities = main.legacy.infected_by_bio_terrorist
            remaining = 9 - len(infected_cities)

        citieslist = '\n'.join([""" - %s with %i cubes """ % (city, (11 - i) // 3)
                          for i, city in enumerate(infected_cities)])

        if remaining:
            remainingtext = "Infect the remaining %i cities as usual." % remaining
        else:
            remainingtext = ""

        super().__init__(**kwargs,
                         main=main,
                         text="Setup:"
                              "- Mix in all cards to the infection deck"
                              "Infect the following cities:" + citieslist + remainingtext)

    def next(self):
        return Game(self.main)
