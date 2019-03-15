import networkx as nx
import scipy.integrate as spi
import numpy as np
import pylab as pl
import random as rd

BETA = 0.8
GAMMA = 0.2
N = 100
t_range = np.arange(0, 120, 1.0)

#init
I = np.zeros(3*N)
for x in range(3*N):
    if x%3==0:
        I[x]=0
    elif x%3==1:
        I[x]=1
    elif x%3==2:
        I[x]=0
#random choose 2 items
i1 = 3*rd.randint(0, N)
i2 = i1
while i2 == i1:
    i2 = 3*rd.randint(0, N)
I[i1] = 1
I[i1+1]=0
I[i2] = 1
I[i2+1]=0

scale_free_network = nx.random_graphs.barabasi_albert_graph(N, 1)
A = nx.to_numpy_matrix(scale_free_network)


def diff_eqs(X, t):
    Y = np.zeros(3*N)
    for i in range(N):
        neighbor_sum = 0
        i_x=X[3*i]
        s_x=X[3*i+1]
        r_x=X[3*i+2]
        for j in range(N):
            neighbor_sum += A[i, j] * X[j]
        Y[3*i] = s_x* BETA * neighbor_sum - GAMMA * i_x
        Y[3*i+1]=-s_x*BETA * neighbor_sum
        Y[3*i+2]=GAMMA*i_x
    return Y

def run_ode():
    result = spi.odeint(func=diff_eqs, y0=I, t=t_range)
    return result


def main():
    result = run_ode()
    result_x_axis=[]
    result_mean_I=[]
    result_mean_S=[]
    result_mean_R=[]
    for i in range(len(result)):
        ImeanOfRow=0
        SmeanOfRow=0
        RmeanOfRow=0
        for j in range(N):
            ImeanOfRow=ImeanOfRow+result[i,3*j]
            SmeanOfRow=SmeanOfRow+result[i,3*j+1]
            RmeanOfRow=RmeanOfRow+result[i,3*j+2]
        result_x_axis.append(i)
        result_mean_I.append(ImeanOfRow/N)
        result_mean_S.append(SmeanOfRow/N)
        result_mean_R.append(RmeanOfRow/N)
    pl.plot(result_x_axis,result_mean_I,marker='*',linestyle='--',markerfacecolor='r',label='I')
    pl.plot(result_x_axis,result_mean_S,marker='^',linestyle='--',markerfacecolor='b',label='S')
    pl.plot(result_x_axis,result_mean_R,marker='o',linestyle='--',markerfacecolor='g',label='R')
    pl.legend(loc=0)
    pl.title('SIR with network')
    pl.xlabel('time/round')
    pl.ylabel('rate')
    pl.show()


if __name__ == '__main__':
    main()

