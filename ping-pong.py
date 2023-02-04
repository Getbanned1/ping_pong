from pygame import *

back = (50, 50, 255) #цвет фона (background)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(back)

FPS = 60
game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
    clock.tick(FPS)
    display.update()