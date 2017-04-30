import os
import subprocess
import argparse
from datetime import datetime


def is_graph_file(filename):
    return filename.endswith(".graph")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory which contains the graphs", type=str)
    args = parser.parse_args()

    graph_files = filter(is_graph_file, sorted(os.listdir(args.directory)))

    count = 0

    if args.runs:
        total_time = args.runs
    else:
        total_time = 1

    for graph_file in graph_files:
        count += 1
        graph_filename = os.path.join(args.directory, graph_file)

        starttime = datetime.now()
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        endtime = datetime.now()

        total_time = (endtime - starttime).total_seconds()
        print(total_time, graph_filename)


if __name__ == '__main__':
    main()

