import numpy as np
from scipy.stats import chi2

class MT():

    # callされたときに相関行列を作る
    def __init__(self, unit_space, th_method = 'X2', X2_p = 0.01):

        # 単位空間の平均と標準偏差
        mean, std = self.statistics(unit_space)
        # 単位空間の標準化
        unit_space_norm = self.normalizing(unit_space, mean, std)

        # 相関行列の計算
        self.R = np.corrcoef(unit_space_norm.transpose())
        # 相関行列の逆行列
        self.Rinv = np.linalg.inv(self.R)
        # χ2乗分布によるしきい値計算
        if th_method == 'X2':
            # 特徴量数の抽出
            n = unit_space_norm.shape[1]
            # しきい値計算
            th = chi2.ppf(1 - X2_p, df = n) / n
        else:
            th = th_method

        # std[std==0] = 1
        self.unit_space = unit_space
        self.unit_space_norm = unit_space_norm
        self.mean = mean
        self.std  = std
        self.th   = th

    def __call__(self, data):
        data_norm = self.normalizing(data, self.mean, self.std)
        md = np.sum((data_norm @ self.Rinv) * data_norm, axis=1) / data_norm.shape[1]
        result = self.judgment(md, self.th)
        return md, result

    # 良否判定
    def judgment(self, md, th):
        # しきい値を超えた場合はFalse
        result = [False if md[i] >= th else True for i in range(len(md))]
        return result
        
    # 統計量を算出
    def statistics(self, data):
        mean = np.mean(data, axis = 0)
        std  = np.std(data,  axis = 0)
        return mean, std

    # 正規化
    def normalizing(self, data, mean, std):
        data_norm = (data - mean) / std
        return data_norm

        

