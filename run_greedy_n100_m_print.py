import os
import subprocess
import argparse
from datetime import datetime


def is_graph_file(filename):
    return filename.endswith(".graph")


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("filename", help="name of the output file", type=str)
    parser.add_argument("-v", "--verbose", help="show full output", action="store_true")
    parser.add_argument("-l", "--limited", help="show limited output", action="store_true")
    parser.add_argument("-q", "--quiet", help="show no output", action="store_true")
    args = parser.parse_args()

    # grab the graph files -- the ones with .graph extension
    graph_files = filter(is_graph_file, sorted(os.listdir('output_n100_m1238/')))

    # op_filename = args.filename + ".greedy_time"
    # op_filepath = os.path.join('output_n100_m1238/', op_filename)

    count = 0
    for graph_file in graph_files:
        count += 1
        graph_filename = os.path.join('output_n100_m1238/', graph_file)

        starttime = datetime.now()
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        endtime = datetime.now()

        total_time = (endtime - starttime).total_seconds()
        print(total_time, graph_filename)

        if args.verbose:
            print(" Runcount {}: ./greedy {} >> {}"
                            .format(count, graph_file, op_filename))
        elif args.limited:
            if (count % 1000) == 0:
                print(" Running count {}: ./greedy {} >> {}"
                      .format(count, graph_file, op_filename))

        # with open(op_filepath, mode='a', encoding='utf-8') as output_file:
        #     output_file.write(str(total_time) + "\n")
            # output_file.write(greedy_result.stdout)


if __name__ == '__main__':
    main()

