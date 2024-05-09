import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100, size=(5))
print(x)
x1 = random.choice([3, 5, 7, 9], size=(3, 5))
print(x1)
x2 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x2)
x3 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x3)
y = random.rand(5)
print(y)
z = random.randint(100, size=(3, 5))
print(z)
z1 = random.rand(3, 5)
print(z1)
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)
print(random.permutation(arr))

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
