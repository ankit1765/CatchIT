# Moving/falling raindrop
# Sprite velocities with pygame

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

raindrop_image = games.load_image("raindrop.bmp")
the_raindrop = games.Sprite(image = raindrop_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1,
                         dy = 1)
games.screen.add(the_raindrop)

games.screen.mainloop()

