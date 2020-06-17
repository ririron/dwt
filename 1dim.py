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

plt.subplots_adjust(wspace=0.4, hspace=0.6)

plt.subplot(3, 1, 1)
plt.title("Sk0 = f[n]")
plt.scatter(t, sk0)

plt.subplot(3, 1, 2)
plt.title("Sk1")
plt.scatter(t[::2], sk1, color='red')

plt.subplot(3, 1, 3)
plt.title("Wk1")
plt.scatter(t[::2], wk1, color='red')


plt.show()