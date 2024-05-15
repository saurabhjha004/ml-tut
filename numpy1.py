import numpy as np

# 1D array operations
arr=np.array([1,2,3,4,5,6]) #declaring list
print(arr) #printing list
#searching in array
m = np.where(arr%2 == 1)
print(m)
n = np.searchsorted(arr, 5, side='right')
print(n)
#sorting in array
s = np.array([True, False, True])
print(np.sort(s))
#array split
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
#copy vs view
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
y = arr.view()
arr[0] = 28
print(arr)
print(y)
#joining list
l5 = np.concatenate((x, y))
print(l5)
l5 = np.hstack((x, y))
print(l5)
l5 = np.vstack((x, y))
print(l5)
l5 = np.dstack((x, y))
print(l5)
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
#reshaping array
l2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = l2.reshape(4, 3)
print(l2.reshape(4, 3).base)
print(l2)
#iterating array
for i in arr:
    print(i)
l3 = np.array([1, 2, 3])
for i in np.nditer(l3, flags=['buffered'], op_dtypes=['S']):
  print(i)
for idx, i in np.ndenumerate(l3):
  print(idx, i)

# 2D array operations
arr1=np.array([[1,2,3], [4,5,6]]) #creating 2D array
print(arr1)
#sorting in 2D array
print(np.sort(arr1))
print(arr1.shape) #shape checking
print('2nd element on 1st row: ', arr1[0, 1]) #accessing elements
#slicing methods
print(arr1[0:2, 2])
print(arr1[1, 1:4])
print(arr1[0:2, 1:4])
newarr = arr1.reshape(-1) #reshaping array
print(newarr)
#iterating array
for i in arr1:
  for j in i:
    print(j)
l4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(l4[:, ::2]):
  print(i)
#joining array
l6 = np.array([[1, 2], [3, 4]])
l7 = np.array([[5, 6], [7, 8]])
l8 = np.concatenate((l6, l7), axis=1)
print(l8)
l8 = np.stack((l6, l7), axis=1)
print(l8)
#2D array split
l9 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr1 = np.array_split(l9, 3)
print(newarr1)
newarr2 = np.array_split(l9, 3, axis=1) #or just use hsplit(l9, 3)
print(newarr2)

# 3D array operations
arr2=np.array([[[1,2,3], [4,5,6], [7,8,9]]]) #creating 3D array
print(arr2)
print(arr2[0, 1, 2]) #accessing elements
print(arr2.ndim)
arr3=np.array([1,2,3,4,5], ndmin=5) #setting an array of dimention 5
print(arr3)
print(arr3.shape) #shape checking
print('number of dimensions :', arr3.ndim)
#iterating array
for i in arr2:
  for j in i:
    for k in j:
      print(k)
for i in np.nditer(arr2):
  print(i)

#filter array method
ar = np.array([41, 42, 43, 44])
z = [True, False, True, False]
newar = arr[z]
print(newar)
# Create an empty list
filter_ar = []
# go through each element in ar
for element in ar:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_ar.append(True)
  else:
    filter_ar.append(False)
newar2 = arr[filter_ar]
print(filter_ar)
print(newar2)