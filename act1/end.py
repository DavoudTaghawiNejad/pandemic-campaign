from kivy.uix.label import Label
from act2.introduction import Introduction


class End(Label):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, text="You won! \n"
                                        "You build alternative Centers of Disease control, we take it from here")
        self.main = main
        self.main.next_visible(True)

    def next(self):
        return Introduction(self.main)
