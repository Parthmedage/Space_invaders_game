import pygame as g

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


gameWindow = g.display.set_mode((900, 600))


game_exit = False
game_over = False

g.display.set_caption("snake game")
g.display.update()




# game Loop
while not game_exit:
    for event in g.event.get():
        
        if event.type == g.QUIT:
            game_exit = True

    gameWindow.fill(black)
    g.display.update()

g.quit()
quit()