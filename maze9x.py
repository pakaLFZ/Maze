import random
import os
import time

maze = []
x = y = 1
direction = 0  #1上2下3左4右

os.system('cls')   #清空屏幕
length = int(input("Hello, please type the length\n"))
width = int(input("how about the width?\n"))

for i in range(length):
    maze.append([])
    for j in range(width):
        maze[i].append('#')
while 1:
    os.system('cls')   #清空屏幕
    direction = random.randint(1,4)
    if direction == 1:
        if maze[y+1][x] == '#':
            maze[y][x] = ' '
            y += 1
    if direction == 2:
        if maze[y-1][x] == ' ':
            maze[y][x] = ' '
            y -= 1
    if direction == 3:
        if maze[y][x-1] == ' ':
            maze[y][x] = ' '
            x -= 1
    if direction == 4:
        if maze[y][x+1] == ' ':
            maze[y][x] = ' '
            x += 1
    for time in range(length):
        for ttime in range(width):
            print(maze[time][ttime], end = '')
        print("")
    time.sleep(3.0)


