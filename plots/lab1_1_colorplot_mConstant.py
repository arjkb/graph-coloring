import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
def roundup(x):
    return int(math.ceil(x /10.0)) *10

NUM_COLORS = 10

with open("lab1_1_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()

i = 0;

colors = [[] for y in range(100)]
n = [[] for y in range(100)]

for x in range (0, 100):
    iter = trials[x].split(" ")
    nodes = int(iter[0])
    edges = float((float(iter[1]))/(float((nodes*(nodes-1))/2)) *100);
    print(roundup(edges))
    index = (roundup(edges)/10) -1
    colors[index].append(float(iter[2]))
    n[index].append(int(iter[0]))

cm = plt.get_cmap('gist_rainbow')
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(10,100)
ax.set_ylim(0,110)


    
for x in range (0, 10):
    print(str(x) + " : " + str(n[x])+"\n")
    plt.scatter(n[x], colors[x], color=(cm(1.*x/NUM_COLORS)))
    ax.plot(np.unique(n[x]), np.poly1d(np.polyfit(n[x], colors[x], 1))(np.unique(n[x])), label = "m="+str((x+1)*10)+"%")


plt.suptitle('Average Number of Colors')
plt.xlabel('n')
plt.ylabel('Colors')
plt.legend(loc=2)
plt.show();
