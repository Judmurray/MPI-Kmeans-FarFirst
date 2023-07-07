import sys
import numpy as np
import matplotlib.pyplot as plt

# the name of the output file is a command line argument
if (len(sys.argv) < 2):
    print ("Command Usage : python3",sys.argv[0],"outfile")
    exit(1)
outfile = sys.argv[1]

# read the data file
data = np.loadtxt(sys.stdin)

# plot the data
plt.gca().set_aspect('equal')
plt.scatter(data[:,0],data[:,1],s=1,color='black')

# plot the centers (if additional command line argments present)
num_centers = len(sys.argv)-2
if (num_centers > 0):
    centers = np.zeros(num_centers,dtype='int')
    for k in range(2,len(sys.argv)):
        centers[k-2] = int(sys.argv[k])
    center_nums = range(len(centers))
    point_centers = np.zeros(len(data))
    point_distances = np.zeros(len(data))
    distance_sq = np.zeros(len(centers))
    for i in range(len(data)):
        for j in range(len(centers)):
            distance_sq[j] = np.inner(data[i]-data[centers[j]],
                                      data[i]-data[centers[j]])
        point_centers[i] = np.argmin(distance_sq)
        point_distances[i] = np.min(distance_sq)
    max_distance_to_center = np.max(point_distances)
    extreme_city = np.argmax(point_distances)
    plt.scatter (data[:,0],data[:,1],
                 c=point_centers,cmap="tab10",s=10)
    plt.scatter (data[centers,0],data[centers,1],
                 c=center_nums,cmap="tab10",s=100)
    plt.scatter (data[extreme_city,0],data[extreme_city,1],
                 s=50,facecolors='none', edgecolors='black')

# save the plot as an image
plt.savefig(outfile)

