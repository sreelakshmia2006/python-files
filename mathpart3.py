#-----program 11-----STUDENT MARK ANALYSIS-----
# import numpy as np

# marks=np.array([78,85,92,45,67,89,55,76,95,62])
# print("Total:",np.sum(marks))
# print("Average:",np.mean(marks))
# print("Highest:",np.max(marks))
# print("Lowest:",np.min(marks))
# print("Median:",np.median(marks))
# print("Standard deviation:",np.std(marks))


#-----program 12-----VARIANCE & STANDARD DEVIATION-----
# a=np.array([50,50,50,50,50])
# b=np.array([40,45,50,55,60])
# c=np.array([10,30,50,70,90])
# print("A - Mean:",np.mean(a),"Var:",np.var(a),"Std:",np.std(a))
# print("B - Mean:",np.mean(b),"Var:",np.var(b),"Std:",np.std(b))
# print("C - Mean:",np.mean(c),"Var:",np.var(c),"Std:",np.std(c))
# print("\nHighest variation is C")


#-----program 13-----SUBJECT WISE AVERAGE-----
# marks=np.array([[80,75,90],
#                 [65,85,70],
#                 [90,95,88],
#                 [55,60,65],
#                 [75,80,85]])
# print("Student total:",np.sum(marks,axis=1))                  # each students total & avg (row wise)
# print("Student averages:",np.mean(marks,axis=1))
# print("Student averages:",np.mean(marks,axis=0))              # each subject average(column wise)
# totals = np.sum(marks,axis=1)
# print("Topper is student",np.argmax(totals)+1,"with",np.max(totals),"marks")


#-----program 14-----RANDOM NUMBER GENERATION-----
# np.random.seed(10)
# nums=np.random.randint(1,101,20)                          # 1 to 100 vare 20 numbers
# print("Numbers:",nums)
# print("Max:",np.max(nums),"Min:",np.min(nums),"Mean:",np.mean(nums))
# print("Count > 50:",np.sum(nums > 50))
# print("Sorted:",np.sort(nums))


#-----program 15-----PERCENTAGE & RANKING-----
# marks=np.array([[85,90,78,88],
#                 [65,70,68,72],
#                 [95,92,90,94],
#                 [55,60,58,62],
#                 [78,82,80,75]])
# print(marks)
# total=np.sum(marks,axis=1)                            # axis=1 row wise
# percent=total / 400 * 100
# print("totals:",total)
# print("percent:",percent)
# order=np.argsort(percent)[::-1]
# print("Rank wise students:",order+1)
# print("toper student",np.argmax(percent)+1)

                  #or
# s=marks.shape
# percentage=(np.sum(marks,axis=1)/(s[1]*100))*100