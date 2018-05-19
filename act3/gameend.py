from kivy.uix.label import Label


class GameEnd(Label):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, text="You cured all diseases; survived the Trump administration and"
                                        "you caught the bio terrorist!")
        main.next_visible(False)
        self.main = main
