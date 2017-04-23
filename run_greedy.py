import os
import subprocess


def is_graph_file(filename):
    if filename.endswith(".graph"):
        return True
    else:
        return False

def main():
    # grab the graph files -- the ones with .graph extension
    graph_files = filter(is_graph_file, sorted(os.listdir('outputs/')) )

    for graph_file in graph_files:
        print(graph_file)
        # graph_filename = os.path.join('outputs/', graph_file)
        # op_filename = graph_file[:-4] + ".greedy"
        #
        # op_filepath = os.path.join('outputs/', op_filename)
        # greedy_result = subprocess.run(["./greedy", graph_filename],
        #                                     encoding='utf-8',
        #                                     stdout=subprocess.PIPE)
        # print(op_filename)
        # with open(op_filepath, mode='w', encoding='utf-8') as output_file:
        #     output_file.write(greedy_result.stdout)


if __name__ == '__main__':
    main()