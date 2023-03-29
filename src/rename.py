import numpy as np
import os


def rename_dir(copy_base, rename_dir):

    rn = sorted(os.listdir(rename_dir))
    cp = sorted(os.listdir(copy_base))
    for c in cp:
        for r in rn:
            os.rename(bs+r, bs+c)
            print(c, r)


