import argparse
import subprocess
import os

import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="output file prefix", type=str)
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_finish", help="number of final vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment each iteration", type=int)
    parser.add_argument("-r", "--runs", help="number of times the entire program must be run", type=int)
    parser.add_argument("--verbose", help="show all output", action="store_true")
    # parser.add_argument("m_start", help="number of initial edges", type=int)
    # # parser.add_argument("m_finish", help="number of final edges", type=int)
    # parser.add_argument("m_step", help="number of edges to increment each iteration", type=int)
    # parser.add_argument("-s", "--seed", help="seed value for randomgraph", type=int)

    args = parser.parse_args()

    print(" Output file prefix: ", args.output)

    print(" N start: ", args.n_start)
    # print(" N finish: ", args.n_finish)
    print(" N step: ", args.n_step)

    # print(" M start: ", args.m_start)
    # # print(" M finish: ", args.m_finish)
    # print(" M step: ", args.m_step)

    # if args.seed:
    #     print(" Seed: ", args.seed)
    # else:
    #     print(" Seed NOT present")

    total_runs = 1
    if args.runs:
        total_runs = args.runs
    else:
        total_runs = 1

    print(" Creating graphs...")

    count = 0
    for run_count in range(total_runs):
        filename_prefix = args.output + str(run_count)

        for n in range(args.n_start, args.n_finish, args.n_step):
            m_max = int(n*(n-1)/2)
            m_s = int(0.30 * m_max)
            m_e = int(0.60 * m_max)
            if args.verbose:
                print(" For n = {}, m_start={}, m_end={}".format(n, m_s, m_e))

            for m in range(m_s, m_e, 1):
                count += 1
                filename = "{0}_{1}_{2}.graph".format(filename_prefix, n, m)
                filepath = os.path.join('outputs/', filename)

                if args.verbose:
                    print(" Count: {} ({}, {}) Filename: {}".format(count, n, m, filename))

                randomgraph_result = subprocess.run(["./randomgraph", str(n), str(m)],
                                                    encoding='utf-8',
                                                    stdout=subprocess.PIPE)
                # print(randomgraph_result.stdout)

                with open(filepath, mode='w', encoding='utf-8') as output_file:
                    output_file.write(randomgraph_result.stdout)


    print("\n Created {} sets of {} graphs in outputs/ directory"
                                    .format(total_runs, count/total_runs))
    print(" Total number of graphs: {}".format(count))
    print()


if __name__ == '__main__':
    main()
