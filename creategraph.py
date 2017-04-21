import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n_start", help="number of initial vertices", type=int)
    parser.add_argument("n_step", help="number of vertices to increment with", type=int)
    parser.add_argument("m_start", help="number of initial edges", type=int)
    parser.add_argument("m_step", help="number of edges to increment with", type=int)

    args = parser.parse_args()

    print(" N start: ", args.n_start)
    print(" N step: ", args.n_step)
    print(" M start: ", args.m_start)
    print(" M step: ", args.m_step)


if __name__ == '__main__':
    main()
