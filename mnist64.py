import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) < 2):
    print ("Not enough command line arguments")
    quit()

outfile = sys.argv[1]

# read the data file
data = np.loadtxt(sys.stdin)
data = data.astype(int)

plt.rcParams['figure.figsize'] = (20, 20)
plt.rcParams['axes.facecolor']='white'
plt.rcParams['savefig.facecolor']='white'
images = np.zeros((64,28,28),dtype=int);
for i in range(64):
    images[i] = np.asarray(data[i]).reshape(28,28)

f, axarr = plt.subplots(8,8)
for i in range(8):
    for j in range(8):
        axarr[i][j].axis('off')
        axarr[i][j].imshow(images[i*8+j],cmap='gray',vmin=0, vmax=255, interpolation='none')
plt.savefig(outfile,bbox_inches='tight')
