
import numpy as np

# ***************************************
# 正規化 
#
#   data: データ
#   split: 正規化パラメータを抽出する領域
# ***************************************
class Normalization():
    # init: 基準となるデータを定義
    def __init__(self, data, scal=1):
        self.data = data
        self.scal = scal
        self.dmax = np.max(data) 
        self.dmin = np.min(data) 
        self.mean = np.mean(data) 
        self.std = np.std(data) 

    # 基準となるデータが0 ~ 1の範囲になるように正規化
    # 倍率もかけれる
    def zero_to_one(self, data, return_params=False):
        data_norm = (data - self.dmin) / ((self.dmax - self.dmin) * self.scal)
        if return_params:
            return data_norm, [self.dmin, self.dmax]
        else:
            return data_norm

    # 正規化したデータを元に戻す
    def re_zero_to_one(self, data_norm):
        data = data_norm * (self.dmax - self.dmin) * self.scal + self.dmin
        return data

