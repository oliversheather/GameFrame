from GameFrame import RoomObject, Globals
from Objects.centenario import centenario
import random

class Car(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("car.png")
        self.set_image(image,13,16)
        
        # start asteroid timer
        asteroid_spawn_time = random.randint(15,150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
        
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = centenario(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)