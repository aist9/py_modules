
import numpy as np
import csv
import codecs 
import time
from chardet.universaldetector import UniversalDetector

# *********************************
#
# csvを使う編
#
# *********************************
#
# エンコーディングの判別
def check_encoding(path):
    detector = UniversalDetector()
    with open(path, mode='rb') as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    # print(detector.result['encoding'], end='')
    return detector.result['encoding']

# 文字列として読み込む
def csv_reader(path, enc='utf-8', enc_check_enable=False):
    if enc_check_enable == True:
        enc = check_encoding(path)
    
    with open(path, encoding=enc) as f:
        reader = csv.reader(f, delimiter = ',')
        data = [row for row in reader]
    return data

# codecs使用、文字列として読み込む
def csv_reader_codecs(path):
    enc = check_encoding(path)
    with codecs.open(path, 'r', encoding=enc) as f:
        reader = f.read()
        data = [row for row in reader]
    return data


# リストを書き込み
def csv_writer(path, data):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# そのままでは使いにくいので指定列のみ抜き出す
#   col: 指定列(0スタート)
#   skip: ヘッダーなどある場合に飛ばす行数を指定
def list2data(data_list, col, skip = 0):
    return [data_list[i + skip][col] for i in range(len(data_list) - skip)]

# *********************************
#
# numpyを使う編
#
# *********************************
#
# 文字列として読み込む
def csv_reader_np(path):
    data = np.loadtxt(path, delimiter = ",", dtype = "unicode")
    return data

# 文字列として書き込む
def csv_writer_np(path, data):
    np.savetxt(path, data, delimiter = ",", fmt = "%s")

