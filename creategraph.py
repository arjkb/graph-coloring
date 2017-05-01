import argparse
import subprocess
import os

import math

def write_to_file(filepath, content):
    with open(filepath, mode='w', encoding='utf-8') as output_file:
        output_file.write(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="directory to output files to", type=str)
    parser.add_argument("output", help="output file prefix", type=str)
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_finish", help="number of final vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment each iteration", type=int)
    parser.add_argument("-r", "--runs", help="number of total iterations of the graph generation", type=int)
    parser.add_argument("--verbose", help="show all output", action="store_true")
    parser.add_argument("--limited", help="show all output", action="store_true")

    args = parser.parse_args()

    print(" Output file prefix: ", args.output)
    print(" N start: ", args.n_start)
    print(" N finish: ", args.n_finish)
    print(" N step: ", args.n_step)
    print(" Creating graphs...")

    total_runs = 1
    if args.runs:
        total_runs = args.runs
    else:
        total_runs = 1

    count = 0
    for run_count in range(total_runs):
        filename_prefix = args.output + str(run_count)

        for n in range(args.n_start, args.n_finish + 1, args.n_step):
            m_max = int(n*(n-1)/2)
            m_start = int(0.10 * m_max)
            m_10perc = int(0.10 * m_max)
            m_end = int(1.00 * m_max)

            if args.verbose:
                print(" For n = {}, m_start={}, m_end={}".format(n, m_start, m_end))

            m_count = 0
            for m in range(m_start, m_end + 1, m_10perc):
                count += 1
                m_count += 1

                filename = "{0}_n{1}_m{2}.graph".format(filename_prefix, n, m)
                filepath = os.path.join(args.output_dir, filename)

                if args.verbose:
                    print(" Count: {} ({}, {}) Filename: {}".format(count, n, m, filename))
                elif args.limited and (count % 1000 == 0):
                    print(" Count: {} ({}, {}) Filename: {}".format(count, n, m, filename))

                randomgraph_result = subprocess.run(["./randomgraph", str(n), str(m), str(count)],
                                                    encoding='utf-8',
                                                    stdout=subprocess.PIPE)

                write_to_file(filepath, randomgraph_result.stdout)

                # with open(filepath, mode='w', encoding='utf-8') as output_file:
                #     output_file.write(randomgraph_result.stdout)
                #     randomgraph_result = None
                if m_count == 10:
                    break

    print("\n Created {} sets of {} graphs in {}/ directory"
                                    .format(total_runs, count/total_runs, args.output_dir))
    print(" Total number of graphs: {}".format(count))
    print()


if __name__ == '__main__':
    main()
