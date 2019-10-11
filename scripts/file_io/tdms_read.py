
import os
import glob
import re
import numpy as np
from nptdms import TdmsFile
from nptdms import TdmsObject
from nptdms import TdmsWriter, ChannelObject
from scipy import signal
from time import sleep

# ソート用の関数
def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# tdmsファイルのフルパスを取得し自然順ソートする
def tdms_path_get(folder):

    # フォルダ内のtdmsを検索する
    file_name = glob.glob(folder + '/**/*.tdms', recursive=True)
    file_path = sorted(file_name, key=numericalSort)

    return file_path

# tdmsのグループ名とチャンネル名を取得
def tdms_info(tdmsName):
    tdms_file = TdmsFile(tdmsName)

    # グループ名をすべて取得
    groupName = tdms_file.groups()
    
    # チャンネル名をすべて取得
    channelName = []
    for g in groupName:
        channelName.append(tdms_file.group_channels(g))
    
    return groupName, channelName

def tdms_to_nparr(tdms_name, time_req=False):

    tdms_file = TdmsFile(tdms_name)

    group_name   = tdms_file.groups()
    channel_name = tdms_file.group_channels(group_name[0])
    
    channel = tdms_file.object(group_name[0], channel_name[0].channel)
    data = channel.data.astype(np.float32)

    if time_req == True:
        time = channel.time_track()
        return data, time
    else:
        return data

# 同一フィオルダ内の複数のTDMSファイルを合わせて送り返す
def tdms_to_nparr_from_dir(folder, time_req=False, 
        start_index=None, max_index=None,
        size_check=False, min_size=0, max_size=100000,
        zero_padding=False, data_cut=False, data_length=None):

    # フォルダ内のtdmsを検索する
    file_name = glob.glob(folder + '/*.tdms')

    flag = False

    data = []
    time = []

    # ファイル名のソート
    basename = [os.path.basename(file_name[i]) for i in range(len(file_name))]
    file_name = sorted(basename, key=numericalSort)
    print(file_name)
    
    if start_index is None:
        start_index = 0

    if max_index is None:
        max_index = len(file_name)

    delete_index = []
    for i in range(start_index, max_index):
        
        tdms_name = os.path.join(folder, file_name[i])
        print('\rFile name: ' + tdms_name)

        # ファイルサイズが範囲外なら読み込まない
        if size_check and \
                (os.path.getsize(tdms_name) < min_size * 1e6 or \
                 os.path.getsize(tdms_name) > max_size * 1e6):
            print('size out')
            delete_index.append(i)
            continue

        if time_req == True:
            d, t = tdms_to_nparr(tdms_name) 
            time.append(t)
        else: 
            d = tdms_to_nparr(tdms_name)

        # データ長を指定した長さに切る
        if data_length is not None and data_cut:
            d = d[0:data_length]

        data.append(d)
            
    # データの長さを指定
    if data_length is None:
        data_length = max(map(len, data))
    # 長さがそれぞれ異なる場合は0埋めする
    if zero_padding:
        l = max(map(len, data))
        data = [np.concatenate([d, np.zeros(data_length-len(d),)]) for d in data]

    # numpyに変換
    data = np.array(data, dtype='float32')

    if time_req:
        timeArr = np.array(time, dtype='float32')
        return data, time
    else:
        return data, delete_index

