import numpy as np

def l2_cross_table(feat_num):
    if feat_num < 3:
        print('feat_num must be larger than 2')
        exit()

    l4_table = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
    if feat_num < 4:
        return l4_table

    count = 0
    n = feat_num
    while True:
        count+=1
        n = n>>1
        if n == 0:
            break

    # L4直交表の拡張を繰り返す回数, L8なら1回
    expand_num = count-2
    table = l4_table.astype(np.bool_)
    for i in range(expand_num):
        table = table.repeat(2, axis=0)
        new_table = np.zeros( (table.shape[0], table.shape[1]+1), dtype=np.bool_ )
        new_table[1::2,0] = True

        for j in range(table.shape[1]):
            # new_table[:,j+1] = np.logical_xor( table[:,j], new_table[:,0] )
            new_table[:,j+1] = table[:,j] ^ new_table[:,0]


        table = np.hstack( (table,new_table) )
    return table[:,:feat_num]


# l2_cross_table(7)
# data = l2_cross_table(8)
# for i in data:
#     for j in i:
#         print(int(j), end=' ')
#     print()
# l2_cross_table(32)

