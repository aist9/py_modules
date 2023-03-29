# ver 0.14.0
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
    groupName   = tdms_file.groups()
    
    # チャンネル名をすべて取得
    channelName = []
    for g in groupName:
        channelName.append(tdms_file.group_channels(g))
    
    return groupName, channelName

def tdms2arr(tdmsName, timeReq = False):

    tdms_file = TdmsFile(tdmsName)

    groupName   = tdms_file.groups()
    channelName = tdms_file.group_channels(groupName[0])
    
    channel = tdms_file.object(groupName[0], channelName[0].channel)
    data = channel.data

    if timeReq == True:
        time = channel.time_track()
        return data, time
    else:
        return data

# 同一フォルダ内の複数のTDMSファイルを合わせて送り返す
def tdms2arrMultiFiles(folder, timeReq = False, index = None):

    # フォルダ内のtdmsを検索する
    file_name = glob.glob(folder + '/*.tdms')

    flag = False

    dataArr = []
    if timeReq == True:
        timeArr = []

    # ファイル名のソート
    basename = [os.path.basename(file_name[i]) for i in range(len(file_name))]
    file_name = sorted(basename, key=numericalSort)
    
    f = open('test.txt', 'w')
    f.write('\n'.join(file_name))
    f.close()

    if index == None:
        index = range(len(file_name))

    for i in index:
        
        tdms_name = folder + '/' + file_name[i]
        print('\rFile name: ' + tdms_name, end="")

        try:
            # # 小さいファイルサイズ(収録されていない)を検知
            # if os.path.getsize(tdms_name[i]) < 10 :
            #     flag = True
            #     break

            if timeReq == True:
                data, time = tdms2arr(tdms_name) 
                timeArr.append(time)
            else: 
                data = tdms2arr(tdms_name)

            dataArr.append(data)
        
        except:
            flag = True
            break
    print()
    dataArr = np.array(dataArr, dtype = 'float32')

    if timeReq == True:
        timeArr = np.array(timeArr, dtype = 'float32')
        return dataArr, timeArr, flag
    if timeReq == False:
        return dataArr, flag




