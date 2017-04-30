from datetime import datetime
import subprocess

times = [0 for _ in range(100)]
for i in range(1, 101):
    for j in range(100):
        graph_file = str(i)+'.graph'
        graph_filename = '/graphs/'+graph_file

        starttime = datetime.now()
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        endtime = datetime.now()

        total_time = (endtime - starttime).total_seconds()
        times[i-1] += float(total_time)
        #  print(total_time, graph_filename)

with open('100_graphs_100_runs_each', 'w') as out_file:
    for time in times:
        time /= 100

        out_file.writelines(str(time)+'\n')
