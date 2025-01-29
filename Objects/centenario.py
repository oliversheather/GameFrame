from GameFrame import RoomObject, Globals
import random

class centenario(RoomObject):
    """
    A class for Cars danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the centenario object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("centenario.png")
        self.set_image(image,150,100)

          # set travel direction
        angle = 0
        self.set_direction(angle, -10)
       
         # register events
        self.register_collision_object("Frog")

    def step(self):
            """
            Determines what happens to the centenario on each tick of the game clock
            """
            self.keep_in_room()
            
    def keep_in_room(self):
            """
            Keeps the centenario inside the top and bottom room limits
            """
            if self.y < 0:
                self.y = 0
                self.y_speed *= -1
            elif self.y > Globals.SCREEN_HEIGHT - self.height:
                self.y = Globals.SCREEN_HEIGHT - self.height
                self.y_speed *= -1
            
    def handle_collision(self, other, other_type):
            """
            Handles the collision events for the centenario
            """
            
            if other_type == "Frog":
                self.room.running = False