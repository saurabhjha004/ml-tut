import numpy as np

# 1D array operations
arr=np.array([1,2,3,4,5,6]) #declaring list
print(arr) #printing list
#copy vs view
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
y = arr.view()
arr[0] = 28
print(arr)
print(y)
#if list owns its data
print(x.base)
print(y.base)
print(type(arr)) #data type in list
print(arr[0]+arr[1]) #indexing
#slicing methods 
print(arr[-3:-1])
print(arr[4:])
print(arr[1:5:2])
print(arr.dtype)
#string list
str = np.array(['apple', 'banana', 'cherry'])
print(str.dtype)
#declaring list with data type
l1 = np.array([1, 2, 3, 4], dtype='S')
print(l1)
print(l1.dtype)
#iterating elements
for i in arr:
    print(i)
#reshaping array
l2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = l2.reshape(4, 3)
print(l2.reshape(4, 3).base)
print(l2)
l3 = np.array([1, 2, 3])
for i in np.nditer(l3, flags=['buffered'], op_dtypes=['S']):
  print(i)
for idx, i in np.ndenumerate(l3):
  print(idx, i)

# 2D array operations
arr1=np.array([[1,2,3], [4,5,6]])
print(arr1)
print(arr1.shape)
print('2nd element on 1st row: ', arr1[0, 1])
print(arr1[0:2, 2])
print(arr1[1, 1:4])
print(arr1[0:2, 1:4])
newarr = arr1.reshape(-1)
print(newarr)
for i in arr1:
  for j in i:
    print(j)
l4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(l4[:, ::2]):
  print(i)

# 3D array operations
arr2=np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr2)
print(arr2[0, 1, 2])
print(arr2.ndim)
arr3=np.array([1,2,3,4,5], ndmin=5)
print(arr3)
print(arr3.shape)
print('number of dimensions :', arr3.ndim)
for i in arr2:
  for j in i:
    for k in j:
      print(k)
for i in np.nditer(arr2):
  print(i)