
# Learning to deal with the boundaries of the screen 

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

class Raindrop(games.Sprite):
    # A bouncing raindrop. 
    def update(self):
        #Reverse a velocity component if edge of screen reached
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    raindrop_image = games.load_image("raindrop.bmp")
    the_raindrop = Raindrop(image = raindrop_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    games.screen.add(the_raindrop)

    games.screen.mainloop()

#Start the game//go to main
main()
