import argparse
import os
import re
import itertools

import numpy


def get_output_filepath(directory, filename):
    return os.path.join(directory, filename)


def get_file_average(filename, h_index):
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        runtimes = list()
        for line in lines:
            runtimes.append(float(line.strip().split(',')[h_index]))
        average_runtime = numpy.average(runtimes)
    return average_runtime


is_graph_file = lambda filename: filename.endswith('.graph')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_dir", help="graph file directory to process", type=str)
    # parser.add_argument("out_dir", help="output directory", type=str)
    args = parser.parse_args()

    # pattern = '^sig_initpolicy_\d+_M'

    pattern_1 = '^sig_initpolicy_3_M0_n\d+_'
    pattern_2 = '^sig_initpolicy_3_M0_n\d+_'
    pattern_3 = '^sig_initpolicy_3_M0_n\d+_'

    pattern_double_digit = '^sig_initpolicy_3_M0_n\d\d_'

    # print(" Input directory: ", args.inp_dir)
    # print(" Output directory: ", args.out_dir)

    gr_files_list = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))
    gr_files_list = list(gr_files_list)

    # find the files with a single digit between them, and
    # rename them to proper format
    for i in range(len(gr_files_list)):
        m = re.search(pattern_double_digit, gr_files_list[i])
        if m is not None:
            fname = gr_files_list[i]
            new_name = '{}0{}'.format(fname[:21], fname[21:])
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
    cat_f_col_avg = dict()
    cat_i_col_avg = dict()
    cat_col_difference = dict()
    for gr_file_name in gr_files_list:
        m = re.search(pattern_1, gr_file_name)
        if m is not None:
            new_pattern = m.group(0)
            if new_pattern != current_pattern:
                cweights_file_categories.append(new_pattern)
                current_pattern = new_pattern

            if new_pattern not in categorized_files:
                categorized_files[new_pattern] = list()
                category_averages[new_pattern] = 0
                cat_f_col_avg[new_pattern] = 0
                cat_i_col_avg[new_pattern] = 0
            categorized_files[new_pattern].append(gr_file_name)

    for k in categorized_files.keys():
        # print(k)
        file_final_color_average = list()
        file_initial_color_average = list()
        file_col_diff_average = list()
        for v in categorized_files[k]:
            # print(v)
            fname = os.path.join(args.inp_dir, v)
            file_final_color_average.append(get_file_average(fname, 2))
            file_initial_color_average.append(get_file_average(fname, 4))
            file_col_diff_average.append(get_file_average(fname, 4) - get_file_average(fname, 2))
        # print(k, file_final_color_average)
        # print(k, file_initial_color_average)
        # print(k, file_col_diff_average)
        cat_f_col_avg[k] = numpy.average(file_final_color_average)
        cat_i_col_avg[k] = numpy.average(file_initial_color_average)
        cat_col_difference[k] = numpy.average(file_col_diff_average)
        # print(len(file_final_color_average))

    for k in cat_col_difference:
        print(k, cat_col_difference[k])


    # for k in cat_f_col_avg:
    #     print(cat_f_col_avg[k])

    # for k in categorized_files.keys():
    #     # print(" CATEGORY :", k)
    #     i = 0
    #     file_averages = list()
    #     for v in categorized_files[k]:
    #         # print(v)
    #         fname = os.path.join(args.inp_dir, v)
    #         i += 1
    #         # print(i, get_file_average(fname))
    #         file_averages.append(get_file_average(fname))
    #     category_averages[k] = numpy.average(file_averages)
    #     del file_averages[:]
    #
    # for category in category_averages.keys():
    #     print(category, category_averages[category])


if __name__ == '__main__':
    main()