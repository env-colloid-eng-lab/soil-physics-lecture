from __future__ import division

import numpy as np


def linear(n, depth):
    z = np.zeros(n + 2, float)
    dz = depth / n
    z[0] = 0
    z[1] = 0
    for i in range(1, n + 1):
        z[i + 1] = z[i] + dz
    return z


def geometric(n, depth):
    z = np.zeros(n + 2, float)
    my_sum = 0.0
    for i in range(1, n + 1):
        my_sum += i * i
    dz = depth / my_sum
    z[0] = 0.0
    z[1] = 0.0
    for i in range(1, n + 1):
        z[i + 1] = z[i] + dz * i * i
    return z
