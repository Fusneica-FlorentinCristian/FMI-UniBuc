import numpy as np
import glob
import matplotlib.pyplot as plt

filenames = glob.glob("./images/*")
# practical-ml-fmi.github.io/ML

im = np.load(filenames[0])
plt.imshow(im, cmap="gray")
plt.show()
