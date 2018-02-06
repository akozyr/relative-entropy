import math
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

def gaussian(x, mu, sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2) / sigma / math.sqrt(2*math.pi)

x = np.arange(0, 255, 1)
y = []
for i in x:
    y.append(gaussian(i, 128, 2))

plt.plot(x, y)
plt.axis([0, 255, 0, 1])
plt.show()

print(reduce(lambda x, y: x + y, y))