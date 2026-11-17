# import numpy as np

# numbers=np.array([10,20,30,40,50,60])
# print(numbers[1:4])
# print(numbers[3:])
# print(numbers[::2])
# print(numbers[::-1])

    
     # Access elements in a two-dimensional array
# marks=np.array([
#     [80,85,90],
#     [70,75,80],
#     [90,95,85],
# ])
# print("first row:",marks[0])
# print("second row",marks[1,2])
# print("first column:",marks[:,0])                         # all rows, first column
# print(marks[:2,:])                                        # first two rows, all columns


      # Perform arithmetic operations
# a=np.array([10,20,30])
# b=np.array([1,2,3])

# print("addition:", a+b)
# print("subtraction:", a-b)
# print("multiplication:", a*b)
# print("division:", a/b)
# print("power:", a**2)


       # reshape an array
# numbers=np.arange(1,13)
# matrix=numbers.reshape(3,4)
# print(numbers.shape)
# print(matrix)
# print("shape:",matrix.shape)


       # join two arrays
# a=np.array([10,20,30])
# b=np.array([40,50,60])
# print("concatenate:",np.concatenate((a,b)))
# print("vertical stack:",np.vstack((a,b)))
# print("horizontal stack:",np.hstack((a,b)))


       # filter values using conditions
# marks = np.array([45,78,32,90,65,28,85])
# passed=marks[marks>=40]
# failed=marks[marks<40]
# high_scores=marks[marks>=80]
# print("passed:",passed)
# print("failed:",failed)
# print("high_scores:",high_scores)


       # mathematical and statistical operations
       # find sum,mean,medium and standard deviation

# marks=np.array([65,70,80,85,90,95])
# print("total:",np.sum(marks))
# print("average:",np.mean(marks))
# print("median:",np.median(marks))
# print("minimum:",np.min(marks))
# print("maximum:",np.max(marks))
# print("standard deviation:",round(np.std(marks)))


       # calculate row-wise and column-wise averages
# marks=np.array([
#     [80,70,90],
#     [60,85,75],
#     [90,95,85]
# ])
# print("student averages:")
# print(np.mean(marks,axis=1))

# print("student averages:")
# print(np.mean(marks,axis=0))
#   # axis=0 perform the operation column-wise,giving subject averages.

# print("student total:")
# print(np.sum(marks,axis=1))
  # axis=1 perform the operation row-wise,giving student averages.


      # generate random numbers
# np.random.seed(10)
# a=np.random.randint(1,101,size=10)
# b=np.random.rand(5)

# print("random integers:",a)
# print("random decimals:",b)

   # randint() generates random integer,while rand() generates random decimal values between 0 and 1.
   # using np.random.seed(10)marks the results reproducible.



# marks=np.array([78,45,92,65,88,54])
# sorted_marks=np.sort(marks)
# print("ascending:",sorted_marks)
# print("descending:",np.sort(marks)[::-1])
# print("original:",marks)
    # np.sort() returns a sorted array without changing the original array.








