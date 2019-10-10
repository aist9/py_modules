
import numpy as np
from scipy import signal

# 周波数ビンの計算
def frequency(fft_size, fs):
    # 周波数binを計算し、片側だけ抽出
    frequency = np.fft.fftfreq(fft_size, 1 / fs)
    frequency = frequency[0:int(len(frequency) / 2)]
    return frequency

# スペクトルの算出
def fft(data, fft_size, fs, use_gpu=False, use_detrend=True):

    data = np.asarray(data)

    # shapeを2次元にする
    if len(data.shape) == 1:
        data = data.reshape(1, data.shape[0])

    # FFTを行い、片側だけ抽出
    # use_gpu=Trueの場合cupyにより高速演算
    if use_detrend:
        sig = signal.detrend(data)
    else:
        sig = data
    if use_gpu:
        import cupy as cp
        gpu_data = cp.asarray(sig)
        ft = cp.fft.fft(gpu_data)
        spectrum = np.abs(cp.asnumpy(ft))
    else:
        spectrum = np.abs(np.fft.fft(sig))

    spectrum = spectrum[:, 0:int(spectrum.shape[1]/2)]
    
    return frequency(fft_size, fs), spectrum

# STFTし平均パワースペクトルを算出
def power(data, fft_size, fs, overlap_rate = 50, dtype = None):

    # shapeを2次元にする
    if len(data.shape) == 1:
        data = data.reshape(1, data.shape[0])

    overlap = fft_size / (100 / overlap_rate)
    frequency_bin, time_bin, spectrogram = signal.stft(
                                    data, fs=fs, nperseg=fft_size, \
                                    noverlap=overlap,
                                    detrend='linear', boundary=None)
    spectrogram = np.abs(spectrogram)
    power = np.mean(spectrogram, axis=-1)
    # パワースペクトルへの変換
    if dtype == 'power':
        power = 20 * np.log10(power)
    
    return frequency_bin, time_bin, spectrogram, power

# test
if __name__=='__main__':

    # サンプリング時間
    sampling_time = 1
    # データ長
    num_samples = 1000

    # データを作成
    num_waves = 10
    sin_wave_1 = np.sin(np.linspace(0, num_waves*2*np.pi, num_samples))
    num_waves = 100
    sin_wave_2= 0.5 * np.sin(np.linspace(0, num_waves*2*np.pi, num_samples))
    num_waves = 300
    sin_wave_3 = 0.3 * np.sin(np.linspace(0, num_waves*2*np.pi, num_samples))
    data = sin_wave_1 + sin_wave_2 + sin_wave_3

    # fft
    fs = int(num_samples / sampling_time)
    fft_size = len(data)
    f_by_fft, s = fft(data, fft_size, fs)
    
    fft_size = 256
    f_by_power, t, spectrogram, p = power(data, fft_size, fs)

    import matplotlib.pyplot as plt
    plt.subplot(3, 1, 1)
    plt.plot(data)
    plt.subplot(3, 1, 2)
    plt.plot(f_by_fft, s[0])
    plt.subplot(3, 1, 3)
    plt.plot(f_by_power, p[0])
    plt.show()


