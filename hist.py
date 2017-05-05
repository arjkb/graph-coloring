import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        help="full path to the input file that contains an array",
                        type=str)
    parser.add_argument("--nbins",
                        help="number of bins in the histogram. (def=25)",
                        type=int)

    parser.add_argument("--title",
                        help="number of bins in the histogram. (def=25)",
                        type=str)

    parser.add_argument("--xlabel",
                        help="number of bins in the histogram. (def=25)",
                        type=str)

    
    args = parser.parse_args()

    with open(args.filename) as input_file:
        runtimes = input_file.read().splitlines()
    runtimes = list(map(float, runtimes))

  
    nbins = 25
    if args.nbins:
        nbins = args.nbins

    fig, ax = plt.subplots()

    #this is the histogram
    n, bins, patches = ax.hist(runtimes, nbins)


    #get mean
    mu = np.mean(runtimes)
    sigma = np.std(runtimes, ddof=1)
    var = np.var(runtimes, ddof=1)

    #add a 'best fit' line
    ax.set_ylabel('Density')
    if args.xlabel:
        ax.set_xlabel(args.xlabel)
    ax.set_title(r'100 Graphs 100 runs each'+'\n$\mu='+str(mu)+'$'+
                     '\n$\sigma='+str(sigma)+'$'+
                     '\n$\sigma^2='+str(var)+'$');

    print('Report Statistics:\nMean: '+str(mu)+
          '\nStandard Deviation: '+str(sigma)+
          '\nVariance: '+str(var));
    


    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
