import numpy as np

def autocorrelation(data, k):
    """Returns the autocorrelation of the *k*th lag in a time series data.

    Parameters
    ----------
    data : one dimentional numpy array
    k : the *k*th lag in the time series data (indexing starts at 0)
    """

    # yの平均
    y_avg = np.mean(data)
    # 偏差
    dev = data - y_avg

    # 分子の計算
    sum_of_covariance = 0
    for i in range(k+1, len(data)):
        covariance =  dev[i] * ( data[i-(k+1)] - y_avg )
        sum_of_covariance += covariance

    # 分母の計算
    sum_of_denominator = np.sum(dev**2)

    if sum_of_denominator==0:
        return 0

    return sum_of_covariance / sum_of_denominator

if __name__ == '__main__':
    a = np.arange(1,11)
    b = np.tile(a, 3)
    for i in range(1,10):
        print( autocorrelation(b,i) )

