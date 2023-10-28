import os
from create_bitmap import generate_bitmap, BITMAP_SIZE
import numpy as np
import json

for x in os.listdir("./dataset"):
    r = np.zeros((BITMAP_SIZE,BITMAP_SIZE), dtype=np.float_)
    a = generate_bitmap("./dataset/" + x)
    c = 0
    for d in a:
        r += d
        c += 1
    r /= c
    r.tofile(open("out_" + x.split(".")[0] + ".np", "w"))
