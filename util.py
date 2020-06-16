#関数をまとめてここにおく
import numpy as np
import matplotlib.pyplot as plt


def calcWaveletCoef(f):
    y = []
    i = 0
    q0 = np.sqrt(2) ** -1
    q1 = -1 * q0
    for x in f:
        if i > len(f) -2:
            break
        ansR = q0 * f[i]
        ansL = q1 * f[i+1]
        result = ansR + ansL
        i += 2
        y.append(result)

    return y


def calcScalingCoef(f):
    y = []
    i = 0
    p0 = p1 = np.sqrt(2)**-1
    for x in f:
        if i > len(f) -2:
            break
        ansR = p0 * f[i]
        ansL = p1 * f[i+1]
        result = ansR + ansL
        i += 2
        y.append(result)

    return y
