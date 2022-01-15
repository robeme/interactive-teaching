#!/usr/bin/env ptyhon3

import matplotlib.pyplot as plt
import numpy as np


def gauss(x, q):
    return lambda xi: q * ETA / (2 * np.pi) * np.exp(-((ETA * (xi - x)) ** 2 / 2))


CUTOFF = 9.5
atoms = [(3, 1), (7, -1), (11, -1), (14, 1), (19, -1)]  # x coordinate, charge
ETA = 1.5
YMAX = 1.2 * ETA / (2 * np.pi)
fig, axs = plt.subplots(3, 1, sharex=True, sharey=True)


### arrows
base_atom_i = 1
base_atom = atoms[base_atom_i]  # index of atom to draw from
# short range
x = base_atom[0]
# short range
for x_cut in [x + CUTOFF]:
    axs[0].plot((x_cut, x_cut), (-YMAX, YMAX), "k--")
    axs[0].text(x_cut, YMAX / 4, "Cutoff", rotation=270)
other_atoms = [a for a in atoms if a != base_atom]  # if a != base_atom]
for i, a in enumerate(other_atoms):
    if abs(a[0] - x) < CUTOFF:
        y = base_atom[1] * YMAX * ((i + 1) / (len(other_atoms) + 1))
        prop = {"arrowstyle": "->", "lw": 1, "color": "black"}
        axs[0].annotate(
            "",
            xy=(a[0], -a[1] * YMAX / 2),
            xytext=(x, y),
            arrowprops=prop,
        )
        axs[0].annotate(
            "",
            xy=(a[0], a[1] * YMAX / 2),
            xytext=(x, y),
            arrowprops=prop,
        )
# long range
y = base_atom[1] * YMAX / 2
prop = {"arrowstyle": "->", "lw": 1, "color": "black"}
for a in atoms:
    axs[1].annotate(
        "",
        xy=(a[0], a[1] * YMAX * 0.3),
        xytext=(x, y * 1.5),
        arrowprops=prop,
    )
# self interaction
axs[2].annotate(
    "",
    xy=(x, -y),
    xytext=(x, y),
    arrowprops=prop,
)

### charges
# gaussian charge densities
xmargin = 2
x_values = np.linspace(atoms[0][0] - xmargin, atoms[-1][0] + xmargin, 1000)
ys_long = np.zeros(x_values.shape)
ys_short = np.zeros(x_values.shape)
for i, (x, q) in enumerate(atoms):
    g = gauss(x, -q)
    ys_long -= g(x_values)
    if i != base_atom_i:
        ys_short += g(x_values)
axs[0].plot(x_values, ys_short, "--", color="tab:blue")
axs[1].plot(x_values, ys_long, "--", color="tab:blue")
g = gauss(base_atom[0], -base_atom[1])
axs[2].plot(
    x_values, gauss(base_atom[0], -base_atom[1])(x_values), "--", color="tab:blue"
)
# point charges
for i, (x, q) in enumerate(atoms):
    axs[0].plot([x, x], [0, q * YMAX], color="tab:orange")
axs[1].plot([base_atom[0], base_atom[0]], [0, base_atom[1] * YMAX], color="tab:orange")
axs[2].plot([base_atom[0], base_atom[0]], [0, base_atom[1] * YMAX], color="tab:orange")

# subplot settings
for ax in axs:
    ax.plot([x_values[0], x_values[-1]], [0, 0], color="black")

    ax.set_xlim(x_values[0], x_values[-1])
    ax.set_ylim(-YMAX, YMAX)
    ax.tick_params(
        which="both",  # both major and minor ticks are affected
        bottom=False,
        top=False,
        labelbottom=False,
        left=False,
        right=False,
        labelleft=False,
    )

# plot settings
for ax, title in zip(axs, ["Kurz", "Lang", "Selbst"]):
    ax.set_ylabel(title)
fig.add_subplot(111, frameon=False)
plt.tick_params(
    labelcolor="none", which="both", top=False, bottom=False, left=False, right=False
)
plt.xlabel(r"$r$")
plt.ylabel(r"$\rho$")
plt.subplots_adjust(wspace=0, hspace=0.03)

plt.savefig("ewald_charges.eps", format="eps")
