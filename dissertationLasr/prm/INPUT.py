
from collections import defaultdict

MIN_RAND = 0
MAX_RAND = 20
ITERATIONS = 50
OBSTACLELIST = []
STEP = 1
SAFE_SIZE = 1
START = [[0,0,0], [20,0,0], [20,0,20]]
GOAL = [[20,20,20], [0,20,20], [0,20,0]]
GNODE = [None for i in range(len(START))]
SNODE = [None for i in range(len(START))]
path = [None for i in range(len(START))]
colors = ['r','b','g','k','y', 'm']
class node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.nearest = []
        self.distanceToNearest = []
for i in range(len(GNODE)):
    GNODE[i] = node(GOAL[i][0], GOAL[i][1], GOAL[i][2])
    SNODE[i] = node(START[i][0], START[i][1], START[i][2])

"35.15149771931837"
"70.25583752133146"