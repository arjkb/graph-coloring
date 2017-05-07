import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

NUM_COLORS = 10

def roundup(x):
    return int(math.ceil(x /10.0)) *10

with open("lab1_1_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()

i = 0;

time = [100]
n = [100]

for x in range (0, 100):
    iter = trials[x].split(" ")
    time.append(float(iter[3]))
    n.append(int(iter[0]))

cm = plt.get_cmap('gist_rainbow')
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(10,100)
ax.set_ylim(0,20)
    
for x in range (0, 10):
    plt.scatter(n, time, color=(cm(1.*5/NUM_COLORS)))
    ax.plot(np.unique(n), np.poly1d(np.polyfit(n, time, 1))(np.unique(n)))

for x in range (0, 100):
    print(str(n[x])+","+str(time[x]))

plt.suptitle('Runtime average')
plt.xlabel('Nodes')
plt.ylabel('Runtime in Milliseconds')
plt.legend(loc=2)
plt.show()

