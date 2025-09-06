# 	Demonstrate the following tasks:
# 1.	Generate and plot a unit step signal and a unit impulse signal of length 20.
# 2.	Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec.
# 3.	Perform time shifting on the sine wave by +5 units and plot both original and shifted signals.
# 4.	Perform addition of the unit step and ramp signal and plot the result.
# 5.	Multiply a sine and cosine wave of same frequency and plot the result.
import numpy as np
import matplotlib.pyplot as plt

from _ICT_DivaParekh_161 import unit_step, sine_wave

n, u = unit_step(10)
print("Unit step:", u)

t, x = sine_wave(A=1, f=2, phase=0, duration=1)
print("Sine wave:", x[:5])  
