# def add(a):
#     if a==5:
#         return 0
#     else:
#        print(a)
#        add(a+1)

# add(1)



# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x * factorial(x-1))
# num = 3
# print("The factorial of",num,"is",factorial(num))



# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     prefix = strs[0]
#     for word in strs[1:]:                                              # second word muthal loop
#         while not word.startswith(prefix):                             # starting nokan
#             prefix = prefix[:-1]                                       # match allengil last letter remove
#             if not prefix:
#                 return ""
#     return prefix
# n = input("enter words :")
# words = [w.strip() for w in n.split(",")]
# print(longest_common_prefix(words))



# n = 5
# letters = "ABCDE"
# for i in range(1,n+1):                                                  # i=1,2,3,4,5 ennu loop oodum.(row number)
#     space = " " * (n-i)                                                 # space pyramid centre il kanan.
#     row = (letters[i-1] + " ") * i 
#     print(space + row)








# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i == n-1 or i+j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




nums = [3,4,-1,1]
n = len(nums)
for i in range(n):
    while 1 <= nums[i] <= n and nums[nums[i]-1]!= nums[i]:
        temp = nums[i]
        nums[i] = nums[temp-1]
        nums[temp-1] = temp
for i in range(n):
    if nums[i]!= i+1:
        print(i+1)
        break
else:
    print(n+1)                                       
                                                       





