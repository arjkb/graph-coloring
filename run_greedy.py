import os
import subprocess
import argparse


def is_graph_file(filename):
    return filename.endswith(".graph")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="show full output", action="store_true")
    parser.add_argument("-l", "--limited", help="show limited output", action="store_true")
    parser.add_argument("-q", "--quiet", help="show no output", action="store_true")
    args = parser.parse_args()

    # grab the graph files -- the ones with .graph extension
    graph_files = filter(is_graph_file, sorted(os.listdir('outputs/')) )

    count = 0

    for graph_file in graph_files:
        # print(graph_file)
        count += 1
        graph_filename = os.path.join('outputs/', graph_file)
        op_filename = graph_file[:-6] + ".greedy"  # set the .greedy extension
        op_filepath = os.path.join('outputs/', op_filename)
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        # print(op_filename) if args.verbose else None

        if args.verbose:
            print(" Running count {}: ./greedy {} > {}"
                            .format(count, graph_file, op_filename))
        elif args.limited:
            if (count % 1000) == 0:
                print(" Running count {}: ./greedy {} > {}"
                      .format(count, graph_file, op_filename))

        with open(op_filepath, mode='w', encoding='utf-8') as output_file:
            output_file.write(greedy_result.stdout)


if __name__ == '__main__':
    main()

