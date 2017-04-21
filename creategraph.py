import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="output file prefix", type=str)
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_finish", help="number of final vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment each iteration", type=int)
    parser.add_argument("m_start", help="number of initial edges", type=int)
    parser.add_argument("m_finish", help="number of final edges", type=int)
    parser.add_argument("m_step", help="number of edges to increment each iteration", type=int)
    parser.add_argument("-s", "--seed", help="seed value for randomgraph", type=int)

    args = parser.parse_args()

    print(" Output file prefix: ", args.output)

    print(" N start: ", args.n_start)
    print(" N finish: ", args.n_finish)
    print(" N step: ", args.n_step)

    print(" M start: ", args.m_start)
    print(" M finish: ", args.m_finish)
    print(" M step: ", args.m_step)

    if args.seed:
        print(" Seed: ", args.seed)
    else:
        print(" Seed NOT present")

    for n in range(args.n_start, args.n_finish, args.n_step):
        for m in range(args.m_start, args.m_finish, args.m_step):
            filename = "{0}_{1}_{2}.out".format(args.output, n, m)
            print("{0} {1} Filename: {2}".format(n, m, filename))

            randomgraph_result = subprocess.run(["./randomgraph", str(n), str(m)],
                                                encoding='utf-8',
                                                stdout=subprocess.PIPE)
            # print(randomgraph_result.stdout)

            with open(filename, mode='w', encoding='utf-8') as output_file:
                output_file.write(randomgraph_result.stdout)


if __name__ == '__main__':
    main()
