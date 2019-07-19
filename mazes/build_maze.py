from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random

def new_room(dim = None):
    if not dim:
        dim = (random.randint(7,13),random.randint(7,13))
    w, h = dim
    exits = [[(i,0) for i in range(2,w-2)],[(i,h-1) for i in range(2,w-2)],[(0,i) for i in range(2,h-2)],[(w-1,i) for i in range(2,h-2)]]
    # corners = [(0,0),(0,w),(0,h),(w,h)]
    exit_directions = random.sample(exits,random.randint(1,3))
    maze = np.array([0 if x == 0 or y == 0 or x == w-1 or y == h-1 else 1 for x in range(w) for y in range(h) ], np.uint8).reshape((w,h))
    # exits = []
    for exit in exit_directions:
        ey, ex = random.choice(exit)
        # exits.append(exit)
        maze[ey,ex] = 1
    return maze#,exits

def new_maze(dim = None):
    
    if not dim:
        dim = (2*random.randint(10,30)-1,2*random.randint(10,30)-1)
    w, h = dim
    exits = [[(i,0) for i in range(2,w-2)],[(i,h-1) for i in range(2,w-2)],[(0,i) for i in range(2,h-2)],[(w-1,i) for i in range(2,h-2)]]
    # corners = [(0,0),(0,w),(0,h),(w,h)]
    exit_directions = random.sample(exits,2)
    maze = np.array([0 if x == 0 or y == 0 or x == w-1 or y == h-1 else 1 for y in range(h) for x in range(w)], np.uint8).reshape((h,w))

    internals = [(x,y) for x in range(2,w-1,2) for y in range(2,h-1,2)]
    for internal in internals:
        x,y = internal
        dir = random.choice([(y+1,x),(y-1,x),(y,x+1),(y,x-1)])
        maze[dir] = 0
        maze[y,x] = 0

    # exits = []
    for exit in exit_directions:
        ex, ey = random.choice(exit)
        # exits.append(exit)
        maze[ey,ex] = 1
    return maze#,exits

for i in range(5):
    maze = new_maze()
    plt.imshow(maze,cmap = plt.cm.get_cmap('gray', 10))
    plt.show()
