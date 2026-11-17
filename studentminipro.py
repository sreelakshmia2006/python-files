import numpy as np
# -----STUDENT PERFORMANCE ANALYSIS SYSTEM MINI PROJECT-----

marks = np.array([
    [85,90,78,88,92],
    [65,70,68,72,60],
    [95,92,90,94,96],
    [55,60,35,62,58],
    [78,82,80,75,79],
    [45,38,42,50,48],
    [88,85,84,86,89],
    [30,40,35,32,39],
    [92,88,91,90,93],
    [76,79,77,80,75]
])

total = np.sum(marks,axis=1)                       # total mark of each student
print("Total marks:",total)
avg = np.mean(marks,axis=1)                        # avg of each student
print("Average marks:",avg)

print("\nSubject-wise avg:",np.mean(marks,axis=0))                # subject wise avg

topper = np.argmax(total)
print(f"\nTopper: student {topper+1} with {total[topper]} marks")

below_40 = np.any(marks < 40,axis=1)                          # students scored below 40 in any subject
print("\nBelow 40 in any subject - student nos:",np.where(below_40)[0]+1)

print("\nClass Average:",np.mean(marks))                            # class avg & std
print("Class Std Dev:",np.std(marks))

rank = np.argsort(total)[::-1] + 1                                  # rank based on total
print("Rank wise student nos (1st to last):",rank)
print("Topper is student",rank[0])

passed_all = np.all(marks >= 40,axis=1)                             # students passed every subject
print("\nPassed all subjects - student nos:",np.where(passed_all)[0]+1)
