import numpy as np
import sklearn.metrics as sm

# 正解率などをdict型で返す
# label:ラベルの真値
# predict_label:予測したラベル
def classifier_evaluation(label, predict_label):

    # 混同行列・正解率・適合率・再現率・F値を計算
    cm  = sm.confusion_matrix(label,predict_label)
    acc = sm.accuracy_score(label,predict_label)
    pre = sm.precision_score(label,predict_label)
    rec = sm.recall_score(label,predict_label)
    fvl = sm.f1_score(label,predict_label)

    # dictionary にして返す 
    v_dict = {'confusion':cm, 'accuracy':acc, 'precision':pre, 'recall':rec, 'F':fvl}
    return v_dict


# 予測に成功している部分のインデックスを返す
def correct_index(label,predict_label):
    idx = np.where(label==predict_label)
    return idx

# 予測に失敗している部分のインデックスを返す
def error_index(label,predict_label):
    idx = np.where(label!=predict_label)
    return idx



