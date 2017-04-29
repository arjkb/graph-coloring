import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        help="full path to the input file that contains an array",
                        type=str)
    parser.add_argument("--ndigits",
                        help="number of decimal places to round to. (def=10)",
                        type=int)
    args = parser.parse_args()

    with open(args.filename, mode='r', encoding='utf-8') as input_file:
        runtimes = input_file.read().splitlines()
    runtimes = list(map(float, runtimes))

    decimal = 10
    if args.ndigits:
        decimal = args.ndigits

    # print(runtimes, type(runtimes[0]))
    print(" Variance of {} runtimes: {}".format(len(runtimes),
                                              np.around(np.var(runtimes, ddof=1), decimal)
                                              )
          )

if __name__ == '__main__':
    main()
