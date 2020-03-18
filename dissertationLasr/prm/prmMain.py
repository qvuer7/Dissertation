from prm.Functions import *
from prm.INPUT import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from prm.dronePRM import dronePRM




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
drones = []
nodelist = get_randomlist(iterations = ITERATIONS, minRand=5, maxRand=15, obstaclelist= OBSTACLELIST, step = STEP, safesize=SAFE_SIZE)
k_nearest_nodes(nodelist, k = len(nodelist), step = STEP, safesize=SAFE_SIZE, obstaclelist=OBSTACLELIST)
graph = Graph()


for i in range(len(nodelist)):
    for j in range(len(nodelist[i].nearest)):
        graph.add_edge(from_node = nodelist[i], to_node = nodelist[i].nearest[j], weight=nodelist[i].distanceToNearest[j])



for i in range(len(START)):
    drones.append(dronePRM(nodelist = nodelist, graph = graph, start = SNODE[i], goal = GNODE[i], ID = i, obstaclelist=OBSTACLELIST,
                        stepx = 1, stepy = 1, stepz = 1, dronesize=SAFE_SIZE, ax = ax))

paths = []
for i in range(len(drones)):
    paths.append(drones[i].path)
for i in range(len(drones)):
    for j in range(len(drones)):
        if j == i:
            pass
        else:
            drones[i].recipents.append(drones[j])

for i in range(len(drones)):
    drones[i].get_path()


sct_obst(OBSTACLELIST, ax = ax, color = 'g')

for i in range(len(nodelist)):
    ax.scatter(nodelist[i].x,nodelist[i].y,nodelist[i].z, color = 'g' )
for i in range(len(drones)):
    for j in range(len(drones[i].path)):
        ax.scatter(drones[i].path[j].x, drones[i].path[j].y, drones[i].path[j].z, color = colors[i])

plt.pause(3)
plt.cla()

c = ['m', 'k', 'y']
for i in range(len(paths)):
    for j in range(len(paths[i])):
        ax.scatter(paths[i][j].x, paths[i][j].y, paths[i][j].z, color = c[i])
for i in range(len(drones)):
    for j in range(len(drones[i].pathLines)):
        for k in range(len(drones[i].pathLines[j])):
            ax.scatter(drones[i].pathLines[j][k].x, drones[i].pathLines[j][k].y, drones[i].pathLines[j][k].z)


plt.show()
