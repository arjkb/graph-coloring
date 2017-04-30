import os
import subprocess
import argparse

from datetime import datetime


def is_graph_file(filename):
    return filename.endswith(".graph")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="name of the output file", type=str)
    parser.add_argument("-v", "--verbose", help="show full output", action="store_true")
    parser.add_argument("-l", "--limited", help="show limited output", action="store_true")
    parser.add_argument("-q", "--quiet", help="show no output", action="store_true")
    parser.add_argument("-r", "--runs", help="number of times the entire program must be run", type=int)    
    args = parser.parse_args()

    # grab the graph files -- the ones with .graph extension
    graph_files = filter(is_graph_file, sorted(os.listdir('outputs/')) )

    op_filename = args.filename + ".greedy"
    op_filepath = os.path.join('outputs/', op_filename)



    if args.runs:
        total_runs = args.runs
    else:
        total_runs = 1

    count = 0
    for graph_file in graph_files:
        count += 1
        graph_filename = os.path.join('outputs/', graph_file)

        starttime = datetime.now()
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        endtime = datetime.now()
        total_time = (endtime - starttime).total_seconds()
        print(total_time)

        if args.verbose:
            print(" Runcount {}: ./greedy {} >> {}"
                            .format(count, graph_file, op_filename))
        elif args.limited:
            if (count % 1000) == 0:
                print(" Running count {}: ./greedy {} >> {}"
                      .format(count, graph_file, op_filename))

        with open(op_filepath, mode='a', encoding='utf-8') as output_file:
            output_file.write(greedy_result.stdout)


if __name__ == '__main__':
    main()
