import json


with open('lab1_1a_greedy_results.json') as data_file:
    data = json.load(data_file)
    for i in range(100):
        print(data[str(i)].items())
print(2)
