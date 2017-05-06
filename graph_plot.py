import argparse
import os

import matplotlib.pyplot as plt


def get_output_filename(inp_fname):
    return inp_fname.replace('output', 'graph.png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_file", help="input file whose data should be plotted", type=str)
    args = parser.parse_args()

    with open(args.inp_file, mode='r', encoding='utf-8') as input_file:
        file_content = input_file.readlines()

    x_vals = list()
    y_vals = list()
    for line in file_content:
        x, y = line.strip().split(' ')
        x_vals.append(int(x[11:-1]))
        y_vals.append(y)

    for a, b in zip(x_vals, y_vals):
        print(a, b)

    print(y)

    plt.plot(x_vals, y_vals, marker='o')
    plt.xlabel('{} setting'.format(args.inp_file))
    plt.ylabel('runtime (millisecond)')
    fig = plt.gcf()
    plt.show()
    # fig.savefig('{}.png'.format(args.inp_file), dpi=100)
    fig.savefig(get_output_filename(args.inp_file))

if __name__ == '__main__':
    main()
