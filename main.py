import numpy as np
import matplotlib.pyplot as plt
from util import calcScalingCoef, calcWaveletCoef



t = np.linspace(-5, 5, 16) 
f = np.sin(t)

sk0 = f #skの初期値
sk1 = calcScalingCoef(f)
sk2 = calcScalingCoef(sk1)
wk1 = calcWaveletCoef(sk0)
wk2 = calcWaveletCoef(sk1)

plt.subplot(5, 1, 1)
plt.scatter(t, sk0)

plt.subplot(5, 1, 2)
plt.scatter(t[::2], sk1, color='red')

plt.subplot(5, 1, 3)
plt.scatter(t[::2], wk1, color='red')

plt.subplot(5, 1, 4)
plt.scatter(t[::4], sk2, color='green')

plt.subplot(5, 1, 5)
plt.scatter(t[::4], wk2, color='green')

plt.show()