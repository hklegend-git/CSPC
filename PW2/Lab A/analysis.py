"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: Reading and separating data of 'freefall.csv'

fname = "freefall.csv"

data = np.loadtxt(fname, delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]

# TODO 2: Finding gradient of parameters (y and v) and mean acceleration

v = np.gradient(y , t)
a = np.gradient(v, t)

mean_a = np.mean(a)

# TODO 3: Finding integration of parameters (v and a)

bua = cumulative_trapezoid(a, t, initial=0) + v[0]
buy = cumulative_trapezoid(bua, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - buy))

# TODO 4: Creatng 3 subploats of graphs and illustarting observed data

fig, ax = plt.subplots(3,1, figsize=(15,5), sharex = True)

ax[0].scatter(t, y, color = 'green', alpha = 0.5, label = 'Original' )
ax[0].plot(t, buy, color = 'darkblue', linestyle = '--', label = 'Recovered')
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Position (m)")
ax[0].set_title("Position")
ax[0].legend()
ax[0].grid(True)

ax[1].scatter(t, v, color = 'red', alpha = 0.5, label = 'Original')
ax[1].plot(t, bua, color = 'darkred', linestyle = '--', label = 'Recovered')
ax[1].set_title("Velocity")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Velocity (m/s)")
ax[1].legend()
ax[1].grid(True)

ax[2].scatter(t, a, color = 'blue', alpha = 0.5)
ax[2].axhline(y = -9.81, color = 'black', linestyle = ':', linewidth = 2, label = 'Theoretical value (-9.81)')
ax[2].set_title("Acceleration")
ax[2].set_xlabel("Time (s)")
ax[2].set_ylabel("Acceleration (m/s2)")
ax[2].legend()
ax[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png')
plt.show()

print("Mean Acceleration", mean_a)
print("max_diff", max_diff)


