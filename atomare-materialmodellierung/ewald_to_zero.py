#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

LJ_S = 2
LJ_E = 1
lj = lambda x: 4 * LJ_E * ((LJ_S / x) ** 12 - (LJ_S / x) ** 6)
morse = lambda x: 1 * (1 - np.exp(-1 * (x - 2))) ** 2 - 1
coul = lambda x: -0.5 / x

x_min = 1e-2
x_max = 10
xs = np.linspace(x_min, x_max, 1000)

fig, ax = plt.subplots(figsize=(5, 3))
axins = inset_axes(ax, width=2, height=1.2, loc="lower left", bbox_to_anchor=(200, 20))

for a in [ax, axins]:
    a.plot(xs, lj(xs), label="Lennard-Jones", color="tab:blue")
    a.plot(xs, morse(xs), label="Morse", color="tab:orange")
    a.plot(xs, coul(xs), label="Coulomb", color="black") #"tab:green")
    a.plot([0, x_max], [0, 0], ":", color="grey")

ax.set_ylim(-2, 1.2)
ax.set_xlim(0, x_max)
ax.legend(loc="upper right", frameon=False)
ax.axis("off")

axins.set_xlim(5, x_max)
axins.set_ylim(-0.12, 0.01)
axins.set_yticks([])
axins.set_xticks([])

mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec="0.5")

plt.savefig(__file__.replace(".py", ".eps"))
