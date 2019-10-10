
import numpy as np
from scipy import signal

# *******************************
# 周波数の算出
#   input 
#     data: 入力データ
#   output
#     f: 周波数
# *******************************
def frequency(data, fs):
    # 周波数binを計算し、片側だけ抽出
    f = np.fft.fftfreq(len(data), 1 / fs)
    f = f[0:int(len(f)/2)]
    return f

class data2spect():
    def __init__(self, fs, fft_size = 1024):
        self.fs       = fs
        self.fft_size = fft_size    

    # *******************************
    # スペクトルの算出
    #   input 
    #     data: 入力データ
    #   output
    #     f: 周波数
    #     data_fft: スペクトル
    # *******************************
    def fft(self, data):
        # 周波数binを計算し、片側だけ抽出
        f = np.fft.fftfreq(len(data), 1 / self.fs)
        f = f[0:int(len(f)/2)]
        
        # FFTを行い、片側だけ抽出
        data_fft = np.abs(np.fft.fft(signal.detrend(data)))
        data_fft = data_fft[:, 0:int(len(data_fft)/2)]
        
        return f, data_fft

    # *******************************
    # STFT 
    #   input 
    #     data: 入力データ
    #     overlap_rate: オーバーラップ率[%] (defalt: 50)
    #     dtype: powerを指定するとdBに変換する (defalt: None)
    #   output
    #     f: 周波数bin
    #     t: 時間bin
    #     s: STFTの結果
    #     p: 平均power
    # *******************************
    def power(self, data, overlap_rate = 50, dtype = None):
        overlap = self.fft_size / (100 / overlap_rate)
        f, t, s = signal.stft(data, fs = self.fs, nperseg = self.fft_size, \
                              noverlap = overlap, detrend = 'linear', boundary = None)
        s = np.abs(s)
        p = np.mean(s, axis = -1)
        if dtype == 'power':
            p = 20 * np.log10(p)

        return f, t, s, p

