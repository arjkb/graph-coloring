import argparse
import os

import matplotlib.pyplot as plt


def get_output_filename(inp_fname):
    return inp_fname.replace('output', 'graph.png')


def get_x_value(graph_type, x):
    if graph_type == "trials":
        return int(x[11:-1])
    elif graph_type == "initpolicy":
        return int(x[21:-1])
    elif graph_type == "maxiter":
        return int(x[12: -1])
    elif graph_type == "revert":
        return int(x[11:-1])
    elif graph_type == "target":
        return int(x[11:-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("graph_type", help="type of graphs (eg., cweights, trials etc)", type=str)
    parser.add_argument("inp_file", help="input file whose data should be plotted", type=str)
    parser.add_argument("init_file2", help="init policy 2 file", type=str)
    parser.add_argument("init_file3", help="init policy 3 file", type=str)
    args = parser.parse_args()

    initpolicy_files = list()
    if args.graph_type == "initpolicy":
        initpolicy_files.append(args.inp_file)
        initpolicy_files.append(args.init_file2)
        initpolicy_files.append(args.init_file3)

        x_vals = dict()
        y_vals = dict()
        for file in initpolicy_files:
            with open(file, mode='r', encoding='utf-8') as input_file:
                file_content = input_file.readlines()

            x_vals[file] = list()
            y_vals[file] = list()
            for line in file_content:
                x, y = line.strip().split(' ')
                x_vals[file].append(get_x_value(args.graph_type, x))
                y_vals[file].append(y)

    # plt.plot(x_vals[args.inp_file], y_vals[args.inp_file], marker='o',
    #          x_vals[args.init_file2], y_vals[args.init_file2], marker='o',
    #          x_vals[args.init_file3], y_vals[args.init_file3], marker='o',
    #          )

    plt.plot(x_vals[args.inp_file], y_vals[args.inp_file],
             x_vals[args.init_file2], y_vals[args.init_file2],
             x_vals[args.init_file3], y_vals[args.init_file3],
             marker='o'
             )
    plt.xlabel('Number of nodes'.format(args.inp_file))
    plt.ylabel('Difference in color')
    fig = plt.gcf()
    plt.show()
    # fig.savefig('{}.png'.format(args.inp_file), dpi=100)
    fig.savefig(get_output_filename(args.inp_file))

    fig.savefig('initpolicy_plot.png')

if __name__ == '__main__':
    main()
