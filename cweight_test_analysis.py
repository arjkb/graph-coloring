import argparse
import os
import re
import itertools

import numpy


def get_output_filepath(directory, filename):
    return os.path.join(directory, filename)


def get_file_average(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        runtimes = list()
        print("Opening!")
        for line in lines:
            runtimes.append(float(line.strip().split(',')[0]))
        average_runtime = numpy.average(runtimes)
    return average_runtime


is_graph_file = lambda filename: filename.endswith('.graph')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_dir", help="graph file directory to process", type=str)
    parser.add_argument("out_dir", help="output directory", type=str)
    args = parser.parse_args()

    pattern = '^sig_cweights_\d\.\d+_\d\.\d+_\d\.\d+_\d\.\d+_\d\.\d+_\d\.\d+'

    print(" Input directory: ", args.inp_dir)
    print(" Output directory: ", args.out_dir)

    gr_files_list = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))

    gr_files_list_it1, gr_files_list_it2 = itertools.tee(gr_files_list, 2)

    # find all the categories
    # for each category
    ## grab all the files in the category
    ## find the averages of all runtimes for each file in a category
    ## -- save it into a list
    ## find the

    count = 0
    new_pattern = ""
    current_pattern = ""
    cweights_file_categories = list()

    categorized_files = dict()
    for gr_file_name in gr_files_list_it1:
        m = re.search(pattern, gr_file_name)
        if m is not None:
            new_pattern = m.group(0)
            if new_pattern != current_pattern:
                cweights_file_categories.append(new_pattern)
                current_pattern = new_pattern

            if new_pattern not in categorized_files:
                categorized_files[new_pattern] = list()

            categorized_files[new_pattern].append(gr_file_name)

    for k in categorized_files.keys():
        print(" CATEGORY :", k)

        for v in categorized_files[k]:
            print(v)


if __name__ == '__main__':
    main()