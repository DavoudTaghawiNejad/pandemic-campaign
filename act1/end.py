from imagetext import  ImageText
from act2.introduction import Introduction


class End(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="You won! \n"
                              "You build alternative Centers of Disease control, we take it from here",
                         image=None,
                         **kwargs)

    def next(self):
        return Introduction(self.main)
