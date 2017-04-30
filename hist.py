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
    args = parser.parse_args()

    with open(args.filename, mode='r', encoding='utf-8') as input_file:
        runtimes = input_file.read().splitlines()
    runtimes = list(map(float, runtimes))

  
    nbins = 25
    if args.nbins:
        nbins = args.nbins

    fig, ax = plt.subplots()

    #this is the histogram
    n, bins, patches = ax.hist(runtimes, nbins, normed=1)
    

    #get mean
    mu = np.mean(runtimes)
    sigma = np.std(runtimes, ddof=1)
    var = np.var(runtimes, ddof=1)

    print('Report Statistics:\nMean: '+str(mu)+
          '\nStandard Deviation: '+str(sigma)+
          '\nVariance: '+str(var));
    
    #add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    ax.plot(bins, y, '--')
    ax.set_ylabel('Density')
    ax.set_xlabel('Runtime')
    ax.set_title(r'Histogram of Run times'+'\n$\mu='+str(mu)+'$'+
                 '\n$\sigma='+str(sigma)+'$');


    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
