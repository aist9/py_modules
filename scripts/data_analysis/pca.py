
import numpy as np

class PCA():
    def __init__(self, th_cr = 1, th_ccr = 90):
        # 寄与率のしきい値
        self.th_cr  = th_cr
        # 累積寄与率のしきい値
        self.th_ccr = th_ccr

    # 単位空間から主成分得点係数行列を作成
    def __call__(self, data):
        pca_mat, mean, std = self.data2pca_mat(data)

        self.pca_mat = pca_mat
        self.mean    = mean
        self.std     = std

    # 主成分得点係数行列を算出
    def data2pca_mat(self, data):

        # 平均と標準偏差
        mean = np.mean(data, axis = 0)
        std  = np.std(data, axis = 0)
        z = (data - mean) / std

        # 分散共分散行列
        cv = np.cov(z, rowvar = 0, bias = 1)
        for i in range(len(cv)):
            cv[i, i] = cv[i, i] ** 2

        # w: 固有値, v: 固有ベクトル
        w, v = np.linalg.eig(cv)

        # 固有ベクトルの規格化
        for i in range(len(v)):
            v[i] = v[i] / np.linalg.norm(v[i])
        
        # 寄与率から主成分の数を決める
        cr = w / sum(w) * 100
        cr_sum = 0
        for i in range(len(cr)):
            cr_sum += cr[i]
            if 90 < cr_sum or cr[i] < 1:
                pca_n = i + 1
                break

        # 主成分得点係数行列を算出
        pca_mat = []
        for i in range(pca_n):
            pca_mat.append(v[:, i] / np.sqrt(w[i]))
        pca_mat = np.array(pca_mat)

        return pca_mat, mean, std

    # 主成分得点係数行列を使って主成分分析を行う
    def data2pca(self, data):
        
        # 正規化
        z = (data - self.mean) / self.std
        
        # 主成分分析
        data_pca = np.dot(z, self.pca_mat.transpose())

        return data_pca
