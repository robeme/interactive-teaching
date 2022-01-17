#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc


def erfc_over_r(eta, r):
    return 1 / r * erfc(eta * r / np.sqrt(2))


plt.figure(figsize=(5, 2))
xmax = 2
x = np.linspace(0, xmax, 301, endpoint=True)[1:]
plt.plot(x, -1 / x, "k--", label="$1/r$")
for eta in (1.0, 2.0, 4.0):
    plt.plot(
        x,
        -erfc_over_r(eta, x),
        linestyle="-",
        label=r"$\eta = $" + str(eta),
    )

ymin=-2
plt.ylim(ymin, 0)
plt.xlim(0, xmax)
plt.xlabel(r"$r$")
plt.ylabel(r"- $\mathrm{erfc} \left(\frac{\eta r}{\sqrt{2}} \right) r^{-1}$")
plt.yticks(np.linspace(ymin, 0, 3, endpoint=True))
plt.xticks(np.linspace(0, xmax, 5, endpoint=True))
plt.legend()
plt.tight_layout()
plt.savefig(__file__.replace(".py", ".eps"))
