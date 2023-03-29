import numpy as np
import matplotlib.pyplot as plt
from nptdms import TdmsFile


def read_tdms(path):
    tdms_file = TdmsFile.read(path)
    group_name = tdms_file.groups()[0].name
    group = tdms_file[group_name]

    Data = []
    for channels in group.channels():
        channel = group[channels.name]
        channel_data = channel[:]
        Data.append(channel_data)

    #print(channel_data.shape)
    #print('max value', channel_data.max())
    #print('min value', channel_data.min())
    return Data


if __name__ == '__main__':
    path = '/media/owner/000D-7BA9/mori/20220810_141026/Signal0_/1-5000/Signal0_13.tdms'
    #path2 = '/media/owner/052D-D4E7/jtekt/20220202_131527/AI0/1-50/AI0-1.tdms'
    data  = read_tdms(path)
    #data2 = read_tdms(path2)

    plt.figure(figsize=(16,8))
    plt.plot(data[0][::10], alpha=0.5)
    plt.plot(data[1][::10], alpha=0.5)
    plt.plot(data[2][::10], alpha=0.5)
    plt.plot(data[3][::10], alpha=0.5)
    plt.show()
