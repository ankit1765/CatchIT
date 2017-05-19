# CatchIT
# Player must catch falling raindrops in a bucket before they hit the ground
# Learned Object-Oriented Programming, PyGame, and Livewires Module 

from livewires import games, color  
import random

#setting up the screen
games.init(screen_width = 640, screen_height = 480, fps = 50)


class Bucket(games.Sprite):
    
    #The user must move the bucket from left to right using a mouse to catch raindrops
 
    image = games.load_image("bucket.bmp")

    def __init__(self): #initialize the bucket object & create a score text box
        
        super(Bucket, self).__init__(image = Bucket.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        
        games.screen.add(self.score) #adding the text/score to the screen

    def update(self):
        
        #Assigning the mouse x-coordinate to bucket's x coordinate 
        self.x = games.mouse.x
        
        #making sure the bucket does not overflow out of the screen on both sides
        
        if self.left < 0:    
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        
        #checking to see if any raindrops have been caught in the bucket 
        for raindrop in self.overlapping_sprites:
            
            #increase score by 10 if the raindrop overlaps the bucket 
            self.score.value += 10
            
            #making sure the score is not out of the screen
            self.score.right = games.screen.width - 10 
            raindrop.handle_caught()


class Raindrop(games.Sprite):
    
    #A raindrop which falls to the ground from the cloud
    
    image = games.load_image("raindrop.bmp")
    speed = 1   

    def __init__(self, x, y = 90): #90 to bring the raindrop right out of the cloud
        
        #Initialize a new raindrop object
        super(Raindrop, self).__init__(image = Raindrop.image,
                                    x = x, y = y,
                                    dy = Raindrop.speed)

    def update(self):
        #Checking to see if raindrop has reached screen bottom. If yes, then end the game. 
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self): #Raindrop has been caught so it disappears here
        
        self.destroy()

    def end_game(self): #when the raindrop has touched the ground, the game ends. 
       
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Cloud(games.Sprite):

    #A cloud which moves left and right, dropping raindrops. 

    image = games.load_image("cloud.bmp")


    def __init__(self, y = 55, speed = 2, odds_change = 200): #setting the clouds speed and location
        #Initialize the Cloud object. 
        super(Cloud, self).__init__(image = Cloud.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)

        #raindrops fall at random times in random directions 
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        #Determine if direction needs to be reversed randomly or at end of the screen
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
                
        self.check_drop()


    def check_drop(self):
        #Decrease countdown or raindrop falls and reset countdown. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_raindrop = Raindrop(x = self.x)
            games.screen.add(new_raindrop)

            
            self.time_til_drop = int(new_raindrop.height * 1.3 / Raindrop.speed) + 1      

#the main function.... starts the game and initializes everything 
def main():
    """ Play the game. """
    
    wall_image = games.load_image("wall.jpg", transparent = False)
    
    games.screen.background = wall_image

    the_chef = Cloud()
    games.screen.add(the_chef)

    the_bucket = Bucket()
    games.screen.add(the_bucket)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

main()

