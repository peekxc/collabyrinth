from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import cm

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

for i in range(5):
    maze = new_room()
    plt.imshow(maze,cmap = cm.get_cmap('gray', 10))
    plt.show()
