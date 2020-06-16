import numpy as np
import matplotlib.pyplot as plt

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


t = np.linspace(-5, 5, 16) 
f = np.sin(t)

sk0 = f #skの初期値

sk1 = calcScalingCoef(f)
sk2 = calcScalingCoef(sk1)

plt.subplot(3, 1, 1)
plt.scatter(t, sk0)

plt.subplot(3, 1, 2)
plt.scatter(t[0:-1:2], sk1)

plt.subplot(3, 1, 3)
plt.scatter(t[0:-1:4], sk2)

plt.show()
