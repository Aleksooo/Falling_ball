import pygame as py
import sys

def fall_down(t):
    global y
    global V
    y = y_0 + (g * t ** 2) / 2
    V = g * t

def bounce_up(t):
    global y
    y = y_0 - V * t + (g * t ** 2) / 2

width, height = (500, 500)
radius = 40
x_0, y_0 = width / 2, height - radius
y = height - radius
g = 10
V = 0
time = 0
Down = True
Up = False

yellow = (255, 255, 217)
white = (0, 0, 0)

py.init()
screen = py.display.set_mode((width, height))

while True:
    screen.fill(yellow)
    py.time.Clock().tick(144)

    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    if py.mouse.get_focused():
        if py.mouse.get_pressed()[0]:
            if x_0 - radius <= py.mouse.get_pos()[0] <= x_0 + radius and y_0 - radius <= py.mouse.get_pos()[1] <= y_0 + radius:
                x_0, y_0 = py.mouse.get_pos()
                y = y_0

    if py.mouse.get_pressed()[0] == False:
        if Down == True:
            if y < height - radius:
                time += 0.2
                fall_down(time)
            elif y > height - radius:
                y = height - radius
                y_0 = y
                V -= 10
                time = 0
                Up = True
                Down = False
        if Up == True:
            if y <= height - radius:
                time += 0.2
                bounce_up(time)
            elif y > height - radius:
                y = height - radius
                V -= 10
                time = 0
        if V < 0:
            Up = False
            Down = True
            y = height - radius

    py.draw.circle(screen, white, (int(x_0), int(y)), radius)
    py.display.flip()

