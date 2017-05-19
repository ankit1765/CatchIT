# Testing for sprite collisions

from livewires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Bucket(games.Sprite):
    """" A bucket controlled by the mouse. """
    def update(self):
        """ Move to mouse position. """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
 
    def check_collide(self):
        """ Check for collision with raindrop. """
        for raindrop in self.overlapping_sprites:
            raindrop.handle_collide()


class Raindrop(games.Sprite):
    """" A slippery raindrop. """
    def handle_collide(self):
        """ Move to a random screen location. """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    raindrop_image = games.load_image("raindrop.bmp")
    raindrop_x = random.randrange(games.screen.width)
    raindrop_y = random.randrange(games.screen.height)
    the_raindrop = Raindrop(image = raindrop_image, x = raindrop_x, y = raindrop_y)
    games.screen.add(the_raindrop)

    bucket_image = games.load_image("bucket.bmp")
    the_bucket = Bucket(image = bucket_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_bucket)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

# kick it off!
main()
