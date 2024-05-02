import numpy as np

# 1D array operations
arr=np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))
print(arr[0]+arr[1])
print(arr[-3:-1])
print(arr[4:])
print(arr[1:5:2])
print(arr.dtype)
for i in arr:
    print(i)

# 2D array operations
arr1=np.array([[1,2,3], [4,5,6]])
print(arr1)
print('2nd element on 1st row: ', arr1[0, 1])
print(arr1[0:2, 2])
print(arr1[1, 1:4])
print(arr1[0:2, 1:4])
str = np.array(['apple', 'banana', 'cherry'])
print(str.dtype)

# 3D array operations
arr2=np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr2)
print(arr2[0, 1, 2])
print(arr2.ndim)
arr3=np.array([1,2,3,4,5], ndmin=5)
print(arr3)
print('number of dimensions :', arr3.ndim)