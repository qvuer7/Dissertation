from MAIN.node.node import node
from MAIN.drone.drone import drone

start = [[0,0,0], [100,100,0]]
goal = [[100,100, 100], [0,0,100]]
obstacleCoordinates = []
droneSize = 5
droneAcceleration_X = 10
droneAcceleration_Y = 10
droneAcceleration_Z = 10
droneMass = 1
annimation = True




startNodes = []
goalNodes = []
for i in range(len(start)):
    startNodes.append(node(x = start[i][0], y = start[i][1], z = start[i][2]))
    goalNodes.append(node(x = goal[i][0], y = goal[i][1], z = goal[i][2]))
obstacles = []
for i in range(len(obstacleCoordinates)):
    obstacles.append([node(x = obstacleCoordinates[i][0], y = obstacleCoordinates[i][1], z = obstacleCoordinates[i][2]), obstacleCoordinates[i][3]])


drones = []

for i in range(len(start)):
    drones.append(drone(start = startNodes[i], finish = goalNodes[i],
                        accelerationX=droneAcceleration_X, accelerationY=droneAcceleration_Y, accelerationZ=droneAcceleration_Z,
                        size = droneSize, mass = droneMass, obstacles = obstacles, annimation = annimation))

for i in range(len(drones)):
    for j in range(len(drones)):
        if i == j : pass
        else: drones[i].recipents.append(drones[j])