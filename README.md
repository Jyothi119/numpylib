NumPY
Import numpy as np

1.What is numpy??
It is a library available in python for scientific computing.
It is also a multidimensional array.
2.What is multidimensional array??
It have both rows and columns

3.How to create an multidimensional array??
Import numpy as np
a = np.array([(1,2,3), (4,5,6)])

4.why are we using numpy over list??
1.it requires less memory compared to lists.
2.it is fast compared to lists
3.very convenient to work with numpy
Ex:
Import numpy as np
Import time
Import sys

s=range(1000)
Print(sys.getsizeof(5)*len(s))#it will give entire memory occupied by the list. sys.getsizeof(5) it will give the memory occupied by one element and then we will multiply with this by length of s then we will get the total memory occupied by the list.
d=np.arange(1000)# arange function will be same as ranage the only difference here is it will also include the 1000.
Print(d.size*d.itemsize)#it will give the total memory occupied by the elements. D.itemsize will give the size of one element and then we will multiply this with total size
5. it is fast compared to lists example??
Import numpy as np
Import sys
Size =100000# defining the variable size
L1=range(SIZE)#creating two lists L1 and L2
L2=range(SIZE)

A1=np.arange(SIZE)#creating two arrays
A2=np.arange(SIZE)

 Start= time.time()#the number of seconds passed
Result = [(x,y) for x,y in zip(L1,L2)]#calculating sum of l1 and l2
Print(time.time()-start*1000)#converting into milliseconds

Strat =time.time()
Result=A1+A2#calulating sum of a1 and a2 in numpy
Print(time.time()-start*1000)

Numpy operations:
1.Find the dimension of the array
2.Find the byte size of each element
3.find the data type of element
4.Find the size of an array: all number of elements present in the array
5.Find the shape of an array:total number of columns and total number of rows
6.reshape:whenever we are changing the number of rows and columns is called reshaping
7.slicing:
8.minimum
9.max
10.sum
11.axis:rows are called axis1 and columns are called axis 0
12.Finding the square root
13.Finding the standard deviation
14.addition, subtraction, divison, multiplication---it will all done by element wise

