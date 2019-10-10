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

