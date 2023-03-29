import numpy as np
import codecs
import array
import sys
# import matplotlib.pyplot as plt

def load_tdms(path, ch_num):

    ch = [[] for _ in range(ch_num)]
    with codecs.open(path, 'rb') as f:
        while True:
            # リードインと呼ばれる部分の読み込み
            tdms = f.read(28) 
            # print(f.tell())
            # print(tdms)
            #if b'TDSm' != tdms[:4]:
            #    continue

            # ファイルを最後まで読み込んだら終了
            if tdms==b'': 
                break

            # データとその区切りを取得
            # 次のセグメントの位置を抽出
            seg_ofs = tdms[12:20]
            by1 = array.array('l')
            by1.frombytes( seg_ofs )
            seg_ofs = np.asarray(by1)[0]
            # データの位置を抽出
            data_ofs= tdms[20:28] 
            by2 = array.array('l')
            by2.frombytes( data_ofs )
            data_ofs = np.asarray(by2)[0]

            # データのある部分まで読み飛ばす
            tdms = f.read(data_ofs)
            #print(tdms[:200], len(tdms))
            #if len(ch[0])==2:
            #    exit()
            #if len(ch[0])==0:
            #    head=tdms
            # データ部分の読み込み
            tdms = f.read(seg_ofs-data_ofs)
            print(tdms[-32:])
            by = array.array('f')
            by.frombytes( tdms )
            data = np.asarray( by )
            # print(data.shape)

            # 各チャンネルを取得
            for i in range(ch_num):
                ch[i].append( data[i::ch_num].reshape(-1,1) )

    for i in range(ch_num):
        ch[i] = np.vstack(ch[i])[:,0]

    return ch



if __name__ == '__main__':
    path = '/home/owner/Desktop/work/program_test/TDMSファイル変換/AE_125.tdms'
    path = '/media/owner/0105-8344/jtekt/20211209_082453/AI0/1-50/AI0-1.tdms'
    # ch_numにはチャンネル数を渡す. AE_Signal, AE_Noise, AE_AF で3チャンネル.
    # data[0]にAE_Signal, data[1]にAE_Noise, data[2]にAE_AFのデータが入る.
    data = load_tdms(path, ch_num=1)
    print( data[0][:10], data[0][-10:] )
    # 例：各データの前方・後方10データずつ表示
    #print( data[0][:10], data[0][-10:] )
    #print( data[1][:10], data[1][-10:] )
    #print( data[2][:10], data[2][-10:] )

