import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from scipy.signal import chirp

# ヒルベルト変換を行う
def envelope(data, axis=-1):
    # axisを設定すると一括変換
    data_env = hilbert(data, axis=axis)
    data_env = np.abs(data_env)

    return data_env

def main():

    fs = 400
    samples = int(fs)
    t = np.arange(samples) / fs

    data = chirp(t, 20.0, t[-1], 100.0) * (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )
    data_env = envelope(data)

    plt.plot(data)
    plt.plot(data_env)
    plt.show()

if __name__=='__main__':
    main()

