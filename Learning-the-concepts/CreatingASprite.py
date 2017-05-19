# Raindrop as a  Sprite
# Creating a sprite using pygame 

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

raindrop_image = games.load_image("raindrop.bmp")
raindrop = games.Sprite(image = raindrop_image, x = 320, y = 240)
games.screen.add(raindrop)

games.screen.mainloop()
