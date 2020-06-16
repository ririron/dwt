import numpy as np
import matplotlib.pyplot as plt
from scale import calcScalingCoef



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

t = np.linspace(-5, 5, 16) 
f = np.sin(t)

sk0 = f #skの初期値
sk1 = calcScalingCoef(f)
wk1 = calcWaveletCoef(sk0)


plt.subplot(3, 1, 1)
plt.scatter(t, sk0)

plt.subplot(3, 1, 2)
plt.scatter(t[::2], sk1, color='red')

plt.subplot(3, 1, 3)
plt.scatter(t[::2], wk1, color='red')


plt.show()