import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

NUM_COLORS = 5

with open("lab1_1_random_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()


n = [10, 10, 50, 100, 100]
m = [4, 40, 610, 495, 4950]



time = [[] for y in range(len(n))]
iterations = [[] for y in range(len(n))]

for y in range (0, (len(n))):
    for x in range (0, 1200):
        iter = trials[x].split(" ")
        
        if (int(iter[0]) == int(n[y]) and int(iter[1]) == int(m[y])):
            time[y].append(math.log(float(iter[3]),2))
            iterations[y].append(int(iter[6]))



cm = plt.get_cmap('gist_rainbow')    
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_ylim(0,15)
ax.set_xlim(0,12)

for x in range (0, 5):
    plt.scatter(iterations[x], time[x], color=(cm(1.*x/NUM_COLORS)))
    plt.plot(iterations[x], time[x],label = "n="+str(n[x])+" m="+str(m[x]))
    #ax.plot(np.unique(iterations[x]), np.poly1d(np.polyfit(iterations[x], time[x], 1))(np.unique(m[x])), label = "n="+str((x+1)*10))


plt.suptitle('Runtime Average vs Iterations')
plt.xlabel('log$2$ of Number of Iterations')
plt.ylabel('log$2$ of Runtime in Milliseconds')
plt.legend(loc=2)
plt.show();
