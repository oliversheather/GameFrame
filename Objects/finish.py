from GameFrame import RoomObject, Globals

class finish(RoomObject):
    def __init__(self, room, x, y):
        """
        Initialise the centenario object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("finish.png")
        self.set_image(image,1280,50)
        # register events
        self.register_collision_object("Frog")
    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the f40
        """
        
        if other_type == "Frog":
            self.room.score.update_score(1)