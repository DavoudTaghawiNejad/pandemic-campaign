from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from act3.end import End
from colorchooser import ColorChooser

bio_terrorist_route = ['Kinshasa', 'Sau Paulo', 'Santiago', 'Lima',
                       'Tokio', 'Hong Kong', 'Sidney', 'Deli', 'Karachi']

class Game(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='horizontal')

        self.moves = 0
        self.cures = 0
        self.main = main
        self.main.next_visible(False)
        self.buttonboxes = BoxLayout(orientation='vertical')
        move_btn = Button(text="Confirm Move")
        move_btn.bind(on_press=self.move)
        self.buttonboxes.add_widget(move_btn)
        cure_btn = Button(text="Cure Found")
        cure_btn.bind(on_press=self.cure_found)
        self.buttonboxes.add_widget(cure_btn)

        self.add_widget(self.buttonboxes)
        self.textside = BoxLayout(orientation='vertical')
        self.add_widget(self.textside)
        self.objective = Label(text="""Objective cure all diseases """)
        self.infection_text = Label(text="")
        self.textside.add_widget(self.objective)
        self.textside.add_widget(self.infection_text)
        self.bio_terrorist_location = bio_terrorist_route[0]
        self.cured = set()

    def move(self, _):
        self.moves += 1

    def cure_found(self, _):
        self.main.callnext(ColorChooser(self.main, self, End(self.main), self.color_choosen))

    def color_choosen(self, color):
        self.cured.add(color)
        return len(self.cured) == 4



    def next(self):
        return End(self.main)