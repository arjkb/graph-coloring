import argparse
import subprocess
import os


def write_to_file(filepath, content):
    with open(filepath, mode='w', encoding='utf-8') as output_file:
        output_file.write(content)


def get_total_runs(runs_argument):
    if runs_argument:
        return runs_argument
    else:
        return 1


def run_c_program(program_params_list):
    return subprocess.run(program_params_list, encoding='utf-8', stdout=subprocess.PIPE)


def generate_filename(prefix, n, m):
    return "{}_n{}_m{}.graph".format(prefix, n, m)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="directory to output files to", type=str)
    parser.add_argument("output", help="output file prefix", type=str)
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_finish", help="number of final vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment each iteration", type=int)
    parser.add_argument("-r", "--runs", help="number of total iterations of the graph generation", type=int)
    parser.add_argument("--verbose", help="show all output", action="store_true")
    args = parser.parse_args()

    total_runs = get_total_runs(args.runs)

    print(" Output file prefix: ", args.output)
    print(" N start: ", args.n_start)
    print(" N finish: ", args.n_finish)
    print(" N step: ", args.n_step)
    print(" Total runs: ", total_runs)
    print(" Creating graphs...")

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
                count, m_count = count + 1, m_count + 1

                filepath = os.path.join(args.output_dir, generate_filename(filename_prefix, n, m))

                if args.verbose:
                    print(" Count: {} ({}, {}) Filename: {}".format(count, n, m, filepath))

                randomgraph_result = run_c_program(["./randomgraph", str(n), str(m), str(count)])
                write_to_file(filepath, randomgraph_result.stdout)
                if m_count == 10:
                    break

    print("\n Created {} sets of {} graphs in {}/ directory"
                                    .format(total_runs, count/total_runs, args.output_dir))
    print(" Total number of graphs: {}".format(count))
    print()


if __name__ == '__main__':
    main()
