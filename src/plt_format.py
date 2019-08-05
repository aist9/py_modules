
import matplotlib.pyplot as plt

def plt_format(font_size = 14, font = 'sans-serif', line_width = 1.0):
    
    ########## font ##########
    # Times New Roman
    plt.rcParams['font.family'] = font
    plt.rcParams['font.size'] = font_size
    
    ########## xtick, ytick ##########
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.major.width'] = 1.0
    plt.rcParams['ytick.major.width'] = 1.0

    ########## overview ##########
    # 軸と数値との距離
    # plt.tick_params(pad = 10) 
    plt.rcParams['axes.linewidth'] = line_width
    plt.rcParams['figure.figsize'] = 10,5
    plt.rcParams['savefig.bbox'] = 'tight'
