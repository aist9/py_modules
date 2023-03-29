
import numpy as np
import datetime

# タイムスタンプが格納された配列をdatetimeに変換
def str2time(data, fmt = '%Y/%m/%d/%H:%M:%S'):
    t = []
    for i in range(len(data)):
        t.append(datetime.datetime.strptime(data[i], fmt))
    return t

# 時刻の差分から
def time_delta_code(t):
    code = []
    for i in range(len(t)):
        code.append(t[i].days)
    return code

