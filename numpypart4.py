# import numpy as np
# program 16        employee salary
# salary=np.array([18000,22000,25000,30000,35000,40000,45000,50000,55000,60000])
# print("Avg:",np.mean(salary))
# print("High:",np.max(salary),"Low:",np.min(salary))
# print("Total expense:",np.sum(salary))
# print("Above avg:",salary[salary > np.mean(salary)])
# print("Std:",np.std(salary))


# program 17         weekly sales
# sales=np.array([12000,15000,18000,10000,22000,25000,20000])
# days = np.array(["monday","tuesday","wednesday","thursday","friday","saturday","sunday"])
# print(days)
# high = np.argmax(sales)
# print(high)
# low = np.argmin(sales)
# print(low)
# print("total:",np.sum(sales),"avg:",np.mean(sales))
# print("Highest day:",days[high],"Lowest day:",days[low])

# print("sorted high to low:",np.sort(sales)[::-1])
# print("days with sales above 18000")
# d = days[sales > 18000]
# print(d)
# e = sales[sales > 18000]
# print(e)
# for day,amount in zip(d , e):
#     print(day,":",amount)


# program 18         attendance analysis
# attendence=np.array([95,88,76,65,92,55,80,45,98,72])
# print("Above 75%:",attendence[attendence > 75])
# print("Below 60%:",attendence[attendence < 60])
# print("Avg:",np.mean(attendence))
# print("High:",np.max(attendence))
# print("Low:",np.min(attendence))
# print("Eligible for exam:",np.sum(attendence >= 75),"students")


# program 19         temperature analysis
# temp=np.array([29,31,30,32,28,35,33])
# print("Avg temp:",np.mean(temp))
# print("High temp:",np.max(temp))
# print("Low temp:",np.min(temp))
# print("Range:",np.max(temp)-np.min(temp))
# print("Std:",np.std(temp))
# print("Days > 30C (Day num):",np.where(temp > 30)[0]+1)


# program 20          image array basics
# image=np.array([
#     [10,20,30,40,50],
#     [60,70,80,90,100],
#     [110,120,130,140,150],
#     [160,170,180,190,200],
#     [210,220,230,240,250]
# ])
# print("Array:\n",image)
# print("Min:",np.min(image))
# print("Max:",np.max(image))
# print("Avg:",np.mean(image))
# modified_image=image.copy()
# print(modified_image)
# modified_image[modified_image < 100]=0
# modified_image[modified_image > 200]=225
# print("Modified image:",modified_image)
# print(image)
          # or
# img[img < 100]=0
# print("\nBelow 100 -> 0:\n",img)
# img[img >= 200]=255
# print("\n>=200 -> 225:\n",img)
