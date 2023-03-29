import numpy as np

# AEパラメータの取得
def get_ae_parameters(data, dt):

    ae_parameters = []

    for d in data:
        v_max = np.max(d)
        v_min = np.min(d)
        v_rms = np.sqrt(np.sum(d ** 2) / len(d))
        v_mean = np.mean(np.abs(d))
        duration = len(d) * dt
        
        ae_parameters.append([v_max, v_min, v_rms, v_mean, duration])

    return ae_parameters


import numpy as np

# AEパラメータの取得
# 1データのみ入力
def get_ae_parameters(data, dt=None):

    ae_parameters = []
    
    # サンプル数
    n = len(data)
    # 最大
    v_max = np.max(data)
    # v_min = np.min(data)
    # 実行値
    v_rms = np.sqrt(np.sum(data**2) / n)
    # 平均値
    v_mean = np.mean(np.abs(data))
    # 分散値
    v_std = (np.std(data))
    v_var = v_std ** 2

    #波形値
    v_wave = v_rms / v_mean
    #波高率
    v_crest = v_max / v_rms

    # 歪度
    v_skew = (n/((n-1)*(n-2)) * np.sum( ((data - v_mean)/v_std)**3))
    # 尖度
    v_kurt = (n*(n-1)/((n-1)*(n-2)*(n-3)) * np.sum( (data-v_mean)**4 / v_std**4) - 3*(n-1)**2 / ((n-2)*(n-3)) )

    # AEパラメータをまとめる
    ae_parameters = [v_max, v_rms, v_mean, v_var, v_wave, v_crest, v_skew, v_kurt]


    # dtが設定されている場合持続時間を取得する
    if dt is not None:
        duration = n * dt
        ae_parameters += [duration]
        # 波形重心値
        # v_weight = (np.sum(data**2 * t) / np.sum(data**2))
        
    return ae_parameters

