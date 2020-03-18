from MAIN.functions.functions import *
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



def rrt(drone, target):
    possibleToConnect = False

    if node_distance(node1 = drone.position, node2 = target) <= drone.size:
        drone.RRTfinished = True
    else: drone.RRTfinished = False

    goalSampleRate = 100
    minRandX = minRandY =minRandZ = -500
    maxRandX = maxRandY =  maxRandZ = 500
    if drone.RRTfinished == True: pass
    else:
        while possibleToConnect == False :


            randomNode = get_random_node(goalSampleRate = goalSampleRate, goalNode=target,
                                         minRandx = minRandX, maxRandx = maxRandX ,
                                         minRandy = minRandY, maxRandy= maxRandY ,
                                        minRandz = minRandZ, maxRandz = maxRandZ )
            check_nearest(node1 = randomNode, nodeList=drone.nodeList)
            newnode = make_step(nodef = drone.position, nodet=randomNode, stepx = drone.accelerationX, stepy = drone.accelerationY, stepz = drone.accelerationZ)

            print(randomNode.x, randomNode.y, randomNode.z)



            if node_obstacle_collision(node1 = newnode, obstacles=drone.obstacles) or drone_collision(drone = drone, node1 = newnode):
                goalSampleRate = 0
                possibleToConnect = False

            else:
                goalSampleRate = 100
                newnode.parent = drone.nodeList[len(drone.nodeList) - 1]
                drone.nodeList.append(newnode)
                drone.position = newnode
                possibleToConnect = True

            if node_distance(drone.position, target) <= drone.size:
                drone.RRTfinished = True
                drone.nodeList.append(target)
                drone.path = generate_final_course(gnode = target, nodelist = drone.nodeList)

            if drone.annimation:
                ax.scatter(newnode.x, newnode.y, newnode.z, color = 'g')
                plt.pause(0.001)




