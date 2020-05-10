import numpy as np


#calculating the dimension of array
A=[(1,2,3), (4,5,6)]
Size=np.array(A)
print(Size.ndim)

#calculating the byte size of each element
A=[(1,2,3), (4,5,6)]
Size=np.array(A)
print(Size.itemsize)

#To calculate the data type of an array
A=[(1,2,3), (4,5,6)]
Size=np.array(A)
print(Size.dtype)

#to calculate the size of an array
A=np.array([(1,2,3), (4,5,6)])
print(A.size)

#To caluculate the shape of an array
A=np.array([(1,2,3,4,5,6,7),(8,9,10,11,12,13,14)])
print(A.shape)

#reshaping

a=np.array([(1,2,3,4),(8,9,10,11),(12,13,14,15)])
print(a[0:2,3])#it will only include 0th and 1st row
print(a[0:, 3])#it will include all rows

#Slicing:

a=np.array([(1,2,3,4),(8,9,10,11),(12,13,14,15)])
print(a[0:2,3])#it will only include 0th and 1st row
print(a[0:, 3])#it will include all rows

#Linspace
#it will print 3 numbers between 1 and 2 which are equally spaced.
a = np.linspace(1,2,3)
print(a)

#max
a = np.array([1,2,5])
print(a.max())

#min
a = np.array([1,2,5])
print(a.min())

#sum
a = np.array([1,2,5])
print(a.sum())

#Axis: suppose if we want to add number columns use axis=0
a = np.array([(1,2,5), (6,7,8)])
print(a.sum(axis=0))

#axis=1
a = np.array([(1,2,5), (6,7,8)])
print(a.sum(axis=1))

#Finding the square root: (sqrt)
a = np.array([(1,2,5), (6,7,8)])
print(np.sqrt(a))

#Finding the standard deviation: (std)
a = np.array([(1,2,5), (6,7,8)])
print(np.std(a))

#Addition
a = np.array([(1,2,5), (6,7,8)])
b= np.array([(1,2,5),(3,4,5)])
print(a+b)

#Multiplication
a = np.array([(1,2,5), (6,7,8)])
b= np.array([(1,2,5),(3,4,5)])
print(a*b)

#Division
a = np.array([(1,2,5), (6,7,8)])
b= np.array([(1,2,5),(3,4,5)])
print(a/b)

#Vertical stacking:
a = np.array([(1,2,5), (6,7,8)])
b= np.array([(1,2,5),(3,4,5)])
print(np.vstack((a,b)))

#Horizontal stacking:
a = np.array([(1,2,5), (6,7,8)])
b= np.array([(1,2,5),(3,4,5)])
print(np.hstack((a,b)))

#Ravel
a = np.array([(1,2,5), (6,7,8)])
print(a.ravel())

#Initialiying different types of arrays:
#1.	All 0’s matrix
print(np.zeros((2,3)))

#All one matrix
print(np.ones((2,3)))

#any other number
print(np.full((2,3), 99))

#full_like
a=[[1,2,3,4], [2,3,4,5]]
print(np.full_like(a,4))

#Random numbers
#1.random decimal numbers
print(np.random.rand(4,2))

#random integer values
print(np.random.randint(4,size=(2,2)))

#repeat an array
a=np.array([1,2,3])
print(np.repeat(a,2))

#matmul
a=np.full((3,2),3)
print(a)
b=np.ones((2,3))
print(b)
print(np.matmul(a,b))

#detc=np.identity(3)
c=np.identity(3)
print(np.linalg.det(c))





