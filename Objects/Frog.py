from GameFrame import RoomObject, Globals
import pygame

class Frog(RoomObject):
    """
    A class for the player's avitar (the Frog)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Frog object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Frog.png")
        self.set_image(image,75,75)
        
        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y -= 20
        elif key[pygame.K_s]:
            self.y += 20
        elif key [pygame.K_a]:
            self.x -= 20
        elif key [pygame.K_d]:
            self.x += 20
        elif key [pygame.K_q]:
            self.y -= 40
            
    def keep_in_room(self):
        """
        Keeps the frog inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
    def step(self):
        """
        Determine what happens to the Frog on each click of the game clock
        """
        self.keep_in_room()