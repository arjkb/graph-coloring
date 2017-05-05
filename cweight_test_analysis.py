import argparse
import os
import numpy


def get_output_filepath(directory, filename):
    return os.path.join(directory, filename)

is_graph_file = lambda filename: filename.endswith('.graph')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_dir", help="graph file directory to process", type=str)
    parser.add_argument("out_dir", help="output directory", type=str)
    args = parser.parse_args()

    print(" Input directory: ", args.inp_dir)
    print(" Output directory: ", args.out_dir)

    gr_files_list = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))

    for gr_file_name in gr_files_list:
        gr_file_path = os.path.join(args.inp_dir, gr_file_name)
        with open(gr_file_path, mode='r', encoding='utf-8') as graph_file:
            lines = graph_file.readlines()
            a_list = list()
            for line in lines:
                # each line is comma-separated. Get the first value of those
                a_list.append(float(line.strip().split(',')[0]))
            average = numpy.average(a_list)
            std_dev = numpy.std(a_list, ddof=1)
            variance = numpy.var(a_list, ddof=1)
            median = numpy.median(a_list)
            summary_line = "{} {} {} {}".format(average, median, std_dev, variance)

            op_file_path = get_output_filepath(args.out_dir, gr_file_name.replace('.graph', '.summary'))
            with open(op_file_path, mode='w', encoding='utf-8') as output_file:
                output_file.write(summary_line)


if __name__ == '__main__':
    main()