from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from act1.gamesetup import GameSetup


class Introduction(AnchorLayout):
    def __init__(self, main, **kwargs):
        super().__init__(anchor_x='center', anchor_y='center')
        image = Image(source='Pandemic.jpg', allow_stretch=True, keep_ratio=True, **kwargs)
        self.main = main
        main.next_visible(True)
        me = Label(text="Welcome to Trumpft the Pandemic the Campaign", center=self.main.center)
        self.add_widget(image)
        self.add_widget(me)

    def next(self):
        return GameSetup(self.main)