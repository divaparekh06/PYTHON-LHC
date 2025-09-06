#This module for generating trigonometric signals 
# 1)	sine_wave(A, f, phi, t) – Generates a sine wave with amplitude A, frequency f, phase phi, and time vector t.
# 2)	cosine_wave(A, f, phi, t) – Generates a cosine wave with similar parameters.
# 3)	exponential_signal(A, a, t) – Generates an exponential signal.

import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phase, duration, fs=1000):
    """
    at t=0, it will start from one, it will be a continueous signal and x(t)=sin(2*(pi)*f*t + phase)
    """
    t = np.linspace(0, duration, int(fs*duration))   
    x = A * np.sin(2 * np.pi * f * t + phase)          
    plt.plot(t, x)
    plt.title(f"Sine Wave (A={A}, f={f}Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    return t, x

def cosine_wave(A, f, phase, duration, fs=1000):
    """
    x(t) = A * cos(2*pi*f*t + phi)
    """
    t = np.linspace(0, duration, int(fs*duration))
    x = A * np.cos(2 * np.pi * f * t + phase)          # cosine formula
    plt.plot(t, x)
    plt.title(f"Cosine Wave (A={A}, f={f}Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    return t, x

def exponential_signal(A, a, duration, fs=1000):
    """
    x(t) = A * exp(a * t)
    If a > 0 → exponential grows at the particular value.
    If a < 0 → exponential decays 
    """
    t = np.linspace(0, duration, int(fs*duration))
    x = A * np.exp(a * t)                            
    plt.plot(t, x)
    plt.title(f"Exponential Signal (A={A}, a={a})")
    plt.xlabel("Time (s)")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    return t, x