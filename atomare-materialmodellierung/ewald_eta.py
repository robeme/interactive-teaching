#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np


def summand(eta, k):
    return 1 / k ** 2 * np.exp(-(k ** 2) / (2 * eta ** 2))


plt.figure(figsize=(5, 2))
x = np.arange(1, 6)
for eta, mark in zip((1.0, 2.0, 4.0), ("s", "o", "v")):
    plt.plot(
        x, summand(eta, x), linestyle="None", marker=mark, label=r"$\eta = $" + str(eta)
    )

plt.ylim(0, 1)
plt.xlabel("k")
plt.ylabel(r"$k^{-2} \exp\left(- \frac{k^2}{2 \eta^2}\right) $")
plt.yticks(np.linspace(0, 1, 5, endpoint=True), ["0", "", "0.5", "", "1"])
plt.xticks(x, [str(xi) for xi in x])
plt.legend()
plt.tight_layout()
plt.savefig(__file__.replace(".py", ".eps"))
