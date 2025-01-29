import random
from GameFrame import RoomObject
from Objects.f40 import f40

class carshooter(RoomObject):
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
        image = self.load_image("carshooter.png")
        self.set_image(image,200,250)
        
        # start f40 timer
        f40_spawn_time = random.randint(15,150)
        self.set_timer(f40_spawn_time, self.spawn_f40)

    def spawn_f40(self):
        """
        Randomly spawns a new f40
        """
        # spawn f40 and add to room
        new_f40 = f40(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_f40)
        
        # reset time for next f40 spawn
        f40_spawn_time = random.randint(15, 100)
        self.set_timer(f40_spawn_time, self.spawn_f40)