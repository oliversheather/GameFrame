from GameFrame import Globals, Level
from Objects.Frog import Frog
from Objects.f40 import f40
from Objects.carshooter import carshooter
from Objects.Hud import Score
from Objects.Car import Car
from Objects.river import river
from Objects.stream import stream
from Objects.finish import finish

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("frogger game screen.png")
        
        # add objects
        self.add_room_object(Frog(self, 550, 700))
        self.add_room_object(Car(self,1120, 500))
        self.add_room_object(river(self,0,300))
        self.add_room_object(stream(self,750,300))
        self.add_room_object(finish(self,0,0))

         # add objects
        self.add_room_object(f40(self, 25, 50))
        self.add_room_object(carshooter(self,-75, 0))

          # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)