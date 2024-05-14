import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
z1 = np.add(x, y)
print(z1)

def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))
print(type(np.concatenate))
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

  