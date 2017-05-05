from datetime import datetime
import subprocess
import os
import json


def run_greedy_100_times():
    trials = {}
    data = {}

    for i in range(100):
        for filename in os.listdir('graphs_to_test'):
            colors = ''
            path = 'graphs_to_test/' + filename.strip()
            start_time = datetime.now()
            subprocess.run(["./greedy " + path + " > " +
                            filename + '.results'], shell=True)
            end_time = datetime.now()
            with open(filename + '.results', 'r') as in_file:
                lines = in_file.readlines()
                colors = lines[len(lines)-1].split(' ')[0]
            subprocess.run('rm ' + filename + '.results', shell=True)
            total_time = (end_time - start_time).total_seconds()
            data[filename] = {'time': total_time, 'colors': colors}
        trials[i] = data

    with open('lab1_1a_greedy_results.json', 'w') as out_file:
        json.dump(trials, out_file)


def run_random_100_times(iterations):
    iter_data = {}
    trials = {}
    data = {}

    for iteration in range(iterations):
        for i in range(100):
            for filename in os.listdir('graphs_to_test'):
                colors = ''
                path = 'graphs_to_test/' + filename.strip()
                start_time = datetime.now()
                subprocess.run(["./random " + path + ' ' + str(2**iteration) + " > " +
                                filename + '.results'], shell=True)
                end_time = datetime.now()
                with open(filename + '.results', 'r') as in_file:
                    lines = in_file.readlines()
                    colors = lines[len(lines) - 1].split(' ')[0]
                subprocess.run('rm ' + filename + '.results', shell=True)
                total_time = (end_time - start_time).total_seconds()
                data[filename] = {'time': total_time, 'colors': colors}
            trials[i] = data
        iter_data['iteration_' + str(iteration)] = trials
        with open('lab1_1a_random_results.json', 'w') as out_file:
            json.dump(iter_data, out_file)

run_random_100_times(7)
