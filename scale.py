import numpy as np
import matplotlib.pyplot as plt

def haalScalingFunc(x): 
    y = 0
    if 0 <= x and x < 1:
        y = 1
    return y 

def calcScalingFunc(f):
    y = []
    for i, x in enumerate(f[:-1]):
        if i % 2 == 0:
            ansR = haalScalingFunc(f[i+1])
            ansL = haalScalingFunc(f[i+2])
            result = np.sqrt(2)**-1 * (ansR + ansL + x)
            y.append(result)

    y.append(f[-1])
    return y

t = np.linspace(-5, 5, 17) 
f = np.sin(t)

maxLevel = 5 

#sk = np.zeros((maxLevel, len(f)))
sk0 = f #skの初期値

sk1 = calcScalingFunc(f)
sk2 = calcScalingFunc(sk1)

plt.subplot(3, 1, 1)
plt.scatter(t, sk0)

plt.subplot(3, 1, 2)
plt.scatter(t[::2], sk1)

plt.subplot(3, 1, 3)
plt.scatter(t[::4], sk2)

plt.show()
