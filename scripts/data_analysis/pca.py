
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

class PCA():
    def __init__(self, data, th_cr=1, th_ccr=90):
        # しきい値のupdate
        self.update_parameters(th_cr=th_cr, th_ccr=th_ccr)
        
        # 主成分得点係数行列の作成
        pca_mat, mean, std = self.data_to_pca_mat(data)
        self.mean = mean
        self.std = std
        self.pca_mat = pca_mat
        
    # 主成分分析の結果を返す
    def __call__(self, data):
        # 正規化
        z = (data - self.mean) / self.std
        # 主成分分析
        data_pca = np.dot(z, self.pca_mat.transpose())

        return data_pca

    def update_parameters(self, th_cr=1, th_ccr=90):
        # 寄与率のしきい値
        self.th_cr = th_cr
        # 累積寄与率のしきい値
        self.th_ccr = th_ccr

    # 主成分得点係数行列を算出
    def data_to_pca_mat(self, data):

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
            if self.th_ccr < cr_sum or cr[i] < self.th_cr:
                pca_n = i + 1
                break

        # 主成分得点係数行列を算出
        pca_mat = []
        for i in range(pca_n):
            pca_mat.append(v[:, i] / np.sqrt(w[i]))
        pca_mat = np.array(pca_mat)
        
        self.pca_n = pca_n

        return pca_mat, mean, std

        
def main():
    # データの読み込み
    dataset = datasets.load_iris()
    data = dataset.data
    targets = dataset.target

    # 主成分分析
    pca = PCA(data, th_cr=1, th_ccr=90)
    data_pca = pca(data)

    plt.scatter(data_pca[:50,0], data_pca[:50,1]) 
    plt.scatter(data_pca[50:100,0], data_pca[50:100,1]) 
    plt.scatter(data_pca[100:,0], data_pca[100:,1]) 
    plt.show()

if __name__=='__main__':
    main()


