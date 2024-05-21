import numpy as np

#adding two element in list
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
z1 = np.add(x, y)
print(z1)

#making own ufunc function for adding two arrays
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))
print(type(np.concatenate))
#checking whether the made function is ufunc or not
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

#doing arithmetic operations using in-built functions
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
newarr = np.subtract(arr1, arr2)
print(newarr)
newarr = np.multiply(arr1, arr2)
print(newarr)
newarr = np.divide(arr1, arr2)
print(newarr)
newarr = np.power(arr1, arr2)
print(newarr)
newarr = np.mod(arr1, arr2)
print(newarr)
newarr = np.remainder(arr1, arr2)
print(newarr)
newarr = np.divmod(arr1, arr2)
print(newarr)
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

#ways of rounding off
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.fix([-3.1666, 3.6667])
print(arr)
arr = np.around(3.1666, 2)
print(arr)
arr = np.floor([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)

#doing log operations
arr = np.arange(1, 10)
print(np.log2(arr))
arr = np.arange(1, 10)
print(np.log10(arr))
arr = np.arange(1, 10)
print(np.log(arr))
from math import log
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

# doing summation
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)
newarr = np.sum([arr1, arr2])
print(newarr)
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr) #cummulative sum
print(newarr)

#doing products
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr) #cummulative products
print(newarr)

#doing difference
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
newarr = np.diff(arr, n=2)
print(newarr)

#doing lcm
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
arr = np.array([3, 6, 9]) #lcm in array
x = np.lcm.reduce(arr)
print(x)
arr = np.arange(1, 11) #contain all integer between 1 to 10
x = np.lcm.reduce(arr)
print(x)

#doing gcd
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

#applying trigonometric functions
x = np.sin(np.pi/2)
print(x)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)
x = np.arcsin(1.0)
print(x)
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

#doing hyperbolic functions
x = np.sinh(np.pi/2)
print(x)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)
x = np.arcsinh(1.0)
print(x)
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)

#doing set operations
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)