# _ICT_DivaParekh_161

A custom Python package designed and implemented for the **Programming with Python (Subject Code: 01CT1309)** course, demonstrating fundamental concepts of Signals and Systems.

---

## **Package Overview**

This package, `_ICT_DivaParekh_161`, is structured modularly and includes three core modules for signal generation and operations, plus a main script for demonstration:

*   **`unitary_signals.py`**: This module implements functions to generate basic discrete-time signals [14]. Each function returns both the time vector (`t`) and the signal array (`x`) as NumPy arrays, and automatically plots the signal using Matplotlib.
    *   `unit_step(n)`: Generates a unit step signal `u[n]`, which is `0` for `n < 0` and `1` for `n >= 0`. The signal is generated for time indices `n` ranging from `-n` to `+n`.
    *   `unit_impulse(n)`: Generates a unit impulse signal `f[n]`, which is `1` at `n = 0` and `0` otherwise. The signal is generated for time indices `n` ranging from `-n` to `+n`.
    *   `ramp_signal(n)`: Generates a ramp signal `r[n]`, where the amplitude `r[n]` is equal to `n`. The signal is generated for time indices `n` ranging from `0` to `n`.

*   **`trigonometric_signals.py`**: This module contains functions for generating continuous-time signals. Each function returns both the time vector (`t`) and the signal array (`x`) as NumPy arrays, and automatically plots the signal using Matplotlib.
    *   `sine_wave(A, f, phase, duration, fs=1000)`: Generates a sine wave `x(t) = A * sin(2 * pi * f * t + phase)`. Parameters include amplitude `A`, frequency `f` (Hz), phase `phase` (radians), total `duration` (seconds), and sampling frequency `fs` (samples per second, default 1000).
    *   `cosine_wave(A, f, phase, duration, fs=1000)`: Generates a cosine wave `x(t) = A * cos(2 * pi * f * t + phase)` with similar parameters.
    *   `exponential_signal(A, a, duration, fs=1000)`: Generates an exponential signal `x(t) = A * exp(a * t)`. `a` determines growth (if `a > 0`) or decay (if `a < 0`).

*   **`operations.py`**: This module provides functions to perform fundamental signal operations. All operation functions expect to receive both a time vector (`t`) and a signal array (`x`) or two signal arrays (`x1`, `x2`) alongside a common time vector. Each function plots the result and returns the new time and/or signal arrays.
    *   `time_shift(t, x, k)`: Shifts the time axis of the signal `x` by `k` units. A positive `k` shifts the signal to the right (delay).
    *   `time_scale(t, x, k)`: Scales the time axis of the signal `x` by a factor `k`. `t_new = t * k`.
    *   `signal_addition(t, x1, x2)`: Performs element-wise addition of two signals, `x1` and `x2`, at corresponding time points `t`.
    *   `signal_multiplication(t, x1, x2)`: Performs point-wise multiplication of two signals, `x1` and `x2`, at corresponding time points `t.

*   **`main.py`**: This script demonstrates the functionality of the package by importing modules and calling their functions.

---

## **Installation**

To use this package, you'll need Python 3.6 or higher and `pip` (Python package installer).

### **1. Prerequisites**
Ensure you have `numpy`, `matplotlib`, `build`, and `twine` installed:
```bash
pip install numpy matplotlib build twine
2. Building the Package
Navigate to the root directory of this project (where setup.py is located) in your terminal and run:
python -m build
This command will create a dist/ folder containing the distributable .whl (wheel) and .tar.gz (source distribution) files.
3. Installing from a Local Wheel File
Once you have built the package, you can install it directly from the generated wheel file:
pip install dist/signal_ICT_YourName_YourEnrollmentNo-0.1.0-py3-none-any.whl
(Note: The exact version number and package name in the .whl file might vary slightly based on your setup.cfg and Python version.)
4. Installing from TestPyPI
After successfully uploading your package to TestPyPI (as instructed below), you can install it using:
pip install --index-url https://test.pypi.org/simple/ --no-deps signal_ICT_YourName_YourEnrollmentNo

--------------------------------------------------------------------------------
Usage Example
The main.py script serves as an example of how to import and use the functions from this package. Note that your main.py directly imports specific functions from the package root due to the __init__.py configuration.
import numpy as np
import matplotlib.pyplot as plt

