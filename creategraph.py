import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_iter", help="number of iterations for vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment each iteration", type=int)
    parser.add_argument("m_start", help="number of initial edges", type=int)
    parser.add_argument("m_iter", help="number of iterations for edges", type=int)
    parser.add_argument("m_step", help="number of edges to increment each iteration", type=int)
    parser.add_argument("-s", "--seed", help="seed value for randomgraph", type=int)

    args = parser.parse_args()

    print(" N start: ", args.n_start)
    print(" N iter: ", args.n_iter)
    print(" N step: ", args.n_step)

    print(" M start: ", args.m_start)
    print(" M iter: ", args.m_iter)
    print(" M step: ", args.m_step)

    if args.seed:
        print(" Seed: ", args.seed)
    else:
        print(" Seed NOT present")

    randomgraph_result = subprocess.run(["./randomgraph", str(args.n_start), str(args.m_start)],
                                        encoding='utf-8',
                                        stdout=subprocess.PIPE)
    print(randomgraph_result.stdout)


if __name__ == '__main__':
    main()
