# Background Image
# Setting the background image of the graphics screen // (using image in folder)

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

games.screen.mainloop()
