import scipy.integrate as spi
import numpy as np
import pylab as pl

beta=0.8
gamma=0.2
TS=1.0
ND=100.0

#initial condition
S0=1-10e-3
I0=10e-3
InitialSIR = (S0, I0, 0.0)

#function
def diff_eqs(INPUT,t,k):
    S = INPUT[0]
    I = INPUT[1]
    R = INPUT[2]
    dsdt = - k*beta * S * I
    didt = beta * S * I - gamma * I
    drdt = gamma * I
    return [dsdt,didt,drdt]

#time points
t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)

#solve ode
k=1
result = spi.odeint(diff_eqs,InitialSIR,t_range,args=(k,))
print(result)

#Ploting
pl.plot(result[:,0], '-bs', label='S')  # I change -g to g--  # result[:,0], '-g',
pl.plot(result[:,2], '-g^', label='R')  # result[:,2], '-k',
pl.plot(result[:,1], '-ro', label='I')
pl.legend(loc=0)
pl.title('SIR epidemic')
pl.xlabel('Time')
pl.ylabel('S, R, I')
pl.savefig('Basic SIR.png', dpi=900) # This does, too
pl.show()
