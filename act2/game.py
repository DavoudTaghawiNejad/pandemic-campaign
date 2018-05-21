from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from citychooser import CityChooser
from act2.end import End


bio_terrorist_route = ['Tokio', 'Shanghai' 'Hong Kong', 'Kolkata', 'Deli', 'Karachi', 'Riyadh',
                       'Cairo', ' Khartoum', 'Kinshasa', 'Lagos' 'Sau Paulo', 'Santiago',
                       'Lima', 'Mexico City', 'Chicago', 'Montreal', 'New York', 'Washington', 'Atlanta',
                       'Chicago', 'San Francisco']


class Game(BoxLayout):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, orientation='horizontal')
        self.main = main
        self.main.next_visible(False)
        self.moves = 0
        self.cdc = 2

        self.buttonboxes = BoxLayout(orientation='vertical')
        move_btn = Button(text="Confirm Move")
        move_btn.bind(on_press=self.move)
        self.buttonboxes.add_widget(move_btn)

        self.add_widget(self.buttonboxes)
        self.textside = BoxLayout(orientation='vertical')
        self.add_widget(self.textside)
        self.objective = Label(text="""Objective cure all diseases 
        
        - Confirm after each move and new
         Center of Disease control""")
        self.infection_text = Label(text="")
        self.textside.add_widget(self.objective)
        self.textside.add_widget(self.infection_text)


        self.bio_terrorist_location = bio_terrorist_route[0]

    def move(self, _):
        self.moves += 1
        self.infection_text.text = "Infect %s with one blue cube" % self.bio_terrorist_location
        self.change_bio_terrorist_location()
        if self.moves == 3:
            self.objective.text = """Interpol, a bio terrorist is on the loose. 
                                     He is headed for north America; Airports are 
                                     monitored. New York is an unlikely entry point.
                                     It appears he is always one step ahead.
                                     - you have one additional action: Search
                                     When you are in a city you can press the 
                                     search button, and if the Bioterrorist is 
                                     in that city you won"""
            search_btn = Button(text="Search")
            search_btn.bind(on_press=self.search)
            self.buttonboxes.add_widget(search_btn)



        self.test_end()

    def search(self, _):
        self.main.callnext(CityChooser(self.main, self, End(self.main), self.city_choosen))

    def city_choosen(self, city):
        return self.bio_terrorist_location == city

    def change_bio_terrorist_location(self):
        self.bio_terrorist_location = bio_terrorist_route[self.moves % len(bio_terrorist_route)]
        print(self.bio_terrorist_location)
        self.main.legacy.infected_by_bio_terrorist.append(self.bio_terrorist_location)

    def test_end(self):
        if self.moves >= 10 and self.cdc >= 2:
            self.callnext(End(self.main))

