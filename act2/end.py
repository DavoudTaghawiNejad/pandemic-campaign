from kivy.uix.image import Image
from kivy.uix.label import Label
from act3.introduction import Introduction


class End(Image):
    def __init__(self, main, **kwargs):
        super().__init__(source='terrorist.jpg', allow_stretch=True, keep_ratio=True, **kwargs)
        self.main = main
        main.next_visible(True)
        me = Label(text="You caught the bio terrorist!", center=self.main.center)
        self.add_widget(me)

    def next(self):
        return Introduction(self.main)
