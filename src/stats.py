import numpy as np

# こちらは計算誤差がそこそこありそうなのでボツ
# def skew(x):
#     n = np.sqrt(len(x))
#     dif = x-x.mean()
#
#     numer = n* np.sum(dif**3)
#     denom = np.sqrt(np.sum(dif**2)**3)
#
#     return numer/denom

# 1次元データの歪度
def skew(x):
    n = float(len(x))
    coef = n/((n-1)*(n-2))
    norm = (x-x.mean()) / x.std()

    return coef * np.sum(norm**3)

# 1次元データの尖度（正規分布で0）
def kurtosis(x):
    n = float(len(x))
    coef = n*(n+1) / ((n-1)*(n-2)*(n-3))
    bias = 3*(n-1)**2 / ((n-2)*(n-3))
    norm = (x-x.mean()) / x.std()
    
    return coef* np.sum(norm**4) - bias


def log_mean(x):
    a = x.mean()+x.std()**2/2
    return np.exp(a)

def log_var(x):
    a = 2*x.mean()+x.std()**2
    return np.exp(a) * (np.exp(x.std()**2)-1)

