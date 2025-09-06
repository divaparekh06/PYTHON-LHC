# Implement the following functions:
# unit_step(n) – Generates a unit step signal.
# unit_impulse(n) – Generates a unit impulse signal.
# ramp_signal(n) – Generates a ramp signal.
# Each function should return a NumPy array and plot the signal using matplotlib.

import numpy as np
import matplotlib.pyplot as plt


def unit_step(n):

    '''Unit step function = u[n]=0 for n<0 and u[n]=1 for n>=0
    the function will run from -n to +n'''
    t = np.arange(-n, n+1)   
    x = (t >= 0).astype(int) 
    plt.stem(t, x)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("u[n]")
    plt.grid(True)
    plt.show()
    return t, x

def unit_impulse(n):
    ''' the function will run from -n to +n and 
    fot unit impulse function, f[n]=1 for n=0 otherwise 0.'''
    t = np.arange(-n, n+1) #etle aapde agar n=5 laiye toh ee -5 thi 5 sudhi na time points lese
    x = (t == 0).astype(int) 
    plt.stem(t, x)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("f[n]")
    plt.grid(True)
    plt.show()
    return t, x

def ramp_signal(n):
    ''' Here we will go from 0 to n+1 and here 
    t i.e time points and x i.e the f[n] will be equal at each 
    point making a step like graph structure.
    '''
    t = np.arange(0, n+1) 
    x = t                 
    plt.stem(t, x)
    plt.title("Ramp Signal r[n]")
    plt.xlabel("n")
    plt.ylabel("r[n]")
    plt.grid(True)
    plt.show()
    return t, x
    
    

