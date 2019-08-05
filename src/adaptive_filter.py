
import numpy as np
from nptdms import TdmsFile
import matplotlib.pyplot as plt
import glob
import scipy.io
import time
from numba import jit

# Adaptive Filter(NLMS)
@jit
def nlms(d, x, N, mu):
    # inputs
    #   d: Desired response
    #   x: Input data
    #   N: Filter length
    #   mu: step size
    # output
    #   s: output data(signal)

    # signal length
    L = len(x)

    # init
    phi = np.zeros(N)
    w = np.zeros(N)
    s = np.zeros(L)
    
    # Adaptive Filter(NLMS)
    for i, x_i in enumerate(x):
        # phi: The vector of buffered input data at step i
        phi[1:] = phi[0:-1]
        phi[0] = x_i

        # error
        e = d[i] - np.dot(w, phi)
        
        # filter update
        w = w + mu * e / (0.01 + np.dot(phi, phi)) * phi

        s[i] = e

    return s

if __name__ == '__main__':
    print()