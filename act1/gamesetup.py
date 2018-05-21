from imagetext import ImageText
from act1.game import Game


class GameSetup(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="""[size=24sp]Setup: 
        [size=18sp]
        - Put the Washington, Atlanta and Tokio infection cards on the infection discard pile\n
        - Infect each of the three cities with three cubes\n
        - Choose 3 more cards randomly and infect them two cubes each\n
        - Choose 3 more cards randomly and infect them one cube each[/size]\n
        \n
        - Play Medic, Scientist, Researcher, Contingency Planer and/or Dispatcher
        """,
                         image='Pandemic.jpg',
                         **kwargs)

    def next(self):
        return Game(self.main)