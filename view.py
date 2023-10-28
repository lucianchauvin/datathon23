import numpy as np
import matplotlib.pyplot as plt

print(np.fromfile("out_cactus.np").reshape(256,256))
plt.imshow(np.fromfile("out_cactus.np").reshape(256,256), interpolation='nearest', cmap='gray', vmin=0, vmax=1)
plt.savefig('cactus.png')

