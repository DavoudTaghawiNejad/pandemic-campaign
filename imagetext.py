from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class ImageText(AnchorLayout):
    def __init__(self, main, text, image=None, **kwargs):
        super().__init__(anchor_x='center', anchor_y='center', **kwargs)
        visible = hasattr(self, 'next')
        main.next_visible(visible)
        self.main = main

        if image is not None:
            image = Image(source='images/' + image, allow_stretch=True, keep_ratio=True, **kwargs)
            self.add_widget(image)

        me = Label(text="[b]" + text + "[/b]", markup=True, text_size=(self.width * 3, None))
        self.add_widget(me)