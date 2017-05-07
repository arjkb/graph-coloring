import json
import scipy.stats as scipy
import numpy as np
import re
with open('lab1_1a_random_results.json') as data_file:    
    data = json.load(data_file)

results = [[[0 for i in range(12)] for x in range(100)] for y in range(100)]

for i in range(0,12):
    iteration = data["iteration_"+str(i)] 
    
    for x in range (0, 100):
        iter = iteration[str(x)]
        for y in range (0, 100):
            graphstring = iter.keys()[y]
            graphstringclean = re.sub("[^0-9+_]","",graphstring)
            graphstringclean = graphstringclean.split("_")
            n = graphstringclean[1]
            m = graphstringclean[2]
            colors = int(iter[graphstring]['colors'])
            time = float(iter[graphstring]['time'])
            results[x][y][i] = str(n)+ " "+str(m) +" "+ str(colors)+ " "+ str(time) + " "+ str(i)


            
for x in range (0,100):
    c= []
    t = []
    for y in range(0,100):
        iter = results[y][x][(int(i))].split(" ")
        n = iter[0]
        m = iter[1]
        i= 7
        c.append(int(iter[2]))
        t.append((float(iter[3]))*1000)
c_mean = np.mean(c)
c_std = np.std(c, ddof=1)
t_std = np.std(t, ddof=1)
c_skew = scipy.skew(c)
t_skew = scipy.skew(t)
c_kurt = scipy.kurtosis(c)
t_kurt = scipy.kurtosis(t)
t_skew = scipy.kurtosis(t)
t_mean = np.mean(t)
c_var = np.var(c, ddof=1)
t_var = np.var(t, ddof=1)

print("---------Random (i=2^7)-----------")

print("Color Stats:\nMean:"+str(c_mean)+"\nStd:"+str(c_std)
      +"\nVar:"+str(c_var)+"\nSkew:"+str(c_skew)+"\nKurtosis:"+
      str(c_kurt) + "\n")
print("Time Stats:\nMean:"+str(t_mean)+"\nStd:"+str(t_std)
      +"\nVar:"+str(t_var)+"\nSkew:"+str(t_skew)+"\nKurtosis:"+
      str(t_kurt))

with open('lab1_1a_greedy_results.json') as data_file:    
    data = json.load(data_file)

results = [[0 for x in range(100)] for y in range(100)] 
    
for x in range (0, 100):
    iter = data[str(x)]
    for y in range (0, 100):
        graphstring = iter.keys()[y]
        graphstringclean = re.sub("[^0-9+_]","",graphstring)
        graphstringclean = graphstringclean.split("_")
        n = graphstringclean[1]
        m = graphstringclean[2]
        colors = int(iter[graphstring]['colors'])
        time = float(iter[graphstring]['time'])
        results[x][y] = str(n)+ " "+str(m) +" "+ str(colors)+ " "+ str(time)


for x in range (0,100):
    c= []
    t = []
    for y in range(0,100):
        iter = results[y][x].split(" ")
        n = iter[0]
        m = iter[1]
        c.append(int(iter[2]))
        t.append((float(iter[3]))*1000)
c_mean = np.mean(c)
c_std = np.std(c, ddof=1)
t_std = np.std(t, ddof=1)
c_skew = scipy.skew(c)
t_skew = scipy.skew(t)
c_kurt = scipy.kurtosis(c)
t_kurt = scipy.kurtosis(t)
t_skew = scipy.kurtosis(t)
t_mean = np.mean(t)
c_var = np.var(c, ddof=1)
t_var = np.var(t, ddof=1)

print("\n\n---------Greedy-----------")

print("Color Stats:\nMean:"+str(c_mean)+"\nStd:"+str(c_std)
      +"\nVar:"+str(c_var)+"\nSkew:"+str(c_skew)+"\nKurtosis:"+
      str(c_kurt) + "\n")
print("Time Stats:\nMean:"+str(t_mean)+"\nStd:"+str(t_std)
      +"\nVar:"+str(t_var)+"\nSkew:"+str(t_skew)+"\nKurtosis:"+
      str(t_kurt)+"\n\n")
            
