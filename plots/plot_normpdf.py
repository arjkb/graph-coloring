import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mu_random = 11.1583048
variance_random = 196.727154981
sigma_random = math.sqrt(variance_random)
x = np.linspace(-40, 60, 1000)
plt.plot(x, mlab.normpdf(x, mu_random, sigma_random))

mu_greedy = 6.2415048
variance_greedy = 48.5366983534
sigma_greedy = math.sqrt(variance_greedy)
y = np.linspace(-40, 60, 1000)
plt.plot(y, mlab.normpdf(y, mu_greedy, sigma_greedy))

plt.show()
