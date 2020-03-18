import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from MAIN.input.input import *
from MAIN.algorithms.rrt import rrt
from MAIN.functions.functions import *
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


while True:
    check = []
    for j in range(len(drones)):
        rrt(drone = drones[j], target=drones[j].finish)
        check.append(drones[j].RRTfinished)

    if all(check) : break


"""
for j in range(len(drones)):
    drones[j].draw_line(start = drones[j].position,end = drones[j].finish)

for j in range(len(drones)):
    for k in range(len(drones)):
        if k==j : pass
        elif get_interception_point(line1 = drones[j].line, line2 = drones[k].line, size1= drones[k].size ,size2 = drones[j].size).x == -666: pass
        else:
            drones[j].intercaptors.append(drones[k])
            drones[j].intercaptionPoint.append(get_interception_point(line1 = drones[j].line, line2 = drones[k].line, size1= drones[k].size ,size2 = drones[j].size))

PRMs = []
droniks = [drones[0], drones[0].intercaptors]

PRMs.append(PRM(drones =droniks, point = drones[0].intercaptionPoint[0]))
"""
print(drones[0].path)
for j in range(len(drones)):
    for k in range(len(drones[j].path)):
        ax.scatter(drones[j].path[k][0],drones[j].path[k][1], drones[j].path[k][2])

plt.show()