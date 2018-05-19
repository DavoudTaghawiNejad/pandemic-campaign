
from kivy.app import App
from kivy.uix.actionbar import ActionBar, ActionButton, ActionView, ActionPrevious, ActionOverflow
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import WidgetException

from act1.introduction import Introduction
from legacy import Legacy


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, orientation='vertical')
        self.legacy = Legacy()
        self.actionbar = ActionBar(pos_hint={'top': 1})
        self.av = av = ActionView()
        av.add_widget(ActionPrevious(title='Action Bar', with_previous=False))
        av.add_widget(ActionOverflow())
        backbutton = ActionButton(text='Back')
        av.add_widget(backbutton)
        backbutton.bind(on_press=(self.back))
        self.nextbutton = ActionButton(text='Next')
        av.add_widget(self.nextbutton)
        self.nextbutton.bind(on_press=(self.nextbtn))
        self.monitor = Introduction(self)

        self.actionbar.add_widget(av)

        # can't be set in F.ActionView() -- seems like a bug
        av.use_separator = True
        self.add_widget(self.actionbar)
        self.add_widget(self.monitor)
        self.av = av


    def next_visible(self, visible=True):
        try:
            if visible:
                self.av.add_widget(self.nextbutton)
            else:
                self.av.remove_widget(self.nextbutton)
        except WidgetException:
            pass

    def back(self, _):
        self.next_visible(True)
        self.remove_widget(self.monitor)
        self.monitor = self.last_widget
        self.add_widget(self.monitor)

    def nextbtn(self, _):
        self.last_widget = self.monitor
        self.remove_widget(self.monitor)
        self.monitor = self.monitor.next()
        self.add_widget(self.monitor)

    def callnext(self, next):
        self.last_widget = self.monitor
        self.remove_widget(self.monitor)
        self.monitor = next
        self.add_widget(self.monitor)




class MyApp(App):

    def build(self):
        self.main = RootWidget()
        #self.main.remove_btn()

        return self.main




if __name__ == '__main__':
    MyApp().run()