# Import functions directly from the package
# Make sure to replace '_ICT_DivaParekh_161' with your actual package name 'signal_ICT_YourName_YourEnrollmentNo'
from _ICT_DivaParekh_161 import unit_step, unit_impulse, ramp_signal, sine_wave, cosine_wave, exponential_signal, time_shift, time_scale, signal_addition, signal_multiplication

print("Demonstrating Signal Generation and Operations:")

# Task 1: Generate and plot a unit step signal and a unit impulse signal of length 20.
# (Your `main.py` snippet only demonstrates `unit_step(10)`)
print("\nTask 1: Generating Unit Step and Unit Impulse Signals (as per problem statement).")
n_length_discrete = 10 # Using 'n=10' as per your main.py snippet's call for unit_step
t_step, x_step = unit_step(n_length_discrete) # Plots automatically
t_impulse, x_impulse = unit_impulse(n_length_discrete) # Plots automatically

# Task 2: Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec.
# (Your `main.py` snippet calls `sine_wave(A=1, f=2, phase=0, duration=1)`)
print("\nTask 2: Generating a Sine Wave (as per problem statement).")
A_sine_req, f_sine_req, phase_sine_req, duration_sine_req = 2, 5, 0, 1 # Requirements [16]
t_sine_req, original_sine_req = sine_wave(A=A_sine_req, f=f_sine_req, phase=phase_sine_req, duration=duration_sine_req) # Plots automatically

# Task 3: Perform time shifting on the sine wave by +5 units and plot both original and shifted signals. [16]
print("\nTask 3: Performing Time Shifting on Sine Wave.")
shift_k = 5
t_shifted_sine, shifted_sine = time_shift(t_sine_req, original_sine_req, k=shift_k)

plt.figure(figsize=(10, 4))
plt.plot(t_sine_req, original_sine_req, label='Original Sine Wave')
plt.plot(t_shifted_sine, shifted_sine, label=f'Shifted Sine Wave (k={shift_k})', linestyle='--')
plt.title('Original and Time-Shifted Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Task 4: Perform addition of the unit step and ramp signal and plot the result. [16]
print("\nTask 4: Performing Addition of Unit Step and Ramp Signal.")
# Note: For addition, signals should ideally have the same time vector or be compatible.
# We'll use the time vector from the unit step for this demonstration.
t_ramp, x_ramp = ramp_signal(n_length_discrete) # Generate ramp for same 'n' as step

# Adjust ramp_signal's time vector to match unit_step's range for addition clarity (optional, but good practice)
# Your ramp_signal runs from 0 to n, unit_step from -n to n.
# For a clear plot, we'll demonstrate addition where both signals exist.
# A simpler approach for the beginner level is to use numpy's automatic broadcasting/padding
# or align them manually if their `t` arrays are directly comparable.
# Given your operations functions expect a common 't', we must ensure alignment.
# Let's align ramp to the -n to +n range of unit_step for demonstration.
# This requires slight adjustment to the ramp_signal or creating it over the full range.
# For simplicity, let's regenerate ramp over the same -n to +n range for addition:

t_common = np.arange(-n_length_discrete, n_length_discrete + 1)
x_step_aligned = (t_common >= 0).astype(int) # Unit step over -n to n
x_ramp_aligned = np.where(t_common >= 0, t_common, 0) # Ramp over -n to n

t_added, x_added = signal_addition(t_common, x_step_aligned, x_ramp_aligned)

plt.figure(figsize=(8, 4))
plt.plot(t_added, x_added, marker='o', linestyle='-', label='Added Signal')
plt.title('Addition of Unit Step and Ramp Signals')
plt.xlabel('n (Time Index)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Task 5: Multiply a sine and cosine wave of same frequency and plot the result. [11]
print("\nTask 5: Performing Multiplication of Sine and Cosine Waves.")
t_mul, x_sin_mul = sine_wave(A=1, f=2, phase=0, duration=1, fs=100) # Reduced fs for clearer marker 'o'
t_mul, x_cos_mul = cosine_wave(A=1, f=2, phase=0, duration=1, fs=100)

t_multiplied, x_multiplied = signal_multiplication(t_mul, x_sin_mul, x_cos_mul)

plt.figure(figsize=(10, 4))
plt.plot(t_multiplied, x_multiplied, marker='o', linestyle='-', label='Multiplied Signal')
plt.title('Multiplication of Sine and Cosine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


print("\nDemonstration tasks complete. Check the generated plots.")
