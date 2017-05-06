import argparse
import os
import re
import itertools
import json

import numpy


def get_output_filepath(directory, filename):
    return os.path.join(directory, filename)


def get_full_path(directory, filename):
    return os.path.join(directory, filename)


def get_file_average(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        runtimes = list()
        for line in lines:
            runtimes.append(float(line.strip().split(',')[0]))
        average_runtime = numpy.average(runtimes)
    return average_runtime


def get_json_name(filename):
    fname = '{}_results.json'.format(filename)
    return fname

is_graph_file = lambda filename: filename.endswith('.graph')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_dir", help="graph file directory to process", type=str)
    args = parser.parse_args()

    pattern = '^sig_target_\d+_'
    pattern_single_file = '^sig_target_\d_'

    gr_files_list = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))
    gr_files_list = list(gr_files_list)

    # find the files with a single digit between them, and rename them
    # to proper format
    for i in range(len(gr_files_list)):
        m = re.search(pattern_single_file, gr_files_list[i])
        if m is not None:
            fname = gr_files_list[i]
            new_name = '{}0{}'.format(fname[:11], fname[11:])
            old_fpath = os.path.join(args.inp_dir, fname)
            new_fpath = os.path.join(args.inp_dir, new_name)
            os.rename(old_fpath, new_fpath)

    # obtain the files list again (since we renamed them)
    gr_files_list = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))
    gr_files_list = list(gr_files_list)

    current_pattern = ""
    cweights_file_categories = list()

    categorized_files = dict()
    category_averages = dict()
    cat_av = dict()
    for gr_file_name in gr_files_list:
        m = re.search(pattern, gr_file_name)
        if m is not None:
            new_pattern = m.group(0)
            if new_pattern != current_pattern:
                cweights_file_categories.append(new_pattern)
                current_pattern = new_pattern

            if new_pattern not in categorized_files:
                categorized_files[new_pattern] = list()
                category_averages[new_pattern] = 0
                cat_av[new_pattern] = list()
            categorized_files[new_pattern].append(gr_file_name)

    for k in categorized_files.keys():
        # print(" CATEGORY :", k)
        i = 0
        file_averages = list()
        for v in categorized_files[k]:
            # print(v)
            fname = os.path.join(args.inp_dir, v)
            i += 1
            # print(i, get_file_average(fname))
            file_averages.append(get_file_average(fname))
        category_averages[k] = numpy.average(file_averages)
        # print(file_averages)
        cat_av[k] = list(file_averages)
        del file_averages[:]

    with open(get_json_name(args.inp_dir[7:]), mode='w', encoding='utf-8') as f:
        json.dump(cat_av, f)

    for category in category_averages.keys():
        print(category, category_averages[category])


if __name__ == '__main__':
    main()