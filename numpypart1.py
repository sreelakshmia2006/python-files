# import numpy as np

# program 1     creating numpy array
# array = np.arange(1,21)             
# print("Array:",array)
# print("Number of elements:",array.size) 
# print("Data type:",array.dtype)
# print("Dimensions:",array.ndim)
# print("Shape:",array.shape) 


# program 2       even & odd numbers
# array = np.arange(1,51)                                 
# even = array[array % 2 == 0]
# odd = array[array % 2 != 0]
# print("Even numbers:",even)
# print("Odd numbers:",odd)
# print("Count of even:",even.size)
# print("Count of odd:",odd.size)


# program 3        indexing & slicing
# array = np.array([12,25,38,45,56,67,78,89,90,100])                 
# print("First 3:",array[0:3])
# print("Last 3:",array[-3:])
# print("Index 2 to 6:",array[2:7])
# print("Reverse:",array[::-1])
# array[4] = 99
# print("After replacing 5th element:",array)


# program 4        create matrix
# matrix = np.arange(1,10).reshape(3,3)                            # reshape(3,3) 1 to 9 ne 3*3 matrix akkan
# print("Matrix:\n",matrix)
# print("First row:",matrix[0])
# print("Last column:",matrix[:,-1])
# print("Diagonal:",np.diag(matrix))
# print("Sum of all elements:",np.sum(matrix))


# program 5         reshape an array
# array = np.arange(1,25)
# a=array.reshape(4,6)
# b=array.reshape(6,4)
# c=array.reshape(2,12)
# print("4*6:\n",a,"\nshape:",a.shape)
# print("\n6*4:\n",b,"\nshape:",b.shape)
# print("\n2*12:\n",c,"\nshape:",c.shape)

# or
# for rows,cols in [(4,6),(6,4),(2,12)]:
#     result = array.reshape(rows,cols)

