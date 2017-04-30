import numpy as np
import argparse
from scipy.stats import ttest_ind, ttest_ind_from_stats


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename1",
                        help="full path to the input file that contains an array",
                        type=str)

    parser.add_argument("filename2",
                        help="full path to the input file that contains an array",
                        type=str)

    
    args = parser.parse_args()

    with open(args.filename1, mode='r', encoding='utf-8') as input_file:
        a = input_file.read().splitlines()
    a = list(map(float, a))

    with open(args.filename2, mode='r', encoding='utf-8') as input_file:
        b = input_file.read().splitlines()
    b = list(map(float, b))
  
   
    #get stats
    mu1 = np.mean(a)
    sigma1 = np.std(a)
    var1 = np.var(a)
    mu2 = np.mean(b)
    sigma2 = np.std(b)
    var2 = np.var(b)


    print('\nDataSet 1 Statistics:\nMean: '+str(mu1)+
          '\nStandard Deviation: '+str(sigma1)+
          '\nVariance: '+str(var1)+'\n');
    print('\nDataSet 2 Statistics:\nMean: '+str(mu2)+
          '\nStandard Deviation: '+str(sigma2)+
          '\nVariance: '+str(var2)+'\n');
    

    t, p = ttest_ind(a, b, equal_var=False)
    print("\nttest_ind:            t = %g  p = %g" % (t, p))

if __name__ == '__main__':
    main()
