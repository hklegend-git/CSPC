"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt


fname = "decay_observed.csv"
fhandle = open(fname)

LAMBDA = 0.3     # decay constant, given

# reading and sorting data from "decay_observed.csv"

data = np.loadtxt(fname, delimiter=",", skiprows = 1)
t = data[:, 0]
observed = data[:, 1]

N0 = observed[0]

# finding analytical value with formula below 

analytical = N0 * np.exp(-LAMBDA * t) 

# making figure by using matplotlib

fig, ax = plt.subplots(1,2,  sharex = True, sharey = True) 

ax[0].scatter(t, observed)
ax[0].set_title("Observed")

ax[1].plot(t, analytical)
ax[1].set_title("Analytical")

ax[0].set_xlabel("Time")
ax[1].set_xlabel("Time")
ax[0].set_ylabel("Count")

plt.savefig("figure.png")
plt.show()



# TODO 4: save the figure as figure.png