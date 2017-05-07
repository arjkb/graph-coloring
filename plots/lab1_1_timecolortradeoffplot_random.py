import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def roundup(x):
    return int(math.ceil(x /10.0)) *10

with open("lab1_1_random_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()


n = 50
m = 610

NUM_COLORS = 12

colors = [0 for x in range(12)]
time = [0 for x in range(12)]

for x in range (0, 1200):
    iter = trials[x].split(" ")
    if (int(iter[0]) == n and int(iter[1]) == m):
        iterations = int(iter[6])
        colors[iterations] = float(iter[2])
        time[iterations] = float(iter[3])



cm = plt.get_cmap('gist_rainbow')    
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

for x in range (0, 12):
    plt.scatter(time[x], colors[x], color=(cm(1.*x/NUM_COLORS)), zorder=1, s=120)
    plt.plot(time[x], colors[x],label = "i="+str(2**x),zorder=1)
plt.plot(time,colors, color='#000000', zorder=2, lw=2)
    #ax.plot(np.unique(iterations[x]), np.poly1d(np.polyfit(iterations[x], time[x], 1))(np.unique(m[x])), label = "n="+str((x+1)*10))


plt.suptitle('Colors vs Time\nFor n = '+str(n) + ' m = '+str(m))
plt.xlabel('Time in Milliseconds')
plt.ylabel('Number of colors')
plt.legend(loc=1)
plt.show();
