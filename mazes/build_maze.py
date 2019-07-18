from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random

def new_maze(dim = (31,31),start = None, end = None):
    w, h = dim
    exits = [(2*i-1,0) for i in range(1,w/2)]+[(2*i-1,h-1) for i in range(1,w/2)]+[(0,2*i-1) for i in range(1,w/2)]+[(w-1,2*i-1) for i in range(1,w/2)]
    corners = [(0,0),(0,w),(0,h),(w,h)]
    if not start and not end:
        start = random.choice(exits)
    if not start and end:
        start = random.choice(list(set(exits)-set(end)))
    if not end or end == start:
        end = random.choice(list(set(exits)-set(start)))
    sx, sy = start
    ex, ey = end
    maze = np.array([0 if x == 0 or y == 0 or x == w-1 or y == h-1 else 1 for x in range(w) for y in range(h) ], np.uint8).reshape((w,h))
    maze[sy,sx] = 1
    maze[ey,ex] = 1
    maze[1:h-1,1:w-1] = np.random.random((h-2,w-2))<.66
    return maze

for i in range(10):
    maze = new_maze(dim = (21,21))
    plt.imshow(maze,cmap = 'gray')
    plt.show()
