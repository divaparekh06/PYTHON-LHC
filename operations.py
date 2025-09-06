# Implement the following signal operations:
# time_shift(signal, k) – Shifts the signal by k units.
# time_scale(signal, k) – Scales the time axis of the signal by factor k.
# signal_addition(signal1, signal2) – Performs addition of two signals.
# signal_multiplication(signal1, signal2) – Performs point-wise multiplication of two signals.

import numpy as np
import matplotlib.pyplot as plt

def time_shift(t, x, k):
    
    t_new = t + k               # shift the time axis
    x_new = x                   # values stay the same
    plt.plot(t_new, x_new, marker='o')
    plt.title(f"Time Shift by {k}")
    plt.xlabel("Time")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    return t_new, x_new

def time_scale(t, x, k):
    
    t_new = t * k               # stretch/compress time
    x_new = x                   # values stay the same
    plt.plot(t_new, x_new, marker='o')
    plt.title(f"Time Scaling by {k}")
    plt.xlabel("Time")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    return t_new, x_new

def signal_addition(t, x1, x2):
    
    s = x1 + x2                 # adds values point by point
    plt.plot(t, s, marker='o')
    plt.title("Signal Addition")
    plt.xlabel("Time")
    plt.ylabel("x1(t) + x2(t)")
    plt.grid(True)
    plt.show()
    return t, s

def signal_multiplication(t, x1, x2):
    """
    Multiply two signals of the same length.
    (t, x1), (t, x2) → signals
    """
    s = x1 * x2                 # multiply values point by point
    plt.plot(t, s, marker='o')
    plt.title("Signal Multiplication")
    plt.xlabel("Time")
    plt.ylabel("x1(t) * x2(t)")
    plt.grid(True)
    plt.show()
    return t, s