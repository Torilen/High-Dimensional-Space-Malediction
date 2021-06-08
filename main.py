import numpy as np
import argparse
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist

parser = argparse.ArgumentParser()
parser.add_argument('--nbDimToTest', type=int, default=1000)
args = parser.parse_args()

percentContour = 0.1
nbData = 10000
k = 1

if __name__ == '__main__':
    expe = []
    for dim in range(1, args.nbDimToTest):
        outofspace = 0
        avgdistance = 0
        data = np.random.rand(10000, dim)
        for i in data:
            for subdim in i:
                if subdim >= 1-percentContour or subdim <= percentContour:
                    outofspace += 1
                    break

        for j in range(100):
            avgsample = data[np.random.randint(nbData, size=int(nbData*0.01)), :]
            avgdistance += np.mean(pdist(avgsample, 'cosine'))
        avgdistance = avgdistance/100
        expe.append(avgdistance)
        print("[{}] OUT OF SPACE = {} ~ {}% of the set | Avg euclidian distance : {}".format(dim, outofspace, outofspace/nbData*100, avgdistance))
        if dim % 100 == 0:
            plt.plot(expe)
            plt.show()