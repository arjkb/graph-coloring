import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


with open('timestamp.greedy_time.txt', 'r') as in_file:
    data = in_file.readlines()
    data_array = []
    for datum in data:
        data_array.append(float(datum))

    mu = sum(data_array) / len(data_array)
    sigma = 15  # standard deviation of distribution
    num_bins = 25

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(data_array, num_bins)
    #
    # # add a 'best fit' line
    # y = mlab.normpdf(bins, mu, sigma)
    # ax.plot(bins, y, '--')
    # ax.set_xlabel('Smarts')
    # ax.set_ylabel('Probability density')
    # ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()