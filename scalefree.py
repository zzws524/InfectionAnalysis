import networkx as nx
import scipy.integrate as spi
import numpy as np
import pylab as pl
import random as rd
import logging
from ziwenLog import myLogConfig

BETA = 0.8
GAMMA = 0.2
N = 100
t_range = np.arange(0, 100, 1.0)

I = np.zeros(N)
i1 = rd.randint(0, N)
i2 = i1
while i2 == i1:
    i2 = rd.randint(0, N)
I[i1] = 1
I[i2] = 1

scale_free_network = nx.random_graphs.barabasi_albert_graph(N, 1)
A = nx.to_numpy_matrix(scale_free_network)
myLog=myLogConfig.ConfigMyLog(logFileName='DataProcess',withFolder=False,consoleLevel=logging.INFO,logLevel=logging.DEBUG)
logger=logging.getLogger(__name__)
logger.info('A is:')
logger.info(A)

def diff_eqs(X, t):
    Y = np.zeros(N)
    for i in range(N):
        neighbor_sum = 0
        for j in range(N):
            neighbor_sum += A[i, j] * X[j]
        Y[i] = (1-X[i]) * BETA * neighbor_sum - GAMMA * X[i]
    return Y

#I[i] = V[i] * X[i] * BETA * neighbor_sum - GAMMA * X[i]
#S[i] =-V[i] * X[i] * BETA* neighbor_sum
#R[i] = gamma * V[i]
#£®S+I+R=1£©


def run_ode():
    result = spi.odeint(func=diff_eqs, y0=I, t=t_range)
    return result


def plot(result):
    pl.plot(result, '-rs', label='I')
    pl.legend(loc=0)
    pl.xlabel('Time')
    pl.ylabel('Ratio')
    pl.show()


def main():
    result = run_ode()
    result_mean = np.mean(result, axis=1)
    plot(result_mean)


if __name__ == '__main__':
    main()

