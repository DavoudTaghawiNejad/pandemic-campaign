from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

city_list = {'blue': ['New York', 'Washington', 'Rome', 'Essen', 'St. Petersburg',
                      'San Francisco', 'Chicago', 'Montreal', 'Milan', 'Madrid',
                      'xxx', 'yyy'],
             'yellow': ['Kinshasa', 'Sau Paulo', 'Santiago', 'Lima'],
             'red': ['Tokio', 'Hong Kong', 'Sidney'],
             'black': ['Deli', 'Karachi']}


class CityChooser(BoxLayout):
    def __init__(self, main, caller, next_screen, returner, **kwargs):
        super().__init__(**kwargs, orientation='horizontal')
        self.next_screen = next_screen
        self.callnext = main.callnext
        self.caller = caller
        self.returner = returner
        self.moves = 0
        self.cdc = 1

        color_btns = BoxLayout(orientation='vertical')
        bluebtn = Button(text="Blue")
        yellowbtn = Button(text="Yellow")
        blackbtn = Button(text="Black")
        redbtn = Button(text="Red")
        bluebtn.bind(on_press=self.color_clicked)
        yellowbtn.bind(on_press=self.color_clicked)
        blackbtn.bind(on_press=self.color_clicked)
        redbtn.bind(on_press=self.color_clicked)
        color_btns.add_widget(bluebtn)
        color_btns.add_widget(yellowbtn)
        color_btns.add_widget(blackbtn)
        color_btns.add_widget(redbtn)
        self.citybtns = BoxLayout(orientation='vertical')
        self.add_widget(color_btns)
        self.add_widget(self.citybtns)

    def color_clicked(self, btn):
        self.citybtns.clear_widgets()
        cities = city_list[btn.text.lower()]
        for city in cities:
            btn = Button(text=city)
            btn.bind(on_press=self.city_choosen)
            self.citybtns.add_widget(btn)

    def city_choosen(self, btn):
        if self.returner(btn.text):
            self.callnext(self.next_screen)
        else:
            self.callnext(self.caller)
