import argparse
import os

is_graph_file = lambda filename: filename.endswith('.graph')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp_dir", help="graph file directory to process", type=str)
    parser.add_argument("out_dir", help="output directory", type=str)
    args = parser.parse_args()

    print(args.inp_dir)
    print(args.out_dir)

    gr_files = filter(is_graph_file, sorted(os.listdir(args.inp_dir)))

    # i = 0
    # for f in gr_files:
    #     print(i, f)
    #     i += 1

    i = 0
    file_count = 0
    for gr_file in gr_files:
        # read the 100 tuples
        # Find median
        file_count += 1
        gr_file_path = os.path.join(args.inp_dir, gr_file)
        with open(gr_file_path, mode='r', encoding='utf-8') as graph_file:
            lines = graph_file.readlines()
            print(i, lines)
        print(type(lines), len(lines))
        # break
    print(file_count)


if __name__ == '__main__':
    main()
