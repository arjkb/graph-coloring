import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def roundup(x):
    return int(math.ceil(x /10.0)) *10

with open("lab1_1_random_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()


n = 100

NUM_COLORS = 10

colors = [[]for x in range(10)]
iterations = [[]for x in range(10)]

for x in range (0, 1200):
    iter = trials[x].split(" ")
        
    if (int(iter[0]) == n):
        nodes = int(iter[0])
        maxedges = float(nodes*(nodes-1))/2
        edges = float(iter[1])
        percent = (edges/maxedges)*100
        index = (roundup(percent)/10) -1
        colors[index].append(float(iter[2]))
        iterations[index].append(int(iter[6]))



cm = plt.get_cmap('gist_rainbow')    
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(0,12)

for x in range (0, 10):
    plt.scatter(iterations[x], colors[x], color=(cm(1.*x/NUM_COLORS)))
    plt.plot(iterations[x], colors[x],label = "m="+str((x+1)*10) + "%")
    #ax.plot(np.unique(iterations[x]), np.poly1d(np.polyfit(iterations[x], time[x], 1))(np.unique(m[x])), label = "n="+str((x+1)*10))


plt.suptitle('Number of colors vs Iterations\nFor n = '+str(n))
plt.xlabel('log$2$ of Number of Iterations')
plt.ylabel('Number of colors')
plt.legend(loc=1)
plt.show();
