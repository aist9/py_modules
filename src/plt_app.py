import numpy as np
import matplotlib.pyplot as plt
import math

# 複数のグラフを同ウィンドウに並べて表示（当然だが大量にデータがあるとグラフが非常に小さくなる）
# 入力データは data.shape = (n,y) を想定
# n : データ数 　y : プロットされるデータ
def multiple_plot( data, ylim=None, xlim=None ):
    # listでも実行できるように雑に対処
    data = np.asarray(data)
    
    num = math.ceil( np.sqrt(data.shape[0]) )
    plt.rcParams["font.size"] = 10

    fig = plt.figure(figsize=(12,8))
    for i in range(data.shape[0]):
        fig.add_subplot(num,num,i+1)
        if ylim != None:
            plt.ylim(ylim[0],ylim[1])
        if xlim != None:
            plt.xlim(xlim[0],xlim[1])
        else:
            plt.xlim(0,data.shape[1])

        plt.plot(data[i])

    plt.show()

# 複数の連続データの変化が見たいとき用（multiple_plotの動画バージョン）
# 複数の画像を保存してviewerで開いてコマ送りする感じ
# 入力データは data.shape = (n,y) を想定
# n : データ数 　y : プロットされるデータ
def video_plot( data, isStop = False ):
    data = np.asarray(data)
    ymax = np.max(data)
    ymin = np.min(data)
    
    fig, ax = plt.subplots(1, 1)
    x = np.arange(data.shape[1])
    y = data[0]
    lines, = ax.plot(x, y)

    for i in range(data.shape[0]):
        y = data[i]
        lines.set_data(x, y)
        plt.pause(.10)
    
    if isStop:
        y = data[-1]
        lines.set_data(x,y)
        plt.show()

# ============================================
#
# 誤差や異常度の推移をplot
#
# ============================================
def err_plot(err, folder, name, th = None, yl = None, xlb = 'Sample', ylb = None):
    plt.figure()
    left = list(range(1, len(err) + 1))
    xmin = min(left) - 1
    xmax = max(left) + 1
    plt.bar(left, err, color = 'k', width = 1)
    plt.xlim([xmin, xmax])
    if xlb != None:
        plt.xlabel(xlb)
    if ylb != None:
        plt.ylabel(ylb)
    if yl != None:
        plt.ylim(yl)
    if th != None:
        plt.hlines([th], xmin, xmax, "blue", linestyles = 'dashed')
    plt.savefig(folder + '/' + name + '.png')
    plt.close()

# ============================================
#
# plotを行う
#
# ============================================
def data_plot(y, folder, name, x=None, xl=None, yl=None, xlb = None, ylb = None):
    plt.figure()
    if type(x) != None:
        plt.plot(x, y, color='k')
        plt.xlim([min(x), max(x)])
    else:
        plt.plot(y, color='k')
    if xlb != None:
        plt.xlabel(xlb)
    if ylb != None:
        plt.ylabel(ylb)
    if yl != None:
        plt.ylim(yl)
    if xl != None:
        plt.xlim(xl)
    plt.savefig(folder + '/' + name + '.png')
    plt.close()

