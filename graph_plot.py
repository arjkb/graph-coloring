import argparse
import os

import matplotlib.pyplot as plt
import numpy as np

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
        x_vals.append(x)
        y_vals.append(y)

    for a, b in zip(x_vals, y_vals):
        print(a, b)


if __name__ == '__main__':
    main()
