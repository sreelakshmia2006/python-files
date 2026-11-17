# import numpy as np

# program 6         arithmetic operations
# a=np.array([10,20,30,40,50])
# b=np.array([2,4,5,8,10])
# print("Addition:",a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)
# print("Exponentiation:",a**b)


# program 7        array joining
# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print("concatenate axis=0 (vertical):\n",np.concatenate((a,b),axis=0))
# print("shape:",np.concatenate((a,b),axis=0).shape)
# print("\nconcatenate axis=1 (horizontal):\n",np.concatenate((a,b),axis=1))
# print("shape:",np.concatenate((a,b),axis=1).shape)

# print("\nvstack (same as axis=0):\n",np.vstack((a,b)))
# print("\nhstack (same as axis=1):\n",np.hstack((a,b)))


# program 8         sorting & searching
# array=np.array([45,12,89,34,67,23,90,56])
# print("Ascenting:",np.sort(array))
# print("Descending:",np.sort(array)[::-1])
# print("Index of highest:",np.argmax(array))                  # index of max value
# print("Index of lowest:",np.argmin(array))
# print("is 67 present?",67 in array)


# program 9          filtering values
# salary=np.array([18000,25000,32000,45000,28000,55000,60000,22000,75000,40000])
# print("greater than 30000:",salary[salary > 30000])
# print("less than 25000:",salary[salary < 25000])
# print("between 25000 and 50000:",salary[(salary >= 25000) & (salary <= 50000)])
# print("count > 40000:",np.sum(salary > 40000))


#-----program 10-----UNIQUE VALUES-----
# array=np.array([10,20,30,20,40,10,50,30,60,20])
# print("unique values:",np.unique(array))
# unique,counts = np.unique(array,return_counts=True)                  # np.uni - remove duplicate & return_count - count ethre thavana vannu 
# print(unique)
# print(counts)
# print("Duplicate:",unique[counts > 1])                               # counts>1=duplicate values filter cheyyan

