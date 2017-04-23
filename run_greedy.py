import os
import subprocess


def main():
    graph_files = sorted(os.listdir('outputs/'))
    for graph_file in graph_files:
        graph_filename = os.path.join('outputs/', graph_file)
        op_filename = graph_file[:-4] + ".greedy"

        op_filepath = os.path.join('outputs/', op_filename)
        greedy_result = subprocess.run(["./greedy", graph_filename],
                                            encoding='utf-8',
                                            stdout=subprocess.PIPE)
        print(op_filename)
        with open(op_filepath, mode='w', encoding='utf-8') as output_file:
            output_file.write(greedy_result.stdout)


if __name__ == '__main__':
    main